# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-01 to 2026-07-27
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-01 to 2026-07-27
- Overlap observations: 2462
- Level correlation: 0.0583
- Same-day return correlation: 0.0171
- Next-day return correlation: -0.0565

### Nasdaq Composite

- Overlap window: 2016-08-01 to 2026-07-27
- Overlap observations: 2462
- Level correlation: 0.0272
- Same-day return correlation: 0.0211
- Next-day return correlation: -0.0566

### Dow Jones Industrial Average

- Overlap window: 2016-08-01 to 2026-07-27
- Overlap observations: 2462
- Level correlation: 0.1027
- Same-day return correlation: 0.0051
- Next-day return correlation: -0.0472

### VIX

- Overlap window: 2016-08-01 to 2026-07-27
- Overlap observations: 2462
- Level correlation: -0.0341
- Same-day return correlation: 0.0386
- Next-day return correlation: -0.0018

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
