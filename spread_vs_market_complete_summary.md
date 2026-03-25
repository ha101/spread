# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-03-28 to 2026-03-23
- Spread observations: 2466

## Correlations By Series

### S&P 500

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: 0.0569
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0622

### Nasdaq Composite

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: 0.0231
- Same-day return correlation: 0.0228
- Next-day return correlation: -0.0614

### Dow Jones Industrial Average

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: 0.1285
- Same-day return correlation: 0.0054
- Next-day return correlation: -0.0534

### VIX

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: -0.0412
- Same-day return correlation: 0.0368
- Next-day return correlation: 0.0056

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
