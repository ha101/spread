# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-15 to 2026-09-09
- Spread observations: 2460

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-15 to 2026-09-09
- Overlap observations: 2460
- Level correlation: 0.0676
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0554

### Nasdaq Composite

- Overlap window: 2016-09-15 to 2026-09-09
- Overlap observations: 2460
- Level correlation: 0.0371
- Same-day return correlation: 0.0222
- Next-day return correlation: -0.0556

### Dow Jones Industrial Average

- Overlap window: 2016-09-15 to 2026-09-09
- Overlap observations: 2460
- Level correlation: 0.1072
- Same-day return correlation: 0.0055
- Next-day return correlation: -0.0453

### VIX

- Overlap window: 2016-09-15 to 2026-09-09
- Overlap observations: 2460
- Level correlation: -0.0494
- Same-day return correlation: 0.0363
- Next-day return correlation: -0.0042

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
