# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-07-27
- Spread observations: 9765

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-04 to 2026-07-27
- Overlap observations: 2459
- Level correlation: 0.0562
- Same-day return correlation: 0.0172
- Next-day return correlation: -0.0562

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-07-27
- Overlap observations: 9735
- Level correlation: 0.3309
- Same-day return correlation: -0.0236
- Next-day return correlation: -0.0115

### Dow Jones Industrial Average

- Overlap window: 2016-08-04 to 2026-07-27
- Overlap observations: 2459
- Level correlation: 0.1002
- Same-day return correlation: 0.0052
- Next-day return correlation: -0.0468

### VIX

- Overlap window: 1990-01-02 to 2026-07-27
- Overlap observations: 9077
- Level correlation: -0.0709
- Same-day return correlation: 0.0448
- Next-day return correlation: -0.0192

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
