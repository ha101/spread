# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2025-11-17 to 2026-11-11
- Spread observations: 244

## Correlations By Series

### S&P 500

- Overlap window: 2025-11-17 to 2026-11-11
- Overlap observations: 244
- Level correlation: 0.1286
- Same-day return correlation: -0.0673
- Next-day return correlation: 0.1004

### Nasdaq Composite

- Overlap window: 2025-11-17 to 2026-11-11
- Overlap observations: 244
- Level correlation: 0.1133
- Same-day return correlation: -0.0444
- Next-day return correlation: 0.0843

### Dow Jones Industrial Average

- Overlap window: 2025-11-17 to 2026-11-11
- Overlap observations: 244
- Level correlation: -0.0455
- Same-day return correlation: -0.0888
- Next-day return correlation: 0.0880

### VIX

- Overlap window: 2025-11-17 to 2026-11-11
- Overlap observations: 244
- Level correlation: 0.0475
- Same-day return correlation: 0.0902
- Next-day return correlation: -0.1347

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
