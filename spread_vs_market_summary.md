# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-04-08
- Spread observations: 9750

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2513
- Level correlation: 0.0726
- Same-day return correlation: 0.0092
- Next-day return correlation: -0.0376

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-04-07
- Overlap observations: 9716
- Level correlation: 0.3254
- Same-day return correlation: -0.0264
- Next-day return correlation: -0.0052

### Dow Jones Industrial Average

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2513
- Level correlation: 0.1368
- Same-day return correlation: -0.0005
- Next-day return correlation: -0.0320

### VIX

- Overlap window: 1990-01-02 to 2026-04-07
- Overlap observations: 9060
- Level correlation: -0.0699
- Same-day return correlation: 0.0430
- Next-day return correlation: -0.0215

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
