# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-03-23
- Spread observations: 9681

## Correlations By Series

### S&P 500

- Overlap window: 2016-03-21 to 2026-03-20
- Overlap observations: 2469
- Level correlation: 0.0581
- Same-day return correlation: 0.0184
- Next-day return correlation: -0.0619

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-03-20
- Overlap observations: 9650
- Level correlation: 0.3206
- Same-day return correlation: -0.0240
- Next-day return correlation: -0.0122

### Dow Jones Industrial Average

- Overlap window: 2016-03-21 to 2026-03-20
- Overlap observations: 2469
- Level correlation: 0.1303
- Same-day return correlation: 0.0061
- Next-day return correlation: -0.0533

### VIX

- Overlap window: 1990-01-02 to 2026-03-20
- Overlap observations: 8992
- Level correlation: -0.0747
- Same-day return correlation: 0.0438
- Next-day return correlation: -0.0164

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
