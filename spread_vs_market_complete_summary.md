# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-13 to 2026-05-11
- Spread observations: 2464

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-13 to 2026-05-11
- Overlap observations: 2464
- Level correlation: 0.1324
- Same-day return correlation: 0.0182
- Next-day return correlation: -0.0572

### Nasdaq Composite

- Overlap window: 2016-05-13 to 2026-05-11
- Overlap observations: 2464
- Level correlation: 0.1032
- Same-day return correlation: 0.0227
- Next-day return correlation: -0.0574

### Dow Jones Industrial Average

- Overlap window: 2016-05-13 to 2026-05-11
- Overlap observations: 2464
- Level correlation: 0.1845
- Same-day return correlation: 0.0056
- Next-day return correlation: -0.0476

### VIX

- Overlap window: 2016-05-13 to 2026-05-11
- Overlap observations: 2464
- Level correlation: -0.0236
- Same-day return correlation: 0.0372
- Next-day return correlation: 0.0004

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
