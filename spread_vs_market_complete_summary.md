# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-20 to 2026-10-14
- Spread observations: 2460

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-20 to 2026-10-14
- Overlap observations: 2460
- Level correlation: 0.1645
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0502

### Nasdaq Composite

- Overlap window: 2016-10-20 to 2026-10-14
- Overlap observations: 2460
- Level correlation: 0.1434
- Same-day return correlation: 0.0218
- Next-day return correlation: -0.0494

### Dow Jones Industrial Average

- Overlap window: 2016-10-20 to 2026-10-14
- Overlap observations: 2460
- Level correlation: 0.1827
- Same-day return correlation: 0.0068
- Next-day return correlation: -0.0434

### VIX

- Overlap window: 2016-10-20 to 2026-10-14
- Overlap observations: 2460
- Level correlation: -0.0697
- Same-day return correlation: 0.0328
- Next-day return correlation: -0.0040

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
