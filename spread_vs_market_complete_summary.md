# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-22 to 2026-04-13
- Spread observations: 2460

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-22 to 2026-04-13
- Overlap observations: 2460
- Level correlation: 0.1006
- Same-day return correlation: 0.0193
- Next-day return correlation: -0.0559

### Nasdaq Composite

- Overlap window: 2016-04-22 to 2026-04-13
- Overlap observations: 2460
- Level correlation: 0.0685
- Same-day return correlation: 0.0245
- Next-day return correlation: -0.0551

### Dow Jones Industrial Average

- Overlap window: 2016-04-22 to 2026-04-13
- Overlap observations: 2460
- Level correlation: 0.1609
- Same-day return correlation: 0.0061
- Next-day return correlation: -0.0464

### VIX

- Overlap window: 2016-04-22 to 2026-04-13
- Overlap observations: 2460
- Level correlation: -0.0192
- Same-day return correlation: 0.0386
- Next-day return correlation: 0.0002

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
