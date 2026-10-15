# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-17 to 2026-10-06
- Spread observations: 2457

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-17 to 2026-10-06
- Overlap observations: 2457
- Level correlation: 0.1366
- Same-day return correlation: 0.0182
- Next-day return correlation: -0.0517

### Nasdaq Composite

- Overlap window: 2016-10-17 to 2026-10-06
- Overlap observations: 2457
- Level correlation: 0.1128
- Same-day return correlation: 0.0219
- Next-day return correlation: -0.0512

### Dow Jones Industrial Average

- Overlap window: 2016-10-17 to 2026-10-06
- Overlap observations: 2457
- Level correlation: 0.1609
- Same-day return correlation: 0.0067
- Next-day return correlation: -0.0438

### VIX

- Overlap window: 2016-10-17 to 2026-10-06
- Overlap observations: 2457
- Level correlation: -0.0654
- Same-day return correlation: 0.0327
- Next-day return correlation: -0.0025

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
