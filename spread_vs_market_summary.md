# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-07-13
- Spread observations: 9755

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-18 to 2026-07-13
- Overlap observations: 2462
- Level correlation: 0.0624
- Same-day return correlation: 0.0176
- Next-day return correlation: -0.0571

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-07-13
- Overlap observations: 9725
- Level correlation: 0.3309
- Same-day return correlation: -0.0236
- Next-day return correlation: -0.0116

### Dow Jones Industrial Average

- Overlap window: 2016-07-18 to 2026-07-13
- Overlap observations: 2462
- Level correlation: 0.1083
- Same-day return correlation: 0.0061
- Next-day return correlation: -0.0477

### VIX

- Overlap window: 1990-01-02 to 2026-07-13
- Overlap observations: 9067
- Level correlation: -0.0708
- Same-day return correlation: 0.0446
- Next-day return correlation: -0.0185

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
