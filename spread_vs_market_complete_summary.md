# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-08-12 to 2026-08-11
- Spread observations: 2464

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-12 to 2026-08-11
- Overlap observations: 2464
- Level correlation: 0.0640
- Same-day return correlation: 0.0165
- Next-day return correlation: -0.0550

### Nasdaq Composite

- Overlap window: 2016-08-12 to 2026-08-11
- Overlap observations: 2464
- Level correlation: 0.0331
- Same-day return correlation: 0.0205
- Next-day return correlation: -0.0550

### Dow Jones Industrial Average

- Overlap window: 2016-08-12 to 2026-08-11
- Overlap observations: 2464
- Level correlation: 0.1066
- Same-day return correlation: 0.0038
- Next-day return correlation: -0.0455

### VIX

- Overlap window: 2016-08-12 to 2026-08-11
- Overlap observations: 2464
- Level correlation: -0.0402
- Same-day return correlation: 0.0385
- Next-day return correlation: -0.0046

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
