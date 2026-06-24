# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-06-22
- Spread observations: 9741

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-24 to 2026-06-22
- Overlap observations: 2463
- Level correlation: 0.0928
- Same-day return correlation: 0.0185
- Next-day return correlation: -0.0567

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-06-22
- Overlap observations: 9711
- Level correlation: 0.3358
- Same-day return correlation: -0.0232
- Next-day return correlation: -0.0115

### Dow Jones Industrial Average

- Overlap window: 2016-06-24 to 2026-06-22
- Overlap observations: 2463
- Level correlation: 0.1416
- Same-day return correlation: 0.0066
- Next-day return correlation: -0.0472

### VIX

- Overlap window: 1990-01-02 to 2026-06-22
- Overlap observations: 9053
- Level correlation: -0.0709
- Same-day return correlation: 0.0440
- Next-day return correlation: -0.0182

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
