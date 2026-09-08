# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-09 to 2026-09-01
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-09 to 2026-09-01
- Overlap observations: 2459
- Level correlation: 0.0624
- Same-day return correlation: 0.0178
- Next-day return correlation: -0.0545

### Nasdaq Composite

- Overlap window: 2016-09-09 to 2026-09-01
- Overlap observations: 2459
- Level correlation: 0.0316
- Same-day return correlation: 0.0216
- Next-day return correlation: -0.0551

### Dow Jones Industrial Average

- Overlap window: 2016-09-09 to 2026-09-01
- Overlap observations: 2459
- Level correlation: 0.1028
- Same-day return correlation: 0.0054
- Next-day return correlation: -0.0441

### VIX

- Overlap window: 2016-09-09 to 2026-09-01
- Overlap observations: 2459
- Level correlation: -0.0479
- Same-day return correlation: 0.0366
- Next-day return correlation: -0.0054

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
