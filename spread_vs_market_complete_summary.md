# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-04-07 to 2026-03-30
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-07 to 2026-03-30
- Overlap observations: 2463
- Level correlation: 0.0743
- Same-day return correlation: 0.0154
- Next-day return correlation: -0.0607

### Nasdaq Composite

- Overlap window: 2016-04-07 to 2026-03-30
- Overlap observations: 2463
- Level correlation: 0.0410
- Same-day return correlation: 0.0205
- Next-day return correlation: -0.0594

### Dow Jones Industrial Average

- Overlap window: 2016-04-07 to 2026-03-30
- Overlap observations: 2463
- Level correlation: 0.1409
- Same-day return correlation: 0.0026
- Next-day return correlation: -0.0526

### VIX

- Overlap window: 2016-04-07 to 2026-03-30
- Overlap observations: 2463
- Level correlation: -0.0268
- Same-day return correlation: 0.0393
- Next-day return correlation: 0.0042

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
