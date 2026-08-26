# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-26 to 2026-08-25
- Spread observations: 2464

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-26 to 2026-08-25
- Overlap observations: 2464
- Level correlation: 0.0659
- Same-day return correlation: 0.0170
- Next-day return correlation: -0.0544

### Nasdaq Composite

- Overlap window: 2016-08-26 to 2026-08-25
- Overlap observations: 2464
- Level correlation: 0.0352
- Same-day return correlation: 0.0208
- Next-day return correlation: -0.0549

### Dow Jones Industrial Average

- Overlap window: 2016-08-26 to 2026-08-25
- Overlap observations: 2464
- Level correlation: 0.1071
- Same-day return correlation: 0.0048
- Next-day return correlation: -0.0441

### VIX

- Overlap window: 2016-08-26 to 2026-08-25
- Overlap observations: 2464
- Level correlation: -0.0453
- Same-day return correlation: 0.0377
- Next-day return correlation: -0.0052

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
