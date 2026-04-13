#!/usr/bin/env python3
"""
Walk-forward backtest: predicting the Brent–WTI crude oil spread.

Models
------
  1. Naive        – last observed value; historical-vol intervals
  2. AR(1)+t      – AR(1) on daily changes, Student-t innovations
  3. OU+t         – Ornstein-Uhlenbeck with rolling params, Student-t intervals
  4. TimesFM      – zero-shot foundation model (if installed)

Benchmarks
----------
  - 1-month futures spread (for the 20-day horizon only)

Evaluation
----------
  Window     : 2018-01-01 → end of data
  Re-forecast: every 21 trading days
  Horizons   : 1, 5, 20 trading days
  Metrics    : MAE, directional accuracy, pinball loss, 80 % interval coverage
"""

import json, re, sys, time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# ── Optional: TimesFM ──────────────────────────────────────────────
HAS_TIMESFM = False
try:
    import timesfm, torch
    HAS_TIMESFM = True
except Exception:
    pass

ROOT = Path(__file__).resolve().parent

# ═══════════════════════════════════════════════════════════════════
#  DATA LOADING
# ═══════════════════════════════════════════════════════════════════

def load_spot() -> pd.DataFrame:
    """Parse all_data.js → DataFrame[date, wti, brent, spread]."""
    text = (ROOT / "all_data.js").read_text()
    raw = re.search(r"window\.ALL_DATA\s*=\s*(\[.*?\])\s*;", text, re.DOTALL)
    data = json.loads(raw.group(1))
    rows = []
    for d, wti, brent in data:
        if wti is not None and brent is not None:
            rows.append((pd.Timestamp(d), float(wti), float(brent),
                         round(float(brent) - float(wti), 4)))
    df = pd.DataFrame(rows, columns=["date", "wti", "brent", "spread"])
    return df.sort_values("date").reset_index(drop=True)


def load_futures_1m() -> pd.DataFrame:
    """Parse futures_data.js → DataFrame[date, fut1m] for the 1-month tenor."""
    text = (ROOT / "futures_data.js").read_text()
    # Find the "1m": { rows: [...] } block — keys are unquoted JS
    # Locate start of 1m rows
    start = text.find('"1m": {')
    if start < 0:
        start = text.find('"1m":{')
    if start < 0:
        return pd.DataFrame(columns=["date", "fut1m"])
    rows_start = text.find("rows:", start)
    if rows_start < 0:
        return pd.DataFrame(columns=["date", "fut1m"])
    # Find the matching closing bracket for the rows array
    bracket_start = text.find("[", rows_start)
    # Scan for all entries until we hit the closing of the 1m block
    chunk = text[bracket_start:]
    # Find end: next "}," or "}" that closes the 1m object
    end_idx = chunk.find("\n  },")
    if end_idx < 0:
        end_idx = chunk.find("\n  }")
    if end_idx > 0:
        chunk = chunk[:end_idx]
    entries = re.findall(r'\["(\d{4}-\d{2}-\d{2})",\s*([\-\d.]+)\]', chunk)
    rows = [(pd.Timestamp(d), float(v)) for d, v in entries]
    df = pd.DataFrame(rows, columns=["date", "fut1m"])
    return df.sort_values("date").reset_index(drop=True)


# ═══════════════════════════════════════════════════════════════════
#  MODEL DEFINITIONS
# ═══════════════════════════════════════════════════════════════════

N_SIMS = 5_000          # Monte-Carlo draws for interval estimation
WINDOW = 1_260          # rolling window ≈ 5 years


def _fit_t(resid: np.ndarray):
    """Fit Student-t to residuals; return (df, loc, scale)."""
    with np.errstate(all="ignore"):
        return stats.t.fit(resid)


# ── 1. Naive ──────────────────────────────────────────────────────

def forecast_naive(history: np.ndarray, horizon: int) -> dict:
    last = history[-1]
    changes = np.diff(history[-WINDOW:]) if len(history) > WINDOW else np.diff(history)
    vol = np.std(changes) * np.sqrt(horizon)
    return dict(
        point=last,
        q10=last - 1.28 * vol,
        q90=last + 1.28 * vol,
    )


# ── 2. AR(1) on changes + Student-t ──────────────────────────────

