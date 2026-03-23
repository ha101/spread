# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-03-21 to 2026-03-20
- Spread observations: 2469

## Correlations By Series

### S&P 500

- Overlap window: 2016-03-21 to 2026-03-20
- Overlap observations: 2469
- Level correlation: 0.0581
- Same-day return correlation: 0.0184
- Next-day return correlation: -0.0623

### Nasdaq Composite

- Overlap window: 2016-03-21 to 2026-03-20
- Overlap observations: 2469
- Level correlation: 0.0244
- Same-day return correlation: 0.0230
- Next-day return correlation: -0.0614

### Dow Jones Industrial Average

- Overlap window: 2016-03-21 to 2026-03-20
- Overlap observations: 2469
- Level correlation: 0.1303
- Same-day return correlation: 0.0060
- Next-day return correlation: -0.0537

### VIX

- Overlap window: 2016-03-21 to 2026-03-20
- Overlap observations: 2469
- Level correlation: -0.0408
- Same-day return correlation: 0.0368
- Next-day return correlation: 0.0054

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
