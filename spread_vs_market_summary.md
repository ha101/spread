# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-04-13
- Spread observations: 9694

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-15 to 2026-04-13
- Overlap observations: 2465
- Level correlation: 0.1031
- Same-day return correlation: 0.0194
- Next-day return correlation: -0.0553

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-04-13
- Overlap observations: 9664
- Level correlation: 0.3327
- Same-day return correlation: -0.0231
- Next-day return correlation: -0.0103

### Dow Jones Industrial Average

- Overlap window: 2016-04-15 to 2026-04-13
- Overlap observations: 2465
- Level correlation: 0.1636
- Same-day return correlation: 0.0062
- Next-day return correlation: -0.0458

### VIX

- Overlap window: 1990-01-02 to 2026-04-13
- Overlap observations: 9006
- Level correlation: -0.0705
- Same-day return correlation: 0.0445
- Next-day return correlation: -0.0186

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
