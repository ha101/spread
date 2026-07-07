# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-08 to 2026-06-29
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-08 to 2026-06-29
- Overlap observations: 2459
- Level correlation: 0.0785
- Same-day return correlation: 0.0178
- Next-day return correlation: -0.0574

### Nasdaq Composite

- Overlap window: 2016-07-08 to 2026-06-29
- Overlap observations: 2459
- Level correlation: 0.0477
- Same-day return correlation: 0.0213
- Next-day return correlation: -0.0571

### Dow Jones Industrial Average

- Overlap window: 2016-07-08 to 2026-06-29
- Overlap observations: 2459
- Level correlation: 0.1257
- Same-day return correlation: 0.0067
- Next-day return correlation: -0.0478

### VIX

- Overlap window: 2016-07-08 to 2026-06-29
- Overlap observations: 2459
- Level correlation: -0.0289
- Same-day return correlation: 0.0383
- Next-day return correlation: -0.0004

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
