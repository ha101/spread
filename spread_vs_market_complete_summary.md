# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-03-31 to 2026-03-23
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-03-31 to 2026-03-23
- Overlap observations: 2463
- Level correlation: 0.0614
- Same-day return correlation: 0.0158
- Next-day return correlation: -0.0604

### Nasdaq Composite

- Overlap window: 2016-03-31 to 2026-03-23
- Overlap observations: 2463
- Level correlation: 0.0279
- Same-day return correlation: 0.0207
- Next-day return correlation: -0.0593

### Dow Jones Industrial Average

- Overlap window: 2016-03-31 to 2026-03-23
- Overlap observations: 2463
- Level correlation: 0.1311
- Same-day return correlation: 0.0034
- Next-day return correlation: -0.0528

### VIX

- Overlap window: 2016-03-31 to 2026-03-23
- Overlap observations: 2463
- Level correlation: -0.0384
- Same-day return correlation: 0.0387
- Next-day return correlation: 0.0045

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
