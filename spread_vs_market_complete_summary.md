# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-22 to 2026-09-15
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-22 to 2026-09-15
- Overlap observations: 2459
- Level correlation: 0.0812
- Same-day return correlation: 0.0168
- Next-day return correlation: -0.0543

### Nasdaq Composite

- Overlap window: 2016-09-22 to 2026-09-15
- Overlap observations: 2459
- Level correlation: 0.0514
- Same-day return correlation: 0.0207
- Next-day return correlation: -0.0548

### Dow Jones Industrial Average

- Overlap window: 2016-09-22 to 2026-09-15
- Overlap observations: 2459
- Level correlation: 0.1189
- Same-day return correlation: 0.0041
- Next-day return correlation: -0.0442

### VIX

- Overlap window: 2016-09-22 to 2026-09-15
- Overlap observations: 2459
- Level correlation: -0.0510
- Same-day return correlation: 0.0377
- Next-day return correlation: -0.0065

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
