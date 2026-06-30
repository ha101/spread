# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-06-30 to 2026-06-22
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-30 to 2026-06-22
- Overlap observations: 2459
- Level correlation: 0.0893
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0567

### Nasdaq Composite

- Overlap window: 2016-06-30 to 2026-06-22
- Overlap observations: 2459
- Level correlation: 0.0587
- Same-day return correlation: 0.0221
- Next-day return correlation: -0.0565

### Dow Jones Industrial Average

- Overlap window: 2016-06-30 to 2026-06-22
- Overlap observations: 2459
- Level correlation: 0.1376
- Same-day return correlation: 0.0062
- Next-day return correlation: -0.0472

### VIX

- Overlap window: 2016-06-30 to 2026-06-22
- Overlap observations: 2459
- Level correlation: -0.0274
- Same-day return correlation: 0.0377
- Next-day return correlation: -0.0005

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
