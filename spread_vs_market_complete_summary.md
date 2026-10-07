# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-07 to 2026-10-06
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-07 to 2026-10-06
- Overlap observations: 2463
- Level correlation: 0.1405
- Same-day return correlation: 0.0187
- Next-day return correlation: -0.0518

### Nasdaq Composite

- Overlap window: 2016-10-07 to 2026-10-06
- Overlap observations: 2463
- Level correlation: 0.1168
- Same-day return correlation: 0.0225
- Next-day return correlation: -0.0512

### Dow Jones Industrial Average

- Overlap window: 2016-10-07 to 2026-10-06
- Overlap observations: 2463
- Level correlation: 0.1655
- Same-day return correlation: 0.0072
- Next-day return correlation: -0.0440

### VIX

- Overlap window: 2016-10-07 to 2026-10-06
- Overlap observations: 2463
- Level correlation: -0.0637
- Same-day return correlation: 0.0319
- Next-day return correlation: -0.0024

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
