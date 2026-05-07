# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-05-01
- Spread observations: 9708

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-09 to 2026-05-01
- Overlap observations: 2463
- Level correlation: 0.1349
- Same-day return correlation: 0.0190
- Next-day return correlation: -0.0557

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-05-01
- Overlap observations: 9678
- Level correlation: 0.3419
- Same-day return correlation: -0.0229
- Next-day return correlation: -0.0106

### Dow Jones Industrial Average

- Overlap window: 2016-05-09 to 2026-05-01
- Overlap observations: 2463
- Level correlation: 0.1877
- Same-day return correlation: 0.0058
- Next-day return correlation: -0.0471

### VIX

- Overlap window: 1990-01-02 to 2026-05-01
- Overlap observations: 9020
- Level correlation: -0.0708
- Same-day return correlation: 0.0438
- Next-day return correlation: -0.0188

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
