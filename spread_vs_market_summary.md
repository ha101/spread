# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-10-14
- Spread observations: 8416

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-17 to 2026-10-14
- Overlap observations: 2463
- Level correlation: 0.1664
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0499

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-10-14
- Overlap observations: 8390
- Level correlation: 0.3368
- Same-day return correlation: -0.0243
- Next-day return correlation: -0.0146

### Dow Jones Industrial Average

- Overlap window: 2016-10-17 to 2026-10-14
- Overlap observations: 2463
- Level correlation: 0.1850
- Same-day return correlation: 0.0069
- Next-day return correlation: -0.0431

### VIX

- Overlap window: 1990-01-02 to 2026-10-14
- Overlap observations: 7767
- Level correlation: -0.0847
- Same-day return correlation: 0.0404
- Next-day return correlation: -0.0106

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
