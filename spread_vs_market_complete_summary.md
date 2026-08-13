# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-15 to 2026-08-11
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-15 to 2026-08-11
- Overlap observations: 2463
- Level correlation: 0.0634
- Same-day return correlation: 0.0165
- Next-day return correlation: -0.0549

### Nasdaq Composite

- Overlap window: 2016-08-15 to 2026-08-11
- Overlap observations: 2463
- Level correlation: 0.0325
- Same-day return correlation: 0.0204
- Next-day return correlation: -0.0549

### Dow Jones Industrial Average

- Overlap window: 2016-08-15 to 2026-08-11
- Overlap observations: 2463
- Level correlation: 0.1059
- Same-day return correlation: 0.0038
- Next-day return correlation: -0.0454

### VIX

- Overlap window: 2016-08-15 to 2026-08-11
- Overlap observations: 2463
- Level correlation: -0.0407
- Same-day return correlation: 0.0385
- Next-day return correlation: -0.0048

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
