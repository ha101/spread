# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-09-29
- Spread observations: 8405

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-03 to 2026-09-29
- Overlap observations: 2462
- Level correlation: 0.1198
- Same-day return correlation: 0.0175
- Next-day return correlation: -0.0544

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-09-29
- Overlap observations: 8379
- Level correlation: 0.3224
- Same-day return correlation: -0.0257
- Next-day return correlation: -0.0163

### Dow Jones Industrial Average

- Overlap window: 2016-10-03 to 2026-09-29
- Overlap observations: 2462
- Level correlation: 0.1501
- Same-day return correlation: 0.0059
- Next-day return correlation: -0.0449

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
