# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-06-27 to 2026-06-22
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-27 to 2026-06-22
- Overlap observations: 2462
- Level correlation: 0.0921
- Same-day return correlation: 0.0182
- Next-day return correlation: -0.0568

### Nasdaq Composite

- Overlap window: 2016-06-27 to 2026-06-22
- Overlap observations: 2462
- Level correlation: 0.0617
- Same-day return correlation: 0.0221
- Next-day return correlation: -0.0566

### Dow Jones Industrial Average

- Overlap window: 2016-06-27 to 2026-06-22
- Overlap observations: 2462
- Level correlation: 0.1408
- Same-day return correlation: 0.0063
- Next-day return correlation: -0.0474

### VIX

- Overlap window: 2016-06-27 to 2026-06-22
- Overlap observations: 2462
- Level correlation: -0.0276
- Same-day return correlation: 0.0378
- Next-day return correlation: -0.0004

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
