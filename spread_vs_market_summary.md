# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-06-15
- Spread observations: 9737

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-24 to 2026-06-15
- Overlap observations: 2459
- Level correlation: 0.1001
- Same-day return correlation: 0.0184
- Next-day return correlation: -0.0564

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-06-15
- Overlap observations: 9707
- Level correlation: 0.3377
- Same-day return correlation: -0.0233
- Next-day return correlation: -0.0114

### Dow Jones Industrial Average

- Overlap window: 2016-06-24 to 2026-06-15
- Overlap observations: 2459
- Level correlation: 0.1489
- Same-day return correlation: 0.0063
- Next-day return correlation: -0.0470

### VIX

- Overlap window: 1990-01-02 to 2026-06-15
- Overlap observations: 9049
- Level correlation: -0.0710
- Same-day return correlation: 0.0441
- Next-day return correlation: -0.0185

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
