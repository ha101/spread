# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-13 to 2026-05-01
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-13 to 2026-05-01
- Overlap observations: 2459
- Level correlation: 0.1320
- Same-day return correlation: 0.0192
- Next-day return correlation: -0.0562

### Nasdaq Composite

- Overlap window: 2016-05-13 to 2026-05-01
- Overlap observations: 2459
- Level correlation: 0.1026
- Same-day return correlation: 0.0240
- Next-day return correlation: -0.0558

### Dow Jones Industrial Average

- Overlap window: 2016-05-13 to 2026-05-01
- Overlap observations: 2459
- Level correlation: 0.1844
- Same-day return correlation: 0.0060
- Next-day return correlation: -0.0476

### VIX

- Overlap window: 2016-05-13 to 2026-05-01
- Overlap observations: 2459
- Level correlation: -0.0235
- Same-day return correlation: 0.0374
- Next-day return correlation: 0.0001

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
