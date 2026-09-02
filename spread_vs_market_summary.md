# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-09-01
- Spread observations: 9790

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-02 to 2026-09-01
- Overlap observations: 2463
- Level correlation: 0.0643
- Same-day return correlation: 0.0173
- Next-day return correlation: -0.0539

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-09-01
- Overlap observations: 9760
- Level correlation: 0.3340
- Same-day return correlation: -0.0233
- Next-day return correlation: -0.0111

### Dow Jones Industrial Average

- Overlap window: 2016-09-06 to 2026-09-01
- Overlap observations: 2462
- Level correlation: 0.1044
- Same-day return correlation: 0.0051
- Next-day return correlation: -0.0435

### VIX

- Overlap window: 1990-01-02 to 2026-09-01
- Overlap observations: 9102
- Level correlation: -0.0720
- Same-day return correlation: 0.0442
- Next-day return correlation: -0.0206

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
