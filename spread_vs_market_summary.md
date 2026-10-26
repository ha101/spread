# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-10-20
- Spread observations: 8420

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-27 to 2026-10-20
- Overlap observations: 2459
- Level correlation: 0.1695
- Same-day return correlation: 0.0192
- Next-day return correlation: -0.0489

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-10-20
- Overlap observations: 8394
- Level correlation: 0.3391
- Same-day return correlation: -0.0232
- Next-day return correlation: -0.0143

### Dow Jones Industrial Average

- Overlap window: 2016-10-24 to 2026-10-20
- Overlap observations: 2462
- Level correlation: 0.1881
- Same-day return correlation: 0.0058
- Next-day return correlation: -0.0426

### VIX

- Overlap window: 1990-01-02 to 2026-10-20
- Overlap observations: 7771
- Level correlation: -0.0849
- Same-day return correlation: 0.0383
- Next-day return correlation: -0.0113

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
