# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-17 to 2026-10-14
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-17 to 2026-10-14
- Overlap observations: 2463
- Level correlation: 0.1664
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0503

### Nasdaq Composite

- Overlap window: 2016-10-17 to 2026-10-14
- Overlap observations: 2463
- Level correlation: 0.1453
- Same-day return correlation: 0.0218
- Next-day return correlation: -0.0495

### Dow Jones Industrial Average

- Overlap window: 2016-10-17 to 2026-10-14
- Overlap observations: 2463
- Level correlation: 0.1850
- Same-day return correlation: 0.0069
- Next-day return correlation: -0.0434

### VIX

- Overlap window: 2016-10-17 to 2026-10-14
- Overlap observations: 2463
- Level correlation: -0.0689
- Same-day return correlation: 0.0327
- Next-day return correlation: -0.0041

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
