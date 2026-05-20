# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-20 to 2026-05-18
- Spread observations: 2464

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-20 to 2026-05-18
- Overlap observations: 2464
- Level correlation: 0.1300
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0569

### Nasdaq Composite

- Overlap window: 2016-05-20 to 2026-05-18
- Overlap observations: 2464
- Level correlation: 0.1008
- Same-day return correlation: 0.0224
- Next-day return correlation: -0.0567

### Dow Jones Industrial Average

- Overlap window: 2016-05-20 to 2026-05-18
- Overlap observations: 2464
- Level correlation: 0.1814
- Same-day return correlation: 0.0055
- Next-day return correlation: -0.0476

### VIX

- Overlap window: 2016-05-20 to 2026-05-18
- Overlap observations: 2464
- Level correlation: -0.0247
- Same-day return correlation: 0.0375
- Next-day return correlation: -0.0000

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
