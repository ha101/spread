# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-12 to 2026-09-01
- Spread observations: 2458

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-12 to 2026-09-01
- Overlap observations: 2458
- Level correlation: 0.0620
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0548

### Nasdaq Composite

- Overlap window: 2016-09-12 to 2026-09-01
- Overlap observations: 2458
- Level correlation: 0.0313
- Same-day return correlation: 0.0219
- Next-day return correlation: -0.0552

### Dow Jones Industrial Average

- Overlap window: 2016-09-12 to 2026-09-01
- Overlap observations: 2458
- Level correlation: 0.1024
- Same-day return correlation: 0.0056
- Next-day return correlation: -0.0444

### VIX

- Overlap window: 2016-09-12 to 2026-09-01
- Overlap observations: 2458
- Level correlation: -0.0479
- Same-day return correlation: 0.0363
- Next-day return correlation: -0.0050

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
