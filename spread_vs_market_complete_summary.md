# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-12 to 2026-05-01
- Spread observations: 2460

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-12 to 2026-05-01
- Overlap observations: 2460
- Level correlation: 0.1327
- Same-day return correlation: 0.0190
- Next-day return correlation: -0.0561

### Nasdaq Composite

- Overlap window: 2016-05-12 to 2026-05-01
- Overlap observations: 2460
- Level correlation: 0.1034
- Same-day return correlation: 0.0240
- Next-day return correlation: -0.0556

### Dow Jones Industrial Average

- Overlap window: 2016-05-12 to 2026-05-01
- Overlap observations: 2460
- Level correlation: 0.1851
- Same-day return correlation: 0.0058
- Next-day return correlation: -0.0474

### VIX

- Overlap window: 2016-05-12 to 2026-05-01
- Overlap observations: 2460
- Level correlation: -0.0232
- Same-day return correlation: 0.0375
- Next-day return correlation: -0.0000

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
