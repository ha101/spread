# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-11-07 to 2026-11-03
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-07 to 2026-11-03
- Overlap observations: 2462
- Level correlation: 0.1834
- Same-day return correlation: 0.0182
- Next-day return correlation: -0.0498

### Nasdaq Composite

- Overlap window: 2016-11-07 to 2026-11-03
- Overlap observations: 2462
- Level correlation: 0.1631
- Same-day return correlation: 0.0224
- Next-day return correlation: -0.0484

### Dow Jones Industrial Average

- Overlap window: 2016-11-07 to 2026-11-03
- Overlap observations: 2462
- Level correlation: 0.1976
- Same-day return correlation: 0.0065
- Next-day return correlation: -0.0428

### VIX

- Overlap window: 2016-11-07 to 2026-11-03
- Overlap observations: 2462
- Level correlation: -0.0710
- Same-day return correlation: 0.0298
- Next-day return correlation: -0.0032

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
