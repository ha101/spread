# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-04-27
- Spread observations: 9704

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-29 to 2026-04-27
- Overlap observations: 2465
- Level correlation: 0.1289
- Same-day return correlation: 0.0193
- Next-day return correlation: -0.0559

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-04-27
- Overlap observations: 9674
- Level correlation: 0.3397
- Same-day return correlation: -0.0228
- Next-day return correlation: -0.0106

### Dow Jones Industrial Average

- Overlap window: 2016-04-29 to 2026-04-27
- Overlap observations: 2465
- Level correlation: 0.1837
- Same-day return correlation: 0.0054
- Next-day return correlation: -0.0470

### VIX

- Overlap window: 1990-01-02 to 2026-04-27
- Overlap observations: 9016
- Level correlation: -0.0706
- Same-day return correlation: 0.0441
- Next-day return correlation: -0.0189

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
