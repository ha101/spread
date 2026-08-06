# Brent/WTI Spread vs Market Indexes

- Spread window: 1987-05-20 to 2026-08-03
- Spread observations: 9770

## Correlations By Series

### S&P 500

- Overlap window: 2016-08-08 to 2026-08-03
- Overlap observations: 2462
- Level correlation: 0.0581
- Same-day return correlation: 0.0162
- Next-day return correlation: -0.0536

### Nasdaq Composite

- Overlap window: 1987-05-20 to 2026-08-03
- Overlap observations: 9740
- Level correlation: 0.3315
- Same-day return correlation: -0.0237
- Next-day return correlation: -0.0105

### Dow Jones Industrial Average

- Overlap window: 2016-08-08 to 2026-08-03
- Overlap observations: 2462
- Level correlation: 0.1016
- Same-day return correlation: 0.0034
- Next-day return correlation: -0.0442

### VIX

- Overlap window: 1990-01-02 to 2026-08-03
- Overlap observations: 9082
- Level correlation: -0.0710
- Same-day return correlation: 0.0446
- Next-day return correlation: -0.0200

## Notes

- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.
- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.
- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.