def forecast_ar1(history: np.ndarray, horizon: int) -> dict:
    h = history[-WINDOW:] if len(history) > WINDOW else history
    changes = np.diff(h)
    if len(changes) < 30:
        return forecast_naive(history, horizon)

    y, x = changes[1:], changes[:-1]
    # OLS for phi
    xm, ym = x.mean(), y.mean()
    phi = np.dot(x - xm, y - ym) / (np.dot(x - xm, x - xm) + 1e-12)
    resid = y - (phi * x)

    df_t, loc_t, scale_t = _fit_t(resid)

    last_spread = history[-1]
    last_change = changes[-1]

    # Analytical point forecast (geometric sum)
    if abs(phi) < 0.999:
        cum = last_change * phi * (1.0 - phi ** horizon) / (1.0 - phi)
    else:
        cum = last_change * phi * horizon
    point = last_spread + cum

    # Simulate for intervals
    innov = stats.t.rvs(df_t, loc=loc_t, scale=scale_t, size=(N_SIMS, horizon))
    paths = np.empty((N_SIMS, horizon))
    paths[:, 0] = phi * last_change + innov[:, 0]
    for step in range(1, horizon):
        paths[:, step] = phi * paths[:, step - 1] + innov[:, step]
    finals = last_spread + paths.cumsum(axis=1)[:, -1]

    return dict(
        point=point,
        q10=np.percentile(finals, 10),
        q90=np.percentile(finals, 90),
    )


# ── 3. OU + Student-t ────────────────────────────────────────────

def forecast_ou(history: np.ndarray, horizon: int) -> dict:
    h = history[-WINDOW:] if len(history) > WINDOW else history
    S = h.astype(np.float64)
    dS = np.diff(S)
    S_lag = S[:-1]
    n = len(S_lag)
    if n < 60:
        return forecast_naive(history, horizon)

    # OLS: dS = a + b * S_lag + eps   →   b = -kappa, a = kappa * mu
    Sx = S_lag.sum()
    Sy = dS.sum()
    Sxx = (S_lag ** 2).sum()
    Sxy = (S_lag * dS).sum()
    denom = n * Sxx - Sx * Sx
    if abs(denom) < 1e-12:
        return forecast_naive(history, horizon)
    b = (n * Sxy - Sx * Sy) / denom
    a = (Sy - b * Sx) / n

    kappa = max(-b, 0.005)       # floor: very weak mean reversion
    mu = a / kappa

    resid = dS - (a + b * S_lag)
    sigma = np.std(resid)

    S_t = history[-1]
    # E[S_{t+h}] = mu + (S_t - mu) * exp(-kappa * h)
    point = mu + (S_t - mu) * np.exp(-kappa * horizon)

    # Var[S_{t+h}] = sigma^2 / (2*kappa) * (1 - exp(-2*kappa*h))
    var_h = (sigma ** 2 / (2 * kappa)) * (1.0 - np.exp(-2 * kappa * horizon))
    sd_h = np.sqrt(max(var_h, 1e-12))

    # Student-t intervals
    df_t, _, _ = _fit_t(resid / (sigma + 1e-12))
    q10 = point + stats.t.ppf(0.10, df_t) * sd_h
    q90 = point + stats.t.ppf(0.90, df_t) * sd_h

    return dict(point=point, q10=q10, q90=q90, kappa=kappa, mu=mu)


# ── 4. TimesFM (zero-shot) ───────────────────────────────────────

_tfm_model = None   # lazy singleton

def _get_timesfm(max_horizon: int = 20):
    global _tfm_model
    if _tfm_model is None and HAS_TIMESFM:
        torch.set_float32_matmul_precision("high")
        m = timesfm.TimesFM_2p5_200M_torch.from_pretrained(
            "google/timesfm-2.5-200m-pytorch"
        )
        m.compile(timesfm.ForecastConfig(
            max_context=2048,
            max_horizon=max_horizon,
            normalize_inputs=True,
            use_continuous_quantile_head=True,
            force_flip_invariance=True,
            infer_is_positive=False,      # spread can be negative
            fix_quantile_crossing=True,
        ))
        _tfm_model = m
    return _tfm_model


def forecast_timesfm(history: np.ndarray, horizon: int) -> dict | None:
    model = _get_timesfm(max_horizon=horizon)
    if model is None:
        return None
    ctx = history[-2048:] if len(history) > 2048 else history
    point_fc, quant_fc = model.forecast(horizon=horizon, inputs=[ctx.astype(np.float32)])
    # quant_fc shape: (1, horizon, 11) — mean + 10th..90th percentiles
    # Index 0 = mean, 1 = p10, ..., 9 = p90
    pt = float(point_fc[0, -1])          # point at final step
    q10 = float(quant_fc[0, -1, 1])      # 10th percentile at final step
    q90 = float(quant_fc[0, -1, 9])      # 90th percentile at final step
    return dict(point=pt, q10=q10, q90=q90)


# ═══════════════════════════════════════════════════════════════════
#  WALK-FORWARD ENGINE
# ═══════════════════════════════════════════════════════════════════

