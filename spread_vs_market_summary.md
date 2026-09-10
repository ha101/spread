# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-09-09
- Spread observations: 9795

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-12 to 2026-09-09
- Overlap observations: 2463
- Level correlation: 0.0689
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0549

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-09-09
- Overlap observations: 9765
- Level correlation: 0.3354
- Same-day return correlation: -0.0232
- Next-day return correlation: -0.0112

### Dow Jones Industrial Average

- Overlap window: 2016-09-12 to 2026-09-09
- Overlap observations: 2463
- Level correlation: 0.1087
- Same-day return correlation: 0.0055
- Next-day return correlation: -0.0449

### VIX

- Overlap window: 1990-01-02 to 2026-09-09
- Overlap observations: 9107
- Level correlation: -0.0724
- Same-day return correlation: 0.0442
- Next-day return correlation: -0.0203

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
