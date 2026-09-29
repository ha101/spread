# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-30 to 2026-09-22
- Spread observations: 2458

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-30 to 2026-09-22
- Overlap observations: 2458
- Level correlation: 0.0973
- Same-day return correlation: 0.0163
- Next-day return correlation: -0.0549

### Nasdaq Composite

- Overlap window: 2016-09-30 to 2026-09-22
- Overlap observations: 2458
- Level correlation: 0.0688
- Same-day return correlation: 0.0198
- Next-day return correlation: -0.0549

### Dow Jones Industrial Average

- Overlap window: 2016-09-30 to 2026-09-22
- Overlap observations: 2458
- Level correlation: 0.1316
- Same-day return correlation: 0.0042
- Next-day return correlation: -0.0453

### VIX

- Overlap window: 2016-09-30 to 2026-09-22
- Overlap observations: 2458
- Level correlation: -0.0560
- Same-day return correlation: 0.0392
- Next-day return correlation: -0.0058

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
