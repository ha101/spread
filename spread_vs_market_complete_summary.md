# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-29 to 2026-07-20
- Spread observations: 2458

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-29 to 2026-07-20
- Overlap observations: 2458
- Level correlation: 0.0534
- Same-day return correlation: 0.0177
- Next-day return correlation: -0.0572

### Nasdaq Composite

- Overlap window: 2016-07-29 to 2026-07-20
- Overlap observations: 2458
- Level correlation: 0.0223
- Same-day return correlation: 0.0217
- Next-day return correlation: -0.0567

### Dow Jones Industrial Average

- Overlap window: 2016-07-29 to 2026-07-20
- Overlap observations: 2458
- Level correlation: 0.0984
- Same-day return correlation: 0.0059
- Next-day return correlation: -0.0479

### VIX

- Overlap window: 2016-07-29 to 2026-07-20
- Overlap observations: 2458
- Level correlation: -0.0334
- Same-day return correlation: 0.0382
- Next-day return correlation: -0.0005

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
