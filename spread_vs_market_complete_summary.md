# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-10-10 to 2026-10-06
- Spread observations: 2462

## Correlations By Series

### S&P 500

- Overlap window: 2016-10-10 to 2026-10-06
- Overlap observations: 2462
- Level correlation: 0.1400
- Same-day return correlation: 0.0186
- Next-day return correlation: -0.0515

### Nasdaq Composite

- Overlap window: 2016-10-10 to 2026-10-06
- Overlap observations: 2462
- Level correlation: 0.1162
- Same-day return correlation: 0.0224
- Next-day return correlation: -0.0510

### Dow Jones Industrial Average

- Overlap window: 2016-10-10 to 2026-10-06
- Overlap observations: 2462
- Level correlation: 0.1649
- Same-day return correlation: 0.0071
- Next-day return correlation: -0.0437

### VIX

- Overlap window: 2016-10-10 to 2026-10-06
- Overlap observations: 2462
- Level correlation: -0.0641
- Same-day return correlation: 0.0320
- Next-day return correlation: -0.0028

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
