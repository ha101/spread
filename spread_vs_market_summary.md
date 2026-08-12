# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-08-11
- Spread observations: 9776

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-12 to 2026-08-11
- Overlap observations: 2464
- Level correlation: 0.0640
- Same-day return correlation: 0.0165
- Next-day return correlation: -0.0547

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-08-11
- Overlap observations: 9746
- Level correlation: 0.3330
- Same-day return correlation: -0.0236
- Next-day return correlation: -0.0110

### Dow Jones Industrial Average

- Overlap window: 2016-08-12 to 2026-08-11
- Overlap observations: 2464
- Level correlation: 0.1066
- Same-day return correlation: 0.0039
- Next-day return correlation: -0.0452

### VIX

- Overlap window: 1990-01-02 to 2026-08-11
- Overlap observations: 9088
- Level correlation: -0.0714
- Same-day return correlation: 0.0447
- Next-day return correlation: -0.0205

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
