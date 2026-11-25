# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-11-24
- Spread observations: 8445

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-28 to 2026-11-24
- Overlap observations: 2463
- Level correlation: 0.1681
- Same-day return correlation: 0.0173
- Next-day return correlation: -0.0491

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-11-24
- Overlap observations: 8419
- Level correlation: 0.3431
- Same-day return correlation: -0.0233
- Next-day return correlation: -0.0146

### Dow Jones Industrial Average

- Overlap window: 2016-11-25 to 2026-11-24
- Overlap observations: 2464
- Level correlation: 0.1808
- Same-day return correlation: 0.0013
- Next-day return correlation: -0.0412

### VIX

- Overlap window: 1990-01-02 to 2026-11-24
- Overlap observations: 7796
- Level correlation: -0.0842
- Same-day return correlation: 0.0417
- Next-day return correlation: -0.0136

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
