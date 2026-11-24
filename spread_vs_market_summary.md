# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-11-17
- Spread observations: 8440

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-25 to 2026-11-17
- Overlap observations: 2459
- Level correlation: 0.1665
- Same-day return correlation: 0.0124
- Next-day return correlation: -0.0439

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-11-17
- Overlap observations: 8414
- Level correlation: 0.3424
- Same-day return correlation: -0.0256
- Next-day return correlation: -0.0121

### Dow Jones Industrial Average

- Overlap window: 2016-11-25 to 2026-11-17
- Overlap observations: 2459
- Level correlation: 0.1788
- Same-day return correlation: -0.0008
- Next-day return correlation: -0.0385

### VIX

- Overlap window: 1990-01-02 to 2026-11-17
- Overlap observations: 7791
- Level correlation: -0.0848
- Same-day return correlation: 0.0438
- Next-day return correlation: -0.0157

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
