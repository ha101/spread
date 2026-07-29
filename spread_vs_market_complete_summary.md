# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-29 to 2026-07-27
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-29 to 2026-07-27
- Overlap observations: 2463
- Level correlation: 0.0591
- Same-day return correlation: 0.0171
- Next-day return correlation: -0.0566

### Nasdaq Composite

- Overlap window: 2016-07-29 to 2026-07-27
- Overlap observations: 2463
- Level correlation: 0.0281
- Same-day return correlation: 0.0211
- Next-day return correlation: -0.0567

### Dow Jones Industrial Average

- Overlap window: 2016-07-29 to 2026-07-27
- Overlap observations: 2463
- Level correlation: 0.1036
- Same-day return correlation: 0.0050
- Next-day return correlation: -0.0472

### VIX

- Overlap window: 2016-07-29 to 2026-07-27
- Overlap observations: 2463
- Level correlation: -0.0334
- Same-day return correlation: 0.0387
- Next-day return correlation: -0.0016

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
