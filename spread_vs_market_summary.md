# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-10-27
- Spread observations: 8425

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-28 to 2026-10-27
- Overlap observations: 2463
- Level correlation: 0.1828
- Same-day return correlation: 0.0184
- Next-day return correlation: -0.0507

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-10-27
- Overlap observations: 8399
- Level correlation: 0.3431
- Same-day return correlation: -0.0238
- Next-day return correlation: -0.0151

### Dow Jones Industrial Average

- Overlap window: 2016-10-28 to 2026-10-27
- Overlap observations: 2463
- Level correlation: 0.1981
- Same-day return correlation: 0.0072
- Next-day return correlation: -0.0444

### VIX

- Overlap window: 1990-01-02 to 2026-10-27
- Overlap observations: 7776
- Level correlation: -0.0849
- Same-day return correlation: 0.0389
- Next-day return correlation: -0.0102

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
