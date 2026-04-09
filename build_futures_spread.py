"""Build futures spread data for Brent-WTI at various tenors.

For each trading day, determines which CME contract represents N months out,
fetches Brent and WTI prices for that contract, and computes the spread.
Uses front-month continuous tickers (CL=F, BZ=F) for the 1m tenor.

Produces two resolution tiers:
  - daily: full history back to 2015 (from individual contract CSVs)
  - hourly: last ~730 days (from Yahoo Finance 1h interval), accumulating
    in the cache so history grows beyond the rolling window over time.

Outputs futures_data.js for the website.
"""

from datetime import date, timedelta
from pathlib import Path

from yfinance_utils import (
    MONTH_CODES,
    fetch_futures_contract,
    fetch_futures_contract_hourly,
    fetch_yfinance_daily,
    fetch_front_month_hourly,
    _read_cache,
    _read_cache_hourly,
)

BASE_PATH = Path(__file__).parent
CACHE_DIR = BASE_PATH / 'futures_cache'
OUTPUT_PATH = BASE_PATH / 'futures_data.js'

TENORS = [1, 2, 3, 6, 12, 24]
TENOR_LABELS = ['1m', '2m', '3m', '6m', '12m', '24m']

# How far back to attempt fetching contracts.
START_YEAR = 2015


def contract_month_for_tenor(trading_date, tenor_months):
    """Given a trading date and a tenor in months, return (year, month) of the
    target contract.

    Convention: on any day in month M, the contract N months out is the one
    with delivery month M + N.  For example, on any day in April 2026 with
    tenor=1, the target is May 2026.
    """
    month = trading_date.month + tenor_months
    year = trading_date.year
    while month > 12:
        month -= 12
        year += 1
    return year, month


def enumerate_contracts(start_year, end_year):
    """Return a list of (year_2digit, month_index, month_code, full_year) for
    all contract months from start_year through end_year inclusive."""
    contracts = []
    for year in range(start_year, end_year + 1):
        y2 = year % 100
        for mi, code in enumerate(MONTH_CODES):
            contracts.append((y2, mi + 1, code, year))
    return contracts


def fetch_front_month_series():
    """Fetch front-month continuous contract data for WTI and Brent.

    Returns (wti_dict, brent_dict) where each is {date_str: price}.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    wti = fetch_yfinance_daily('CL=F', '2000-01-01', CACHE_DIR / 'CL_front.csv')
    brent = fetch_yfinance_daily('BZ=F', '2000-01-01', CACHE_DIR / 'BZ_front.csv')
    return wti, brent


def fetch_all_contracts(contracts):
    """Fetch WTI (CL) and Brent (BZ) prices for every contract in the list.

    Returns two dicts keyed by (full_year, month) -> {date_str: price}.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    wti_by_contract = {}
    brent_by_contract = {}

    for y2, month_num, code, full_year in contracts:
        key = (full_year, month_num)

        # Skip contracts that expired long ago (more than 2 months before today).
        contract_expiry_approx = date(full_year, month_num, 1)
        if contract_expiry_approx < date.today() - timedelta(days=60):
            # Only use cached data for expired contracts.
            wti_cache = CACHE_DIR / f'CL{code}{y2:02d}.csv'
            bz_cache = CACHE_DIR / f'BZ{code}{y2:02d}.csv'
            if wti_cache.exists():
                wti_by_contract[key] = _read_cache(wti_cache)
            if bz_cache.exists():
                brent_by_contract[key] = _read_cache(bz_cache)
            continue

        try:
            wti_by_contract[key] = fetch_futures_contract('CL', code, y2, CACHE_DIR)
        except Exception as exc:
            print(f'  Warning: CL{code}{y2:02d} fetch failed: {exc}')

        try:
            brent_by_contract[key] = fetch_futures_contract('BZ', code, y2, CACHE_DIR)
        except Exception as exc:
            print(f'  Warning: BZ{code}{y2:02d} fetch failed: {exc}')

    return wti_by_contract, brent_by_contract


