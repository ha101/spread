# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-23 to 2026-05-18
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-23 to 2026-05-18
- Overlap observations: 2463
- Level correlation: 0.1294
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0566

### Nasdaq Composite

- Overlap window: 2016-05-23 to 2026-05-18
- Overlap observations: 2463
- Level correlation: 0.1003
- Same-day return correlation: 0.0223
- Next-day return correlation: -0.0564

### Dow Jones Industrial Average

- Overlap window: 2016-05-23 to 2026-05-18
- Overlap observations: 2463
- Level correlation: 0.1808
- Same-day return correlation: 0.0055
- Next-day return correlation: -0.0474

### VIX

- Overlap window: 2016-05-23 to 2026-05-18
- Overlap observations: 2463
- Level correlation: -0.0250
- Same-day return correlation: 0.0376
- Next-day return correlation: -0.0003

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
