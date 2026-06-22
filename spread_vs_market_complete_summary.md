# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-06-23 to 2026-06-15
- Spread observations: 2460

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-23 to 2026-06-15
- Overlap observations: 2460
- Level correlation: 0.1009
- Same-day return correlation: 0.0178
- Next-day return correlation: -0.0569

### Nasdaq Composite

- Overlap window: 2016-06-23 to 2026-06-15
- Overlap observations: 2460
- Level correlation: 0.0707
- Same-day return correlation: 0.0218
- Next-day return correlation: -0.0568

### Dow Jones Industrial Average

- Overlap window: 2016-06-23 to 2026-06-15
- Overlap observations: 2460
- Level correlation: 0.1499
- Same-day return correlation: 0.0058
- Next-day return correlation: -0.0475

### VIX

- Overlap window: 2016-06-23 to 2026-06-15
- Overlap observations: 2460
- Level correlation: -0.0286
- Same-day return correlation: 0.0389
- Next-day return correlation: -0.0007

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
