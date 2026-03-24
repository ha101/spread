# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-03-24 to 2026-03-23
- Spread observations: 2467

## Correlations By Series

### S&P 500

- Overlap window: 2016-03-24 to 2026-03-23
- Overlap observations: 2467
- Level correlation: 0.0576
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0621

### Nasdaq Composite

- Overlap window: 2016-03-24 to 2026-03-23
- Overlap observations: 2467
- Level correlation: 0.0238
- Same-day return correlation: 0.0228
- Next-day return correlation: -0.0613

### Dow Jones Industrial Average

- Overlap window: 2016-03-24 to 2026-03-23
- Overlap observations: 2467
- Level correlation: 0.1293
- Same-day return correlation: 0.0054
- Next-day return correlation: -0.0534

### VIX

- Overlap window: 2016-03-24 to 2026-03-23
- Overlap observations: 2467
- Level correlation: -0.0408
- Same-day return correlation: 0.0368
- Next-day return correlation: 0.0056

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
