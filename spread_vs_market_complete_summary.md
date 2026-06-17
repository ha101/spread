# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-06-17 to 2026-06-08
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-17 to 2026-06-08
- Overlap observations: 2459
- Level correlation: 0.1103
- Same-day return correlation: 0.0183
- Next-day return correlation: -0.0564

### Nasdaq Composite

- Overlap window: 2016-06-17 to 2026-06-08
- Overlap observations: 2459
- Level correlation: 0.0805
- Same-day return correlation: 0.0223
- Next-day return correlation: -0.0563

### Dow Jones Industrial Average

- Overlap window: 2016-06-17 to 2026-06-08
- Overlap observations: 2459
- Level correlation: 0.1598
- Same-day return correlation: 0.0063
- Next-day return correlation: -0.0471

### VIX

- Overlap window: 2016-06-17 to 2026-06-08
- Overlap observations: 2459
- Level correlation: -0.0289
- Same-day return correlation: 0.0382
- Next-day return correlation: -0.0011

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
