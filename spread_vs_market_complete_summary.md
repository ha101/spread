# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-11-21 to 2026-11-17
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-21 to 2026-11-17
- Overlap observations: 2462
- Level correlation: 0.1687
- Same-day return correlation: 0.0123
- Next-day return correlation: -0.0441

### Nasdaq Composite

- Overlap window: 2016-11-21 to 2026-11-17
- Overlap observations: 2462
- Level correlation: 0.1487
- Same-day return correlation: 0.0170
- Next-day return correlation: -0.0421

### Dow Jones Industrial Average

- Overlap window: 2016-11-21 to 2026-11-17
- Overlap observations: 2462
- Level correlation: 0.1814
- Same-day return correlation: -0.0008
- Next-day return correlation: -0.0387

### VIX

- Overlap window: 2016-11-21 to 2026-11-17
- Overlap observations: 2462
- Level correlation: -0.0751
- Same-day return correlation: 0.0398
- Next-day return correlation: -0.0142

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
