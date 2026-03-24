# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-03-23
- Spread observations: 9681

## Correlations By Series

### S&P 500

- Overlap window: 2016-03-24 to 2026-03-23
- Overlap observations: 2467
- Level correlation: 0.0576
- Same-day return correlation: 0.0180
- Next-day return correlation: -0.0618

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-03-23
- Overlap observations: 9651
- Level correlation: 0.3210
- Same-day return correlation: -0.0241
- Next-day return correlation: -0.0121

### Dow Jones Industrial Average

- Overlap window: 2016-03-24 to 2026-03-23
- Overlap observations: 2467
- Level correlation: 0.1293
- Same-day return correlation: 0.0055
- Next-day return correlation: -0.0531

### VIX

- Overlap window: 1990-01-02 to 2026-03-23
- Overlap observations: 8993
- Level correlation: -0.0746
- Same-day return correlation: 0.0439
- Next-day return correlation: -0.0165

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
