# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-09-15
- Spread observations: 8395

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-16 to 2026-09-15
- Overlap observations: 2463
- Level correlation: 0.0829
- Same-day return correlation: 0.0167
- Next-day return correlation: -0.0543

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-09-15
- Overlap observations: 8369
- Level correlation: 0.3121
- Same-day return correlation: -0.0258
- Next-day return correlation: -0.0162

### Dow Jones Industrial Average

- Overlap window: 2016-09-16 to 2026-09-15
- Overlap observations: 2463
- Level correlation: 0.1209
- Same-day return correlation: 0.0041
- Next-day return correlation: -0.0442

### VIX

- Overlap window: 1990-01-02 to 2026-09-15
- Overlap observations: 7746
- Level correlation: -0.0813
- Same-day return correlation: 0.0432
- Next-day return correlation: -0.0121

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