MODELS = [
    ("naive",   forecast_naive),
    ("ar1_t",   forecast_ar1),
    ("ou_t",    forecast_ou),
]
if HAS_TIMESFM:
    MODELS.append(("timesfm", forecast_timesfm))

HORIZONS = [1, 5, 20]
STEP = 21                # re-forecast every ~month
EVAL_START = "2018-01-01"
MIN_TRAIN = 1_260         # need ≥5 years of history


def run_backtest(spot_df: pd.DataFrame, fut_df: pd.DataFrame) -> pd.DataFrame:
    spreads = spot_df["spread"].values
    dates = spot_df["date"].values
    max_h = max(HORIZONS)

    # Merge futures for 20-day benchmark
    fut_map = {}
    if len(fut_df):
        for _, row in fut_df.iterrows():
            fut_map[row["date"]] = row["fut1m"]

    eval_start_idx = spot_df[spot_df["date"] >= EVAL_START].index[0]
    start_idx = max(MIN_TRAIN, eval_start_idx)
    n_cutoffs = (len(spot_df) - max_h - start_idx) // STEP + 1

    print(f"Running walk-forward: {n_cutoffs} cutoffs × {len(HORIZONS)} horizons × {len(MODELS)} models")
    rows = []
    t0 = time.time()

    for ci, cutoff_idx in enumerate(range(start_idx, len(spot_df) - max_h, STEP)):
        history = spreads[: cutoff_idx]
        cutoff_date = dates[cutoff_idx - 1]

        if (ci + 1) % 10 == 0:
            elapsed = time.time() - t0
            print(f"  cutoff {ci + 1}/{n_cutoffs}  ({elapsed:.1f}s)")

        for h in HORIZONS:
            target_idx = cutoff_idx + h - 1
            if target_idx >= len(spreads):
                continue
            y_true = spreads[target_idx]
            target_date = dates[target_idx]

            for model_name, model_fn in MODELS:
                try:
                    pred = model_fn(history, h)
                except Exception as e:
                    print(f"  !! {model_name} h={h} @ {cutoff_date}: {e}")
                    continue
                if pred is None:
                    continue
                rows.append(dict(
                    cutoff=cutoff_date, target=target_date, horizon=h,
                    model=model_name,
                    y_true=y_true, point=pred["point"],
                    q10=pred["q10"], q90=pred["q90"],
                ))

            # Futures benchmark (h=20 only)
            if h == 20 and pd.Timestamp(cutoff_date) in fut_map:
                fp = fut_map[pd.Timestamp(cutoff_date)]
                # Futures spread is the predicted spread level
                # Use naive vol for intervals
                naive_pred = forecast_naive(history, h)
                rows.append(dict(
                    cutoff=cutoff_date, target=target_date, horizon=h,
                    model="futures_1m",
                    y_true=y_true, point=fp,
                    q10=naive_pred["q10"], q90=naive_pred["q90"],
                ))

    elapsed = time.time() - t0
    print(f"Done in {elapsed:.1f}s — {len(rows)} forecast rows")
    return pd.DataFrame(rows)


# ═══════════════════════════════════════════════════════════════════
#  SCORING
# ═══════════════════════════════════════════════════════════════════

def pinball(y_true, q, tau):
    """Pinball loss for quantile tau."""
    diff = y_true - q
    return np.where(diff >= 0, tau * diff, (tau - 1) * diff).mean()


def score(results: pd.DataFrame) -> pd.DataFrame:
    """Compute metrics grouped by model × horizon."""
    records = []
    for (model, h), g in results.groupby(["model", "horizon"]):
        yt = g["y_true"].values
        pt = g["point"].values
        q10 = g["q10"].values
        q90 = g["q90"].values

        err = yt - pt
        mae = np.abs(err).mean()
        rmse = np.sqrt((err ** 2).mean())

        # Directional accuracy: did we predict the direction of change?
        # "change" = y_true at target vs spread at cutoff
        # Since we forecasted the level, direction = sign(point - last) vs sign(y_true - last)
        # We approximate "last" as y_true - (y_true - point) ... better: use stored data
        # Actually, our naive model's point IS the last value, so:
        naive_rows = results[(results["model"] == "naive") & (results["horizon"] == h)]
        if len(naive_rows) == len(g):
            last_vals = naive_rows["point"].values   # naive point = last spread
            actual_dir = np.sign(yt - last_vals)
            pred_dir = np.sign(pt - last_vals)
            mask = actual_dir != 0
            dir_acc = (actual_dir[mask] == pred_dir[mask]).mean() if mask.sum() > 0 else np.nan
        else:
            dir_acc = np.nan

        # Pinball loss at 10th and 90th percentiles
        pb10 = pinball(yt, q10, 0.10)
        pb90 = pinball(yt, q90, 0.90)
        pb_avg = (pb10 + pb90) / 2

        # 80% interval coverage
        covered = ((yt >= q10) & (yt <= q90)).mean()

        # Interval width
        width = (q90 - q10).mean()

        records.append(dict(
            model=model, horizon=h, n=len(g),
            mae=mae, rmse=rmse, dir_acc=dir_acc,
            pinball_avg=pb_avg, coverage_80=covered,
            interval_width=width,
        ))

    return pd.DataFrame(records)


