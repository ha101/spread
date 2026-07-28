# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-28 to 2026-07-20
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-28 to 2026-07-20
- Overlap observations: 2459
- Level correlation: 0.0540
- Same-day return correlation: 0.0176
- Next-day return correlation: -0.0572

### Nasdaq Composite

- Overlap window: 2016-07-28 to 2026-07-20
- Overlap observations: 2459
- Level correlation: 0.0229
- Same-day return correlation: 0.0217
- Next-day return correlation: -0.0567

### Dow Jones Industrial Average

- Overlap window: 2016-07-28 to 2026-07-20
- Overlap observations: 2459
- Level correlation: 0.0991
- Same-day return correlation: 0.0059
- Next-day return correlation: -0.0479

### VIX

- Overlap window: 2016-07-28 to 2026-07-20
- Overlap observations: 2459
- Level correlation: -0.0330
- Same-day return correlation: 0.0384
- Next-day return correlation: -0.0006

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
