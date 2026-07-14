# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-07-06
- Spread observations: 9750

## Correlations By Series

### S&P 500

- Overlap window: 2016-07-14 to 2026-07-06
- Overlap observations: 2459
- Level correlation: 0.0687
- Same-day return correlation: 0.0178
- Next-day return correlation: -0.0571

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-07-06
- Overlap observations: 9720
- Level correlation: 0.3323
- Same-day return correlation: -0.0235
- Next-day return correlation: -0.0116

### Dow Jones Industrial Average

- Overlap window: 2016-07-14 to 2026-07-06
- Overlap observations: 2459
- Level correlation: 0.1151
- Same-day return correlation: 0.0065
- Next-day return correlation: -0.0476

### VIX

- Overlap window: 1990-01-02 to 2026-07-06
- Overlap observations: 9062
- Level correlation: -0.0708
- Same-day return correlation: 0.0445
- Next-day return correlation: -0.0185

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
