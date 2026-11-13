# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-11-11
- Spread observations: 8436

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-14 to 2026-11-11
- Overlap observations: 2463
- Level correlation: 0.1743
- Same-day return correlation: 0.0124
- Next-day return correlation: -0.0435

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-11-11
- Overlap observations: 8410
- Level correlation: 0.3429
- Same-day return correlation: -0.0255
- Next-day return correlation: -0.0120

### Dow Jones Industrial Average

- Overlap window: 2016-11-14 to 2026-11-11
- Overlap observations: 2463
- Level correlation: 0.1876
- Same-day return correlation: -0.0007
- Next-day return correlation: -0.0382

### VIX

- Overlap window: 1990-01-02 to 2026-11-11
- Overlap observations: 7787
- Level correlation: -0.0848
- Same-day return correlation: 0.0437
- Next-day return correlation: -0.0160

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
