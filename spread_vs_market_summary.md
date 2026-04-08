# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-04-08
- Spread observations: 9692

## Correlations By Series

### S&P 500

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2467
- Level correlation: 0.0789
- Same-day return correlation: 0.0164
- Next-day return correlation: -0.0598

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-04-07
- Overlap observations: 9661
- Level correlation: 0.3268
- Same-day return correlation: -0.0239
- Next-day return correlation: -0.0118

### Dow Jones Industrial Average

- Overlap window: 2016-04-08 to 2026-04-07
- Overlap observations: 2467
- Level correlation: 0.1436
- Same-day return correlation: 0.0042
- Next-day return correlation: -0.0509

### VIX

- Overlap window: 1990-01-02 to 2026-04-07
- Overlap observations: 9003
- Level correlation: -0.0714
- Same-day return correlation: 0.0432
- Next-day return correlation: -0.0175

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
