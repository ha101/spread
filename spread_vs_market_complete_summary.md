# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-04 to 2026-03-30
- Spread observations: 2466

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-04 to 2026-03-30
- Overlap observations: 2466
- Level correlation: 0.0759
- Same-day return correlation: 0.0153
- Next-day return correlation: -0.0604

### Nasdaq Composite

- Overlap window: 2016-04-04 to 2026-03-30
- Overlap observations: 2466
- Level correlation: 0.0428
- Same-day return correlation: 0.0202
- Next-day return correlation: -0.0592

### Dow Jones Industrial Average

- Overlap window: 2016-04-04 to 2026-03-30
- Overlap observations: 2466
- Level correlation: 0.1427
- Same-day return correlation: 0.0026
- Next-day return correlation: -0.0524

### VIX

- Overlap window: 2016-04-04 to 2026-03-30
- Overlap observations: 2466
- Level correlation: -0.0261
- Same-day return correlation: 0.0394
- Next-day return correlation: 0.0038

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
