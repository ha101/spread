# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-15 to 2026-07-06
- Spread observations: 2458

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-15 to 2026-07-06
- Overlap observations: 2458
- Level correlation: 0.0681
- Same-day return correlation: 0.0178
- Next-day return correlation: -0.0575

### Nasdaq Composite

- Overlap window: 2016-07-15 to 2026-07-06
- Overlap observations: 2458
- Level correlation: 0.0370
- Same-day return correlation: 0.0215
- Next-day return correlation: -0.0572

### Dow Jones Industrial Average

- Overlap window: 2016-07-15 to 2026-07-06
- Overlap observations: 2458
- Level correlation: 0.1144
- Same-day return correlation: 0.0065
- Next-day return correlation: -0.0479

### VIX

- Overlap window: 2016-07-15 to 2026-07-06
- Overlap observations: 2458
- Level correlation: -0.0303
- Same-day return correlation: 0.0382
- Next-day return correlation: -0.0002

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
