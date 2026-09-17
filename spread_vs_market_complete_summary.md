# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-19 to 2026-09-15
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-19 to 2026-09-15
- Overlap observations: 2462
- Level correlation: 0.0826
- Same-day return correlation: 0.0167
- Next-day return correlation: -0.0547

### Nasdaq Composite

- Overlap window: 2016-09-19 to 2026-09-15
- Overlap observations: 2462
- Level correlation: 0.0528
- Same-day return correlation: 0.0206
- Next-day return correlation: -0.0551

### Dow Jones Industrial Average

- Overlap window: 2016-09-19 to 2026-09-15
- Overlap observations: 2462
- Level correlation: 0.1205
- Same-day return correlation: 0.0040
- Next-day return correlation: -0.0445

### VIX

- Overlap window: 2016-09-19 to 2026-09-15
- Overlap observations: 2462
- Level correlation: -0.0503
- Same-day return correlation: 0.0378
- Next-day return correlation: -0.0058

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
