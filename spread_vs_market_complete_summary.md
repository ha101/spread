# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-24 to 2026-10-20
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-24 to 2026-10-20
- Overlap observations: 2462
- Level correlation: 0.1713
- Same-day return correlation: 0.0192
- Next-day return correlation: -0.0492

### Nasdaq Composite

- Overlap window: 2016-10-24 to 2026-10-20
- Overlap observations: 2462
- Level correlation: 0.1507
- Same-day return correlation: 0.0243
- Next-day return correlation: -0.0483

### Dow Jones Industrial Average

- Overlap window: 2016-10-24 to 2026-10-20
- Overlap observations: 2462
- Level correlation: 0.1881
- Same-day return correlation: 0.0058
- Next-day return correlation: -0.0429

### VIX

- Overlap window: 2016-10-24 to 2026-10-20
- Overlap observations: 2462
- Level correlation: -0.0705
- Same-day return correlation: 0.0286
- Next-day return correlation: -0.0054

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
