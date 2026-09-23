# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-09-22
- Spread observations: 8400

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-23 to 2026-09-22
- Overlap observations: 2463
- Level correlation: 0.1003
- Same-day return correlation: 0.0159
- Next-day return correlation: -0.0540

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-09-22
- Overlap observations: 8374
- Level correlation: 0.3167
- Same-day return correlation: -0.0262
- Next-day return correlation: -0.0162

### Dow Jones Industrial Average

- Overlap window: 2016-09-23 to 2026-09-22
- Overlap observations: 2463
- Level correlation: 0.1352
- Same-day return correlation: 0.0037
- Next-day return correlation: -0.0444

### VIX

- Overlap window: 1990-01-02 to 2026-09-22
- Overlap observations: 7751
- Level correlation: -0.0820
- Same-day return correlation: 0.0441
- Next-day return correlation: -0.0117

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
