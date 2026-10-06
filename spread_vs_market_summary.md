# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-09-29
- Spread observations: 8405

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-06 to 2026-09-29
- Overlap observations: 2459
- Level correlation: 0.1178
- Same-day return correlation: 0.0175
- Next-day return correlation: -0.0545

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-09-29
- Overlap observations: 8379
- Level correlation: 0.3224
- Same-day return correlation: -0.0257
- Next-day return correlation: -0.0163

### Dow Jones Industrial Average

- Overlap window: 2016-10-07 to 2026-09-29
- Overlap observations: 2458
- Level correlation: 0.1469
- Same-day return correlation: 0.0060
- Next-day return correlation: -0.0451

### VIX

- Overlap window: 1990-01-02 to 2026-09-29
- Overlap observations: 7756
- Level correlation: -0.0828
- Same-day return correlation: 0.0431
- Next-day return correlation: -0.0110

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
