# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-03-23
- Spread observations: 9681

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-01 to 2026-03-23
- Overlap observations: 2462
- Level correlation: 0.0606
- Same-day return correlation: 0.0157
- Next-day return correlation: -0.0600

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-03-23
- Overlap observations: 9651
- Level correlation: 0.3224
- Same-day return correlation: -0.0247
- Next-day return correlation: -0.0115

### Dow Jones Industrial Average

- Overlap window: 2016-04-01 to 2026-03-23
- Overlap observations: 2462
- Level correlation: 0.1302
- Same-day return correlation: 0.0033
- Next-day return correlation: -0.0523

### VIX

- Overlap window: 1990-01-02 to 2026-03-23
- Overlap observations: 8993
- Level correlation: -0.0741
- Same-day return correlation: 0.0448
- Next-day return correlation: -0.0169

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
