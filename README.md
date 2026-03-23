# Crude Benchmark Spreads

Static chart site for Brent, WTI, and Dubai benchmark spread views.

## What is in the repo

- `index.html`: the frontend
- `benchmark_data.js`: chart data used by the frontend
- `refresh_spread_history.py`: refreshes daily Brent and WTI history
- `build_benchmark_dataset.py`: rebuilds the combined benchmark dataset
- `build_site_bundle.py`: stages the deployable static site into `dist/`

## Data frequency

- WTI and Brent in this repo come from public FRED daily series.
- Dubai in this repo comes from FRED series `POILDUBUSDM`, which is monthly.

This repository is set up for daily refreshes, not intraday streaming. In practice that matches the current public upstream sources: daily for WTI and Brent, monthly for Dubai.

## Local preview

```bash
python3 -m http.server 8765
```

Then open `http://127.0.0.1:8765/index.html`.

## GitHub Pages deployment

This repo includes two workflows:

- `.github/workflows/pages.yml`: deploys the current site on push to the default branch or via manual run
- `.github/workflows/refresh-data.yml`: refreshes data once each weekday, commits changed generated files, and deploys the updated site

The deployed artifact is built from `build_site_bundle.py` and currently contains:

- `index.html`
- `benchmark_data.js`
- `.nojekyll`
- optional `CNAME` if you add one at the repo root

## GitHub setup

1. Create a GitHub repository and push this folder.
2. In the repository settings, enable GitHub Pages and choose `GitHub Actions` as the source.
3. Confirm that Actions are enabled for the repository.
4. If you want a custom domain, add a `CNAME` file at the repo root before deploying.

## Scheduled refresh behavior

The refresh workflow runs at:

- `15:20` UTC
- Monday through Friday

The run is offset away from the top of the hour because GitHub notes that scheduled workflows can be delayed when Actions load is high near `:00`.

## Important limitation

The current setup is intentionally daily. If you later want intraday updates, you would need both an intraday-capable source and a different refresh cadence.
