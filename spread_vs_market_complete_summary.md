# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-22 to 2026-07-13
- Spread observations: 2458

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-22 to 2026-07-13
- Overlap observations: 2458
- Level correlation: 0.0601
- Same-day return correlation: 0.0176
- Next-day return correlation: -0.0576

### Nasdaq Composite

- Overlap window: 2016-07-22 to 2026-07-13
- Overlap observations: 2458
- Level correlation: 0.0289
- Same-day return correlation: 0.0214
- Next-day return correlation: -0.0574

### Dow Jones Industrial Average

- Overlap window: 2016-07-22 to 2026-07-13
- Overlap observations: 2458
- Level correlation: 0.1057
- Same-day return correlation: 0.0061
- Next-day return correlation: -0.0481

### VIX

- Overlap window: 2016-07-22 to 2026-07-13
- Overlap observations: 2458
- Level correlation: -0.0318
- Same-day return correlation: 0.0386
- Next-day return correlation: 0.0001

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