# ═══════════════════════════════════════════════════════════════════
#  OUTPUT
# ═══════════════════════════════════════════════════════════════════

def print_summary(metrics: pd.DataFrame):
    print("\n" + "=" * 80)
    print("  WALK-FORWARD BACKTEST RESULTS — Brent–WTI Spread")
    print("  Evaluation window: 2018-01-01 → present")
    print("  Re-forecast every 21 trading days")
    print("=" * 80)

    for h in HORIZONS:
        hm = metrics[metrics["horizon"] == h].sort_values("mae")
        print(f"\n{'─' * 80}")
        print(f"  HORIZON: {h} {'day' if h == 1 else 'days'}")
        print(f"{'─' * 80}")
        print(f"  {'Model':<12} {'MAE':>7} {'RMSE':>7} {'Dir%':>6} {'Pinball':>8} "
              f"{'Cov80%':>7} {'Width':>7}  n")
        print(f"  {'─'*12} {'─'*7} {'─'*7} {'─'*6} {'─'*8} {'─'*7} {'─'*7}  ──")
        for _, r in hm.iterrows():
            da = f"{r['dir_acc']:.1%}" if not np.isnan(r["dir_acc"]) else "  n/a"
            print(f"  {r['model']:<12} {r['mae']:7.3f} {r['rmse']:7.3f} {da:>6} "
                  f"{r['pinball_avg']:8.4f} {r['coverage_80']:6.1%} "
                  f"{r['interval_width']:7.2f}  {int(r['n'])}")

    # Best model per horizon
    print(f"\n{'─' * 80}")
    print("  SUMMARY")
    print(f"{'─' * 80}")
    for h in HORIZONS:
        hm = metrics[metrics["horizon"] == h]
        best_mae = hm.loc[hm["mae"].idxmin()]
        best_cov = hm.loc[(hm["coverage_80"] - 0.80).abs().idxmin()]
        print(f"  h={h:>2}d  Best MAE: {best_mae['model']:<12} ({best_mae['mae']:.3f})"
              f"    Best calibrated: {best_cov['model']:<12} (cov={best_cov['coverage_80']:.1%})")


def save_outputs(results: pd.DataFrame, metrics: pd.DataFrame):
    results.to_csv(ROOT / "backtest_predictions.csv", index=False)
    metrics.to_csv(ROOT / "backtest_summary.csv", index=False)
    print(f"\n  Saved: backtest_predictions.csv ({len(results)} rows)")
    print(f"  Saved: backtest_summary.csv")

    # ── Chart ──
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=False)
        fig.suptitle("Walk-Forward Backtest: Brent–WTI Spread", fontsize=14, fontweight="bold")

        for ax, h in zip(axes, HORIZONS):
            hm = metrics[metrics["horizon"] == h].sort_values("mae")
            models = hm["model"].values
            maes = hm["mae"].values
            colors = ["#5b9bf7" if m != "naive" else "#7c7c85" for m in models]
            bars = ax.barh(models, maes, color=colors, edgecolor="none", height=0.6)
            ax.set_title(f"{h}-day horizon", fontsize=12)
            ax.set_xlabel("MAE ($)")
            ax.invert_yaxis()
            for bar, v in zip(bars, maes):
                ax.text(v + 0.02, bar.get_y() + bar.get_height() / 2,
                        f"${v:.3f}", va="center", fontsize=10)

        plt.tight_layout()
        fig.savefig(ROOT / "backtest_results.png", dpi=150, bbox_inches="tight",
                    facecolor="white")
        plt.close()
        print(f"  Saved: backtest_results.png")
    except Exception as e:
        print(f"  (chart skipped: {e})")


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print("Loading data...")
    spot = load_spot()
    fut = load_futures_1m()
    print(f"  Spot: {len(spot)} obs, {spot['date'].min().date()} → {spot['date'].max().date()}")
    print(f"  Futures 1m: {len(fut)} obs")

    if HAS_TIMESFM:
        print("  TimesFM: available ✓")
    else:
        print("  TimesFM: not installed — skipping")

    results = run_backtest(spot, fut)
    metrics = score(results)
    print_summary(metrics)
    save_outputs(results, metrics)


if __name__ == "__main__":
    main()
