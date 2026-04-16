# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-18 to 2026-04-13
- Spread observations: 2464

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-18 to 2026-04-13
- Overlap observations: 2464
- Level correlation: 0.1025
- Same-day return correlation: 0.0193
- Next-day return correlation: -0.0557

### Nasdaq Composite

- Overlap window: 2016-04-18 to 2026-04-13
- Overlap observations: 2464
- Level correlation: 0.0706
- Same-day return correlation: 0.0243
- Next-day return correlation: -0.0551

### Dow Jones Industrial Average

- Overlap window: 2016-04-18 to 2026-04-13
- Overlap observations: 2464
- Level correlation: 0.1630
- Same-day return correlation: 0.0061
- Next-day return correlation: -0.0462

### VIX

- Overlap window: 2016-04-18 to 2026-04-13
- Overlap observations: 2464
- Level correlation: -0.0181
- Same-day return correlation: 0.0385
- Next-day return correlation: 0.0001

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
