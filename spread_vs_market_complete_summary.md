# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-11-28 to 2026-11-24
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-28 to 2026-11-24
- Overlap observations: 2463
- Level correlation: 0.1681
- Same-day return correlation: 0.0172
- Next-day return correlation: -0.0494

### Nasdaq Composite

- Overlap window: 2016-11-28 to 2026-11-24
- Overlap observations: 2463
- Level correlation: 0.1480
- Same-day return correlation: 0.0230
- Next-day return correlation: -0.0483

### Dow Jones Industrial Average

- Overlap window: 2016-11-28 to 2026-11-24
- Overlap observations: 2463
- Level correlation: 0.1801
- Same-day return correlation: 0.0013
- Next-day return correlation: -0.0415

### VIX

- Overlap window: 2016-11-28 to 2026-11-24
- Overlap observations: 2463
- Level correlation: -0.0755
- Same-day return correlation: 0.0353
- Next-day return correlation: -0.0099

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
