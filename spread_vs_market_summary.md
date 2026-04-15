# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-04-08
- Spread observations: 9692

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-15 to 2026-04-08
- Overlap observations: 2463
- Level correlation: 0.0748
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0594

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-04-08
- Overlap observations: 9662
- Level correlation: 0.3265
- Same-day return correlation: -0.0234
- Next-day return correlation: -0.0117

### Dow Jones Industrial Average

- Overlap window: 2016-04-15 to 2026-04-08
- Overlap observations: 2463
- Level correlation: 0.1393
- Same-day return correlation: 0.0060
- Next-day return correlation: -0.0504

### VIX

- Overlap window: 1990-01-02 to 2026-04-08
- Overlap observations: 9004
- Level correlation: -0.0714
- Same-day return correlation: 0.0424
- Next-day return correlation: -0.0177

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
