# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-11-14 to 2026-11-11
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-14 to 2026-11-11
- Overlap observations: 2463
- Level correlation: 0.1743
- Same-day return correlation: 0.0124
- Next-day return correlation: -0.0438

### Nasdaq Composite

- Overlap window: 2016-11-14 to 2026-11-11
- Overlap observations: 2463
- Level correlation: 0.1542
- Same-day return correlation: 0.0172
- Next-day return correlation: -0.0418

### Dow Jones Industrial Average

- Overlap window: 2016-11-14 to 2026-11-11
- Overlap observations: 2463
- Level correlation: 0.1876
- Same-day return correlation: -0.0008
- Next-day return correlation: -0.0385

### VIX

- Overlap window: 2016-11-14 to 2026-11-11
- Overlap observations: 2463
- Level correlation: -0.0724
- Same-day return correlation: 0.0398
- Next-day return correlation: -0.0147

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
