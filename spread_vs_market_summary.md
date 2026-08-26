# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-08-25
- Spread observations: 9786

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-26 to 2026-08-25
- Overlap observations: 2464
- Level correlation: 0.0659
- Same-day return correlation: 0.0171
- Next-day return correlation: -0.0540

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-08-25
- Overlap observations: 9756
- Level correlation: 0.3342
- Same-day return correlation: -0.0234
- Next-day return correlation: -0.0111

### Dow Jones Industrial Average

- Overlap window: 2016-08-26 to 2026-08-25
- Overlap observations: 2464
- Level correlation: 0.1071
- Same-day return correlation: 0.0048
- Next-day return correlation: -0.0437

### VIX

- Overlap window: 1990-01-02 to 2026-08-25
- Overlap observations: 9098
- Level correlation: -0.0719
- Same-day return correlation: 0.0444
- Next-day return correlation: -0.0206

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
