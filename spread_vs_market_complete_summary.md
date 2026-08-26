# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-29 to 2026-08-25
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-29 to 2026-08-25
- Overlap observations: 2463
- Level correlation: 0.0656
- Same-day return correlation: 0.0170
- Next-day return correlation: -0.0544

### Nasdaq Composite

- Overlap window: 2016-08-29 to 2026-08-25
- Overlap observations: 2463
- Level correlation: 0.0348
- Same-day return correlation: 0.0208
- Next-day return correlation: -0.0548

### Dow Jones Industrial Average

- Overlap window: 2016-08-29 to 2026-08-25
- Overlap observations: 2463
- Level correlation: 0.1067
- Same-day return correlation: 0.0047
- Next-day return correlation: -0.0440

### VIX

- Overlap window: 2016-08-29 to 2026-08-25
- Overlap observations: 2463
- Level correlation: -0.0455
- Same-day return correlation: 0.0378
- Next-day return correlation: -0.0052

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
