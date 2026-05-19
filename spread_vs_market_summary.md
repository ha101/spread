# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-05-11
- Spread observations: 9713

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-20 to 2026-05-11
- Overlap observations: 2459
- Level correlation: 0.1293
- Same-day return correlation: 0.0178
- Next-day return correlation: -0.0566

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-05-11
- Overlap observations: 9683
- Level correlation: 0.3418
- Same-day return correlation: -0.0233
- Next-day return correlation: -0.0112

### Dow Jones Industrial Average

- Overlap window: 2016-05-20 to 2026-05-11
- Overlap observations: 2459
- Level correlation: 0.1810
- Same-day return correlation: 0.0053
- Next-day return correlation: -0.0471

### VIX

- Overlap window: 1990-01-02 to 2026-05-11
- Overlap observations: 9025
- Level correlation: -0.0708
- Same-day return correlation: 0.0437
- Next-day return correlation: -0.0187

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
