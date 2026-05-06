# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-06 to 2026-05-01
- Spread observations: 2464

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-06 to 2026-05-01
- Overlap observations: 2464
- Level correlation: 0.1356
- Same-day return correlation: 0.0190
- Next-day return correlation: -0.0563

### Nasdaq Composite

- Overlap window: 2016-05-06 to 2026-05-01
- Overlap observations: 2464
- Level correlation: 0.1064
- Same-day return correlation: 0.0239
- Next-day return correlation: -0.0558

### Dow Jones Industrial Average

- Overlap window: 2016-05-06 to 2026-05-01
- Overlap observations: 2464
- Level correlation: 0.1884
- Same-day return correlation: 0.0058
- Next-day return correlation: -0.0477

### VIX

- Overlap window: 2016-05-06 to 2026-05-01
- Overlap observations: 2464
- Level correlation: -0.0218
- Same-day return correlation: 0.0376
- Next-day return correlation: 0.0002

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
