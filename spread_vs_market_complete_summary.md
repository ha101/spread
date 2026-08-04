# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-04 to 2026-07-27
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-04 to 2026-07-27
- Overlap observations: 2459
- Level correlation: 0.0562
- Same-day return correlation: 0.0172
- Next-day return correlation: -0.0565

### Nasdaq Composite

- Overlap window: 2016-08-04 to 2026-07-27
- Overlap observations: 2459
- Level correlation: 0.0250
- Same-day return correlation: 0.0212
- Next-day return correlation: -0.0566

### Dow Jones Industrial Average

- Overlap window: 2016-08-04 to 2026-07-27
- Overlap observations: 2459
- Level correlation: 0.1002
- Same-day return correlation: 0.0051
- Next-day return correlation: -0.0471

### VIX

- Overlap window: 2016-08-04 to 2026-07-27
- Overlap observations: 2459
- Level correlation: -0.0354
- Same-day return correlation: 0.0385
- Next-day return correlation: -0.0019

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
