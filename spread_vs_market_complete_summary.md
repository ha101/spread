# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-03-28 to 2026-03-23
- Spread observations: 2466

## Correlations By Series

### S&P 500

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: 0.0636
- Same-day return correlation: 0.0157
- Next-day return correlation: -0.0605

### Nasdaq Composite

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: 0.0302
- Same-day return correlation: 0.0206
- Next-day return correlation: -0.0593

### Dow Jones Industrial Average

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: 0.1336
- Same-day return correlation: 0.0034
- Next-day return correlation: -0.0528

### VIX

- Overlap window: 2016-03-28 to 2026-03-23
- Overlap observations: 2466
- Level correlation: -0.0373
- Same-day return correlation: 0.0388
- Next-day return correlation: 0.0046

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
