# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-04-20
- Spread observations: 9699

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-28 to 2026-04-20
- Overlap observations: 2461
- Level correlation: 0.1164
- Same-day return correlation: 0.0179
- Next-day return correlation: -0.0550

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-04-20
- Overlap observations: 9669
- Level correlation: 0.3367
- Same-day return correlation: -0.0236
- Next-day return correlation: -0.0099

### Dow Jones Industrial Average

- Overlap window: 2016-04-28 to 2026-04-20
- Overlap observations: 2461
- Level correlation: 0.1732
- Same-day return correlation: 0.0043
- Next-day return correlation: -0.0469

### VIX

- Overlap window: 1990-01-02 to 2026-04-20
- Overlap observations: 9011
- Level correlation: -0.0706
- Same-day return correlation: 0.0445
- Next-day return correlation: -0.0193

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
