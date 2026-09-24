# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-26 to 2026-09-22
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-26 to 2026-09-22
- Overlap observations: 2462
- Level correlation: 0.0999
- Same-day return correlation: 0.0156
- Next-day return correlation: -0.0542

### Nasdaq Composite

- Overlap window: 2016-09-26 to 2026-09-22
- Overlap observations: 2462
- Level correlation: 0.0715
- Same-day return correlation: 0.0193
- Next-day return correlation: -0.0543

### Dow Jones Industrial Average

- Overlap window: 2016-09-26 to 2026-09-22
- Overlap observations: 2462
- Level correlation: 0.1348
- Same-day return correlation: 0.0034
- Next-day return correlation: -0.0446

### VIX

- Overlap window: 2016-09-26 to 2026-09-22
- Overlap observations: 2462
- Level correlation: -0.0543
- Same-day return correlation: 0.0403
- Next-day return correlation: -0.0066

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
