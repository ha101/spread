# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-02 to 2026-04-27
- Spread observations: 2464

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-02 to 2026-04-27
- Overlap observations: 2464
- Level correlation: 0.1282
- Same-day return correlation: 0.0191
- Next-day return correlation: -0.0560

### Nasdaq Composite

- Overlap window: 2016-05-02 to 2026-04-27
- Overlap observations: 2464
- Level correlation: 0.0984
- Same-day return correlation: 0.0243
- Next-day return correlation: -0.0557

### Dow Jones Industrial Average

- Overlap window: 2016-05-02 to 2026-04-27
- Overlap observations: 2464
- Level correlation: 0.1829
- Same-day return correlation: 0.0052
- Next-day return correlation: -0.0471

### VIX

- Overlap window: 2016-05-02 to 2026-04-27
- Overlap observations: 2464
- Level correlation: -0.0204
- Same-day return correlation: 0.0379
- Next-day return correlation: -0.0002

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
