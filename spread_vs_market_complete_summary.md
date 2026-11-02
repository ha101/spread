# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-11-03 to 2026-10-27
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-03 to 2026-10-27
- Overlap observations: 2459
- Level correlation: 0.1800
- Same-day return correlation: 0.0183
- Next-day return correlation: -0.0510

### Nasdaq Composite

- Overlap window: 2016-11-03 to 2026-10-27
- Overlap observations: 2459
- Level correlation: 0.1596
- Same-day return correlation: 0.0220
- Next-day return correlation: -0.0505

### Dow Jones Industrial Average

- Overlap window: 2016-11-03 to 2026-10-27
- Overlap observations: 2459
- Level correlation: 0.1948
- Same-day return correlation: 0.0071
- Next-day return correlation: -0.0447

### VIX

- Overlap window: 2016-11-03 to 2026-10-27
- Overlap observations: 2459
- Level correlation: -0.0716
- Same-day return correlation: 0.0301
- Next-day return correlation: -0.0031

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
