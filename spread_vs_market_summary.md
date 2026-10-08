# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-10-06
- Spread observations: 8410

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-10 to 2026-10-06
- Overlap observations: 2462
- Level correlation: 0.1400
- Same-day return correlation: 0.0186
- Next-day return correlation: -0.0512

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-10-06
- Overlap observations: 8384
- Level correlation: 0.3285
- Same-day return correlation: -0.0243
- Next-day return correlation: -0.0152

### Dow Jones Industrial Average

- Overlap window: 2016-10-10 to 2026-10-06
- Overlap observations: 2462
- Level correlation: 0.1649
- Same-day return correlation: 0.0072
- Next-day return correlation: -0.0434

### VIX

- Overlap window: 1990-01-02 to 2026-10-06
- Overlap observations: 7761
- Level correlation: -0.0836
- Same-day return correlation: 0.0404
- Next-day return correlation: -0.0099

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
