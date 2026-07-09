# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-11 to 2026-07-06
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-11 to 2026-07-06
- Overlap observations: 2462
- Level correlation: 0.0710
- Same-day return correlation: 0.0179
- Next-day return correlation: -0.0575

### Nasdaq Composite

- Overlap window: 2016-07-11 to 2026-07-06
- Overlap observations: 2462
- Level correlation: 0.0401
- Same-day return correlation: 0.0217
- Next-day return correlation: -0.0572

### Dow Jones Industrial Average

- Overlap window: 2016-07-11 to 2026-07-06
- Overlap observations: 2462
- Level correlation: 0.1177
- Same-day return correlation: 0.0066
- Next-day return correlation: -0.0479

### VIX

- Overlap window: 2016-07-11 to 2026-07-06
- Overlap observations: 2462
- Level correlation: -0.0286
- Same-day return correlation: 0.0382
- Next-day return correlation: -0.0002

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
