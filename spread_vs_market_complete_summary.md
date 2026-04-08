# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-08 to 2026-04-07
- Spread observations: 2467

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2467
- Level correlation: 0.0789
- Same-day return correlation: 0.0164
- Next-day return correlation: -0.0602

### Nasdaq Composite

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2467
- Level correlation: 0.0462
- Same-day return correlation: 0.0213
- Next-day return correlation: -0.0588

### Dow Jones Industrial Average

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2467
- Level correlation: 0.1436
- Same-day return correlation: 0.0041
- Next-day return correlation: -0.0512

### VIX

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2467
- Level correlation: -0.0235
- Same-day return correlation: 0.0358
- Next-day return correlation: 0.0022

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
