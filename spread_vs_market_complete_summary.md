# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-14 to 2026-10-06
- Spread observations: 2458

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-14 to 2026-10-06
- Overlap observations: 2458
- Level correlation: 0.1374
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0516

### Nasdaq Composite

- Overlap window: 2016-10-14 to 2026-10-06
- Overlap observations: 2458
- Level correlation: 0.1136
- Same-day return correlation: 0.0219
- Next-day return correlation: -0.0511

### Dow Jones Industrial Average

- Overlap window: 2016-10-14 to 2026-10-06
- Overlap observations: 2458
- Level correlation: 0.1619
- Same-day return correlation: 0.0067
- Next-day return correlation: -0.0438

### VIX

- Overlap window: 2016-10-14 to 2026-10-06
- Overlap observations: 2458
- Level correlation: -0.0651
- Same-day return correlation: 0.0327
- Next-day return correlation: -0.0026

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
