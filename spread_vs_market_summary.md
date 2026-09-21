# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-09-15
- Spread observations: 8395

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-22 to 2026-09-15
- Overlap observations: 2459
- Level correlation: 0.0812
- Same-day return correlation: 0.0168
- Next-day return correlation: -0.0540

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-09-15
- Overlap observations: 8369
- Level correlation: 0.3121
- Same-day return correlation: -0.0258
- Next-day return correlation: -0.0162

### Dow Jones Industrial Average

- Overlap window: 2016-09-22 to 2026-09-15
- Overlap observations: 2459
- Level correlation: 0.1189
- Same-day return correlation: 0.0041
- Next-day return correlation: -0.0439

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
