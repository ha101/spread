# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-03 to 2026-09-29
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-03 to 2026-09-29
- Overlap observations: 2462
- Level correlation: 0.1198
- Same-day return correlation: 0.0174
- Next-day return correlation: -0.0548

### Nasdaq Composite

- Overlap window: 2016-10-03 to 2026-09-29
- Overlap observations: 2462
- Level correlation: 0.0934
- Same-day return correlation: 0.0205
- Next-day return correlation: -0.0549

### Dow Jones Industrial Average

- Overlap window: 2016-10-03 to 2026-09-29
- Overlap observations: 2462
- Level correlation: 0.1501
- Same-day return correlation: 0.0058
- Next-day return correlation: -0.0453

### VIX

- Overlap window: 2016-10-03 to 2026-09-29
- Overlap observations: 2462
- Level correlation: -0.0594
- Same-day return correlation: 0.0371
- Next-day return correlation: -0.0044

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
