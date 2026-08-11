# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-11 to 2026-08-03
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-11 to 2026-08-03
- Overlap observations: 2459
- Level correlation: 0.0562
- Same-day return correlation: 0.0162
- Next-day return correlation: -0.0539

### Nasdaq Composite

- Overlap window: 2016-08-11 to 2026-08-03
- Overlap observations: 2459
- Level correlation: 0.0250
- Same-day return correlation: 0.0204
- Next-day return correlation: -0.0535

### Dow Jones Industrial Average

- Overlap window: 2016-08-11 to 2026-08-03
- Overlap observations: 2459
- Level correlation: 0.0994
- Same-day return correlation: 0.0033
- Next-day return correlation: -0.0445

### VIX

- Overlap window: 2016-08-11 to 2026-08-03
- Overlap observations: 2459
- Level correlation: -0.0384
- Same-day return correlation: 0.0383
- Next-day return correlation: -0.0036

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
