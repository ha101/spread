# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-08-18
- Spread observations: 9781

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-19 to 2026-08-18
- Overlap observations: 2464
- Level correlation: 0.0666
- Same-day return correlation: 0.0165
- Next-day return correlation: -0.0544

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-08-18
- Overlap observations: 9751
- Level correlation: 0.3340
- Same-day return correlation: -0.0237
- Next-day return correlation: -0.0109

### Dow Jones Industrial Average

- Overlap window: 2016-08-19 to 2026-08-18
- Overlap observations: 2464
- Level correlation: 0.1085
- Same-day return correlation: 0.0040
- Next-day return correlation: -0.0450

### VIX

- Overlap window: 1990-01-02 to 2026-08-18
- Overlap observations: 9093
- Level correlation: -0.0717
- Same-day return correlation: 0.0448
- Next-day return correlation: -0.0206

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
