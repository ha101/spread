# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-06-08
- Spread observations: 9732

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-17 to 2026-06-08
- Overlap observations: 2459
- Level correlation: 0.1103
- Same-day return correlation: 0.0183
- Next-day return correlation: -0.0561

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-06-08
- Overlap observations: 9702
- Level correlation: 0.3394
- Same-day return correlation: -0.0231
- Next-day return correlation: -0.0112

### Dow Jones Industrial Average

- Overlap window: 2016-06-17 to 2026-06-08
- Overlap observations: 2459
- Level correlation: 0.1598
- Same-day return correlation: 0.0064
- Next-day return correlation: -0.0468

### VIX

- Overlap window: 1990-01-02 to 2026-06-08
- Overlap observations: 9044
- Level correlation: -0.0710
- Same-day return correlation: 0.0439
- Next-day return correlation: -0.0187

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
