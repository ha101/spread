# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-07-18 to 2026-07-13
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-18 to 2026-07-13
- Overlap observations: 2462
- Level correlation: 0.0624
- Same-day return correlation: 0.0175
- Next-day return correlation: -0.0575

### Nasdaq Composite

- Overlap window: 2016-07-18 to 2026-07-13
- Overlap observations: 2462
- Level correlation: 0.0314
- Same-day return correlation: 0.0213
- Next-day return correlation: -0.0572

### Dow Jones Industrial Average

- Overlap window: 2016-07-18 to 2026-07-13
- Overlap observations: 2462
- Level correlation: 0.1083
- Same-day return correlation: 0.0060
- Next-day return correlation: -0.0480

### VIX

- Overlap window: 2016-07-18 to 2026-07-13
- Overlap observations: 2462
- Level correlation: -0.0301
- Same-day return correlation: 0.0386
- Next-day return correlation: -0.0001

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
