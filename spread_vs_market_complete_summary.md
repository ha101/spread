# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-20 to 2026-05-11
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-20 to 2026-05-11
- Overlap observations: 2459
- Level correlation: 0.1293
- Same-day return correlation: 0.0178
- Next-day return correlation: -0.0569

### Nasdaq Composite

- Overlap window: 2016-05-20 to 2026-05-11
- Overlap observations: 2459
- Level correlation: 0.0999
- Same-day return correlation: 0.0220
- Next-day return correlation: -0.0570

### Dow Jones Industrial Average

- Overlap window: 2016-05-20 to 2026-05-11
- Overlap observations: 2459
- Level correlation: 0.1810
- Same-day return correlation: 0.0052
- Next-day return correlation: -0.0474

### VIX

- Overlap window: 2016-05-20 to 2026-05-11
- Overlap observations: 2459
- Level correlation: -0.0247
- Same-day return correlation: 0.0378
- Next-day return correlation: -0.0002

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
