# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-22 to 2026-08-18
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-22 to 2026-08-18
- Overlap observations: 2463
- Level correlation: 0.0661
- Same-day return correlation: 0.0165
- Next-day return correlation: -0.0548

### Nasdaq Composite

- Overlap window: 2016-08-22 to 2026-08-18
- Overlap observations: 2463
- Level correlation: 0.0353
- Same-day return correlation: 0.0202
- Next-day return correlation: -0.0546

### Dow Jones Industrial Average

- Overlap window: 2016-08-22 to 2026-08-18
- Overlap observations: 2463
- Level correlation: 0.1078
- Same-day return correlation: 0.0039
- Next-day return correlation: -0.0453

### VIX

- Overlap window: 2016-08-22 to 2026-08-18
- Overlap observations: 2463
- Level correlation: -0.0437
- Same-day return correlation: 0.0385
- Next-day return correlation: -0.0051

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
