# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-22 to 2026-04-20
- Spread observations: 2465

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-22 to 2026-04-20
- Overlap observations: 2465
- Level correlation: 0.1186
- Same-day return correlation: 0.0177
- Next-day return correlation: -0.0549

### Nasdaq Composite

- Overlap window: 2016-04-22 to 2026-04-20
- Overlap observations: 2465
- Level correlation: 0.0879
- Same-day return correlation: 0.0226
- Next-day return correlation: -0.0537

### Dow Jones Industrial Average

- Overlap window: 2016-04-22 to 2026-04-20
- Overlap observations: 2465
- Level correlation: 0.1757
- Same-day return correlation: 0.0040
- Next-day return correlation: -0.0467

### VIX

- Overlap window: 2016-04-22 to 2026-04-20
- Overlap observations: 2465
- Level correlation: -0.0192
- Same-day return correlation: 0.0388
- Next-day return correlation: -0.0013

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