# ── Hourly data ─────────────────────────────────────────────────────

def fetch_front_month_hourly_series():
    """Fetch hourly front-month continuous data for WTI and Brent.

    Returns (wti_dict, brent_dict) where each is {datetime_str: price}.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    return fetch_front_month_hourly(CACHE_DIR)


def fetch_all_contracts_hourly(contracts):
    """Fetch hourly data for non-expired contracts.

    Returns two dicts keyed by (full_year, month) -> {datetime_str: price}.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    wti_by_contract = {}
    brent_by_contract = {}

    for y2, month_num, code, full_year in contracts:
        key = (full_year, month_num)

        contract_expiry_approx = date(full_year, month_num, 1)
        if contract_expiry_approx < date.today() - timedelta(days=60):
            # For expired contracts, only use cached hourly data.
            wti_cache = CACHE_DIR / f'CL{code}{y2:02d}_hourly.csv'
            bz_cache = CACHE_DIR / f'BZ{code}{y2:02d}_hourly.csv'
            if wti_cache.exists():
                wti_by_contract[key] = _read_cache_hourly(wti_cache)
            if bz_cache.exists():
                brent_by_contract[key] = _read_cache_hourly(bz_cache)
            continue

        try:
            wti_by_contract[key] = fetch_futures_contract_hourly('CL', code, y2, CACHE_DIR)
        except Exception as exc:
            print(f'  Warning: CL{code}{y2:02d} hourly fetch failed: {exc}')

        try:
            brent_by_contract[key] = fetch_futures_contract_hourly('BZ', code, y2, CACHE_DIR)
        except Exception as exc:
            print(f'  Warning: BZ{code}{y2:02d} hourly fetch failed: {exc}')

    return wti_by_contract, brent_by_contract


# ── Spread building ─────────────────────────────────────────────────

def build_front_month_spread(wti_front, brent_front):
    """Build the 1m spread from continuous front-month tickers."""
    common_dates = sorted(set(wti_front) & set(brent_front))
    return [
        [d, round(brent_front[d] - wti_front[d], 2)]
        for d in common_dates
    ]


def build_tenor_series(wti_by_contract, brent_by_contract, tenor_months):
    """Build a spread series for a given tenor.

    Returns a sorted list of [datetime_or_date_str, spread_value].
    """
    # Collect all trading timestamps from all contracts.
    all_timestamps = set()
    for series in list(wti_by_contract.values()) + list(brent_by_contract.values()):
        all_timestamps.update(series.keys())

    rows = []
    for ts in sorted(all_timestamps):
        # Extract date portion (works for both 'YYYY-MM-DD' and 'YYYY-MM-DD HH:MM').
        date_part = ts[:10]
        parts = date_part.split('-')
        if len(parts) != 3:
            continue
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
        try:
            trading_date = date(y, m, d)
        except ValueError:
            continue

        target_year, target_month = contract_month_for_tenor(trading_date, tenor_months)
        key = (target_year, target_month)

        wti_price = wti_by_contract.get(key, {}).get(ts)
        brent_price = brent_by_contract.get(key, {}).get(ts)

        if wti_price is not None and brent_price is not None:
            spread = round(brent_price - wti_price, 2)
            rows.append([ts, spread])

    return rows


def merge_daily_hourly(daily_rows, hourly_rows):
    """Merge daily and hourly spread rows, preferring hourly where available.

    Daily rows have keys like 'YYYY-MM-DD'.
    Hourly rows have keys like 'YYYY-MM-DD HH:MM'.

    For dates that have hourly data, the daily row is dropped.
    Result is sorted chronologically.
    """
    # Find dates covered by hourly data.
    hourly_dates = set()
    for row in hourly_rows:
        hourly_dates.add(row[0][:10])

    # Keep daily rows only for dates with no hourly coverage.
    merged = [row for row in daily_rows if row[0][:10] not in hourly_dates]
    merged.extend(hourly_rows)
    merged.sort(key=lambda r: r[0])
    return merged


