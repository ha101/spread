# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-07-20
- Spread observations: 9760

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-25 to 2026-07-20
- Overlap observations: 2462
- Level correlation: 0.0556
- Same-day return correlation: 0.0177
- Next-day return correlation: -0.0568

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-07-20
- Overlap observations: 9730
- Level correlation: 0.3298
- Same-day return correlation: -0.0235
- Next-day return correlation: -0.0114

### Dow Jones Industrial Average

- Overlap window: 2016-07-25 to 2026-07-20
- Overlap observations: 2462
- Level correlation: 0.1009
- Same-day return correlation: 0.0060
- Next-day return correlation: -0.0475

### VIX

- Overlap window: 1990-01-02 to 2026-07-20
- Overlap observations: 9072
- Level correlation: -0.0708
- Same-day return correlation: 0.0446
- Next-day return correlation: -0.0188

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
