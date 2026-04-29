# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-29 to 2026-04-20
- Spread observations: 2460

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-29 to 2026-04-20
- Overlap observations: 2460
- Level correlation: 0.1156
- Same-day return correlation: 0.0179
- Next-day return correlation: -0.0553

### Nasdaq Composite

- Overlap window: 2016-04-29 to 2026-04-20
- Overlap observations: 2460
- Level correlation: 0.0848
- Same-day return correlation: 0.0225
- Next-day return correlation: -0.0541

### Dow Jones Industrial Average

- Overlap window: 2016-04-29 to 2026-04-20
- Overlap observations: 2460
- Level correlation: 0.1724
- Same-day return correlation: 0.0043
- Next-day return correlation: -0.0473

### VIX

- Overlap window: 2016-04-29 to 2026-04-20
- Overlap observations: 2460
- Level correlation: -0.0207
- Same-day return correlation: 0.0385
- Next-day return correlation: -0.0007

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