# ── Output ──────────────────────────────────────────────────────────

def format_js_rows(rows):
    """Format rows as a JS array string."""
    lines = ['[']
    for i, row in enumerate(rows):
        suffix = ',' if i < len(rows) - 1 else ''
        lines.append(f'    ["{row[0]}", {row[1]:.2f}]{suffix}')
    lines.append('    ]')
    return '\n'.join(lines)


def write_output(tenor_rows):
    """Write futures_data.js."""
    parts = ['window.FUTURES_DATA = {']
    labels = ', '.join(f'"{t}"' for t in TENOR_LABELS)
    parts.append(f'  tenors: [{labels}],')

    for label, rows in zip(TENOR_LABELS, tenor_rows):
        parts.append(f'  "{label}": {{')
        parts.append(f'    rows: {format_js_rows(rows)},')
        parts.append('  },')

    parts.append('};')
    parts.append('')
    OUTPUT_PATH.write_text('\n'.join(parts))


def main():
    today = date.today()
    end_year = today.year + 2
    contracts = enumerate_contracts(START_YEAR, end_year)
    print(f'Enumerating {len(contracts)} contract months from {START_YEAR} to {end_year}')

    # ── Daily data (full history) ──
    print('Fetching front-month continuous data (daily)...')
    wti_front, brent_front = fetch_front_month_series()
    print(f'  CL=F: {len(wti_front)} days, BZ=F: {len(brent_front)} days')

    print('Fetching individual contract data (daily)...')
    wti_by_contract, brent_by_contract = fetch_all_contracts(contracts)
    print(f'  WTI contracts with data: {len(wti_by_contract)}')
    print(f'  Brent contracts with data: {len(brent_by_contract)}')

    # ── Hourly data (last ~730 days, accumulating) ──
    print('Fetching front-month continuous data (hourly)...')
    wti_front_h, brent_front_h = fetch_front_month_hourly_series()
    print(f'  CL=F hourly: {len(wti_front_h)} bars, BZ=F hourly: {len(brent_front_h)} bars')

    # Only fetch hourly for contracts that are within Yahoo's ~730-day window.
    hourly_cutoff = today - timedelta(days=730)
    hourly_contracts = [
        c for c in contracts
        if date(c[3], c[1], 1) >= hourly_cutoff
    ]
    print(f'Fetching individual contract data (hourly, {len(hourly_contracts)} contracts)...')
    wti_by_contract_h, brent_by_contract_h = fetch_all_contracts_hourly(hourly_contracts)
    print(f'  WTI hourly contracts with data: {len(wti_by_contract_h)}')
    print(f'  Brent hourly contracts with data: {len(brent_by_contract_h)}')

    # ── Build and merge spread series ──
    tenor_rows = []
    for tenor, label in zip(TENORS, TENOR_LABELS):
        if tenor == 1:
            daily_rows = build_front_month_spread(wti_front, brent_front)
            hourly_rows = build_front_month_spread(wti_front_h, brent_front_h)
        else:
            daily_rows = build_tenor_series(wti_by_contract, brent_by_contract, tenor)
            hourly_rows = build_tenor_series(wti_by_contract_h, brent_by_contract_h, tenor)

        merged = merge_daily_hourly(daily_rows, hourly_rows)
        tenor_rows.append(merged)

        daily_count = len(daily_rows)
        hourly_count = len(hourly_rows)
        total_count = len(merged)
        if merged:
            print(f'  {label}: {total_count} points ({daily_count} daily + {hourly_count} hourly, {merged[0][0]} to {merged[-1][0]})')
        else:
            print(f'  {label}: 0 points')

    write_output(tenor_rows)
    print(f'Wrote {OUTPUT_PATH.name}')


if __name__ == '__main__':
    main()
