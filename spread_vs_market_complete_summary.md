# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-06-24 to 2026-06-22
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-24 to 2026-06-22
- Overlap observations: 2463
- Level correlation: 0.0928
- Same-day return correlation: 0.0184
- Next-day return correlation: -0.0570

### Nasdaq Composite

- Overlap window: 2016-06-24 to 2026-06-22
- Overlap observations: 2463
- Level correlation: 0.0624
- Same-day return correlation: 0.0224
- Next-day return correlation: -0.0568

### Dow Jones Industrial Average

- Overlap window: 2016-06-24 to 2026-06-22
- Overlap observations: 2463
- Level correlation: 0.1416
- Same-day return correlation: 0.0065
- Next-day return correlation: -0.0476

### VIX

- Overlap window: 2016-06-24 to 2026-06-22
- Overlap observations: 2463
- Level correlation: -0.0282
- Same-day return correlation: 0.0380
- Next-day return correlation: -0.0000

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
