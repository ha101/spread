# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-05-18
- Spread observations: 9718

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-31 to 2026-05-18
- Overlap observations: 2458
- Level correlation: 0.1261
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0564

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-05-18
- Overlap observations: 9688
- Level correlation: 0.3417
- Same-day return correlation: -0.0232
- Next-day return correlation: -0.0112

### Dow Jones Industrial Average

- Overlap window: 2016-05-31 to 2026-05-18
- Overlap observations: 2458
- Level correlation: 0.1770
- Same-day return correlation: 0.0056
- Next-day return correlation: -0.0473

### VIX

- Overlap window: 1990-01-02 to 2026-05-18
- Overlap observations: 9030
- Level correlation: -0.0709
- Same-day return correlation: 0.0436
- Next-day return correlation: -0.0186

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
