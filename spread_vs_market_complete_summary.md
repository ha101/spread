# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-27 to 2026-05-18
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-27 to 2026-05-18
- Overlap observations: 2459
- Level correlation: 0.1268
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0568

### Nasdaq Composite

- Overlap window: 2016-05-27 to 2026-05-18
- Overlap observations: 2459
- Level correlation: 0.0975
- Same-day return correlation: 0.0222
- Next-day return correlation: -0.0565

### Dow Jones Industrial Average

- Overlap window: 2016-05-27 to 2026-05-18
- Overlap observations: 2459
- Level correlation: 0.1778
- Same-day return correlation: 0.0055
- Next-day return correlation: -0.0476

### VIX

- Overlap window: 2016-05-27 to 2026-05-18
- Overlap observations: 2459
- Level correlation: -0.0262
- Same-day return correlation: 0.0377
- Next-day return correlation: -0.0001

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
