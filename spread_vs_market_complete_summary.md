# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-13 to 2026-10-06
- Spread observations: 2459

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-13 to 2026-10-06
- Overlap observations: 2459
- Level correlation: 0.1382
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0515

### Nasdaq Composite

- Overlap window: 2016-10-13 to 2026-10-06
- Overlap observations: 2459
- Level correlation: 0.1144
- Same-day return correlation: 0.0219
- Next-day return correlation: -0.0511

### Dow Jones Industrial Average

- Overlap window: 2016-10-13 to 2026-10-06
- Overlap observations: 2459
- Level correlation: 0.1628
- Same-day return correlation: 0.0067
- Next-day return correlation: -0.0437

### VIX

- Overlap window: 2016-10-13 to 2026-10-06
- Overlap observations: 2459
- Level correlation: -0.0649
- Same-day return correlation: 0.0328
- Next-day return correlation: -0.0026

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
