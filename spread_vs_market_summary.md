# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-06-29
- Spread observations: 9746

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-05 to 2026-06-29
- Overlap observations: 2462
- Level correlation: 0.0809
- Same-day return correlation: 0.0172
- Next-day return correlation: -0.0564

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-06-29
- Overlap observations: 9716
- Level correlation: 0.3340
- Same-day return correlation: -0.0236
- Next-day return correlation: -0.0116

### Dow Jones Industrial Average

- Overlap window: 2016-07-05 to 2026-06-29
- Overlap observations: 2462
- Level correlation: 0.1286
- Same-day return correlation: 0.0062
- Next-day return correlation: -0.0469

### VIX

- Overlap window: 1990-01-02 to 2026-06-29
- Overlap observations: 9058
- Level correlation: -0.0709
- Same-day return correlation: 0.0445
- Next-day return correlation: -0.0186

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
