# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-05 to 2026-06-29
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-05 to 2026-06-29
- Overlap observations: 2462
- Level correlation: 0.0809
- Same-day return correlation: 0.0172
- Next-day return correlation: -0.0567

### Nasdaq Composite

- Overlap window: 2016-07-05 to 2026-06-29
- Overlap observations: 2462
- Level correlation: 0.0503
- Same-day return correlation: 0.0210
- Next-day return correlation: -0.0567

### Dow Jones Industrial Average

- Overlap window: 2016-07-05 to 2026-06-29
- Overlap observations: 2462
- Level correlation: 0.1286
- Same-day return correlation: 0.0062
- Next-day return correlation: -0.0472

### VIX

- Overlap window: 2016-07-05 to 2026-06-29
- Overlap observations: 2462
- Level correlation: -0.0280
- Same-day return correlation: 0.0387
- Next-day return correlation: -0.0011

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
