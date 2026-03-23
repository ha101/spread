# Benchmark Data Audit

Audit date: 2026-03-23

## Scope

- `all_data.js`
- `benchmark_data.js`
- `wti_monthly_fred.csv`
- `brent_monthly_fred.csv`
- `dubai_monthly_fred.csv`

## Summary

- The daily Brent/WTI dataset is clean: sorted ascending, no duplicate dates, no null prices.
- `benchmark_data.js.daily` is an exact mirror of `all_data.js`.
- The monthly benchmark dataset is clean and sorted, with no duplicate dates.
- Dubai is monthly only. There are no internal gaps inside the Dubai coverage window.
- The only missing Dubai values in `benchmark_data.js.monthly` are expected:
  - leading nulls before Dubai begins in 2003-01-01
  - one trailing null at 2026-02-01 because the raw Dubai series currently stops at 2026-01-01
- Rounded monthly values in `benchmark_data.js` match the raw FRED cache files exactly after rounding to 2 decimals.

## Coverage

| Series | File | Rows | First | Last |
| --- | --- | ---: | --- | --- |
| WTI / Brent daily | `all_data.js` | 9681 | 1987-05-20 | 2026-03-23 |
| WTI / Brent daily | `benchmark_data.js.daily` | 9681 | 1987-05-20 | 2026-03-23 |
| WTI monthly raw | `wti_monthly_fred.csv` | 482 | 1986-01-01 | 2026-02-01 |
| Brent monthly raw | `brent_monthly_fred.csv` | 466 | 1987-05-01 | 2026-02-01 |
| Dubai monthly raw | `dubai_monthly_fred.csv` | 277 | 2003-01-01 | 2026-01-01 |
| Combined monthly benchmark data | `benchmark_data.js.monthly` | 466 | 1987-05-01 | 2026-02-01 |

## Missing Values

Within `benchmark_data.js.monthly`:

| Column | Null rows | Notes |
| --- | ---: | --- |
| `wti` | 0 | complete across retained monthly rows |
| `brent` | 0 | complete across retained monthly rows |
| `dubai` | 189 | 188 leading null months before 2003-01-01, plus 1 trailing null month at 2026-02-01 |

There are no interior Dubai null runs between the first and last non-null Dubai observations. That means the Dubai coverage window itself is contiguous from 2003-01-01 through 2026-01-01.

## Pairwise Overlap Windows

Using the generated frontend dataset:

| Pair | Frequency | Rows | First | Last |
| --- | --- | ---: | --- | --- |
| Brent - WTI | daily | 9681 | 1987-05-20 | 2026-03-23 |
| Brent - WTI | monthly | 466 | 1987-05-01 | 2026-02-01 |
| Brent - Dubai | monthly | 277 | 2003-01-01 | 2026-01-01 |
| WTI - Dubai | monthly | 277 | 2003-01-01 | 2026-01-01 |

## Consistency Checks

- `benchmark_data.js.daily` exactly matches `all_data.js`
- monthly rounded value checks:
  - WTI: 466 checked, 0 mismatches
  - Brent: 466 checked, 0 mismatches
  - Dubai: 277 checked, 0 mismatches

## Frontend Implication

Dubai is a monthly series overlaid onto a daily Brent/WTI chart when requested. That means very short daily horizons can legitimately show zero Dubai points if no Dubai observation falls inside that date window. The frontend horizon filter was updated so those short windows are now anchored to the daily chart end date instead of leaking older Dubai points into `1D`, `1W`, or `1M`.
