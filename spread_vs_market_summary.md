# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-03-30
- Spread observations: 9686

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-07 to 2026-03-30
- Overlap observations: 2463
- Level correlation: 0.0743
- Same-day return correlation: 0.0154
- Next-day return correlation: -0.0603

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-03-30
- Overlap observations: 9656
- Level correlation: 0.3258
- Same-day return correlation: -0.0248
- Next-day return correlation: -0.0116

### Dow Jones Industrial Average

- Overlap window: 2016-04-07 to 2026-03-30
- Overlap observations: 2463
- Level correlation: 0.1409
- Same-day return correlation: 0.0027
- Next-day return correlation: -0.0523

### VIX

- Overlap window: 1990-01-02 to 2026-03-30
- Overlap observations: 8998
- Level correlation: -0.0721
- Same-day return correlation: 0.0450
- Next-day return correlation: -0.0170

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
