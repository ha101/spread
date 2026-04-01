# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-01 to 2026-03-23
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-01 to 2026-03-23
- Overlap observations: 2462
- Level correlation: 0.0606
- Same-day return correlation: 0.0157
- Next-day return correlation: -0.0603

### Nasdaq Composite

- Overlap window: 2016-04-01 to 2026-03-23
- Overlap observations: 2462
- Level correlation: 0.0271
- Same-day return correlation: 0.0206
- Next-day return correlation: -0.0592

### Dow Jones Industrial Average

- Overlap window: 2016-04-01 to 2026-03-23
- Overlap observations: 2462
- Level correlation: 0.1302
- Same-day return correlation: 0.0033
- Next-day return correlation: -0.0527

### VIX

- Overlap window: 2016-04-01 to 2026-03-23
- Overlap observations: 2462
- Level correlation: -0.0388
- Same-day return correlation: 0.0389
- Next-day return correlation: 0.0043

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
