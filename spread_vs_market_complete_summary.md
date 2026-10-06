# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-07 to 2026-09-29
- Spread observations: 2458

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-07 to 2026-09-29
- Overlap observations: 2458
- Level correlation: 0.1171
- Same-day return correlation: 0.0176
- Next-day return correlation: -0.0549

### Nasdaq Composite

- Overlap window: 2016-10-07 to 2026-09-29
- Overlap observations: 2458
- Level correlation: 0.0906
- Same-day return correlation: 0.0206
- Next-day return correlation: -0.0550

### Dow Jones Industrial Average

- Overlap window: 2016-10-07 to 2026-09-29
- Overlap observations: 2458
- Level correlation: 0.1469
- Same-day return correlation: 0.0059
- Next-day return correlation: -0.0454

### VIX

- Overlap window: 2016-10-07 to 2026-09-29
- Overlap observations: 2458
- Level correlation: -0.0612
- Same-day return correlation: 0.0369
- Next-day return correlation: -0.0043

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
