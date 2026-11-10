# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-11-03
- Spread observations: 8430

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-11 to 2026-11-03
- Overlap observations: 2458
- Level correlation: 0.1805
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0496

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-11-03
- Overlap observations: 8404
- Level correlation: 0.3444
- Same-day return correlation: -0.0237
- Next-day return correlation: -0.0145

### Dow Jones Industrial Average

- Overlap window: 2016-11-10 to 2026-11-03
- Overlap observations: 2459
- Level correlation: 0.1948
- Same-day return correlation: 0.0064
- Next-day return correlation: -0.0427

### VIX

- Overlap window: 1990-01-02 to 2026-11-03
- Overlap observations: 7781
- Level correlation: -0.0849
- Same-day return correlation: 0.0389
- Next-day return correlation: -0.0102

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
