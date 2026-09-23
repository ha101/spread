# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-23 to 2026-09-22
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-23 to 2026-09-22
- Overlap observations: 2463
- Level correlation: 0.1003
- Same-day return correlation: 0.0159
- Next-day return correlation: -0.0543

### Nasdaq Composite

- Overlap window: 2016-09-23 to 2026-09-22
- Overlap observations: 2463
- Level correlation: 0.0718
- Same-day return correlation: 0.0195
- Next-day return correlation: -0.0545

### Dow Jones Industrial Average

- Overlap window: 2016-09-23 to 2026-09-22
- Overlap observations: 2463
- Level correlation: 0.1352
- Same-day return correlation: 0.0036
- Next-day return correlation: -0.0447

### VIX

- Overlap window: 2016-09-23 to 2026-09-22
- Overlap observations: 2463
- Level correlation: -0.0541
- Same-day return correlation: 0.0397
- Next-day return correlation: -0.0063

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
