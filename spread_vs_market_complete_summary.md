# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-15 to 2026-04-08
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-15 to 2026-04-08
- Overlap observations: 2463
- Level correlation: 0.0748
- Same-day return correlation: 0.0179
- Next-day return correlation: -0.0598

### Nasdaq Composite

- Overlap window: 2016-04-15 to 2026-04-08
- Overlap observations: 2463
- Level correlation: 0.0421
- Same-day return correlation: 0.0227
- Next-day return correlation: -0.0584

### Dow Jones Industrial Average

- Overlap window: 2016-04-15 to 2026-04-08
- Overlap observations: 2463
- Level correlation: 0.1393
- Same-day return correlation: 0.0059
- Next-day return correlation: -0.0508

### VIX

- Overlap window: 2016-04-15 to 2026-04-08
- Overlap observations: 2463
- Level correlation: -0.0248
- Same-day return correlation: 0.0342
- Next-day return correlation: 0.0020

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
