# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-08 to 2026-04-07
- Spread observations: 2513

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2513
- Level correlation: 0.0726
- Same-day return correlation: 0.0085
- Next-day return correlation: -0.0380

### Nasdaq Composite

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2513
- Level correlation: 0.0403
- Same-day return correlation: 0.0124
- Next-day return correlation: -0.0373

### Dow Jones Industrial Average

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2513
- Level correlation: 0.1368
- Same-day return correlation: -0.0014
- Next-day return correlation: -0.0323

### VIX

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2513
- Level correlation: -0.0194
- Same-day return correlation: 0.0355
- Next-day return correlation: -0.0078

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
