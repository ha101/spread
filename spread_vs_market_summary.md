# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-05-26
- Spread observations: 9723

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-02 to 2026-05-26
- Overlap observations: 2461
- Level correlation: 0.1255
- Same-day return correlation: 0.0191
- Next-day return correlation: -0.0565

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-05-26
- Overlap observations: 9693
- Level correlation: 0.3416
- Same-day return correlation: -0.0228
- Next-day return correlation: -0.0112

### Dow Jones Industrial Average

- Overlap window: 2016-05-31 to 2026-05-26
- Overlap observations: 2463
- Level correlation: 0.1775
- Same-day return correlation: 0.0070
- Next-day return correlation: -0.0473

### VIX

- Overlap window: 1990-01-02 to 2026-05-26
- Overlap observations: 9035
- Level correlation: -0.0710
- Same-day return correlation: 0.0433
- Next-day return correlation: -0.0187

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
