# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-12 to 2026-09-09
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-12 to 2026-09-09
- Overlap observations: 2463
- Level correlation: 0.0689
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0553

### Nasdaq Composite

- Overlap window: 2016-09-12 to 2026-09-09
- Overlap observations: 2463
- Level correlation: 0.0385
- Same-day return correlation: 0.0222
- Next-day return correlation: -0.0555

### Dow Jones Industrial Average

- Overlap window: 2016-09-12 to 2026-09-09
- Overlap observations: 2463
- Level correlation: 0.1087
- Same-day return correlation: 0.0055
- Next-day return correlation: -0.0452

### VIX

- Overlap window: 2016-09-12 to 2026-09-09
- Overlap observations: 2463
- Level correlation: -0.0491
- Same-day return correlation: 0.0363
- Next-day return correlation: -0.0043

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
