# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-05-05 to 2026-04-27
- Spread observations: 2461

## Correlations By Series

### S&P 500

- Overlap window: 2016-05-05 to 2026-04-27
- Overlap observations: 2461
- Level correlation: 0.1261
- Same-day return correlation: 0.0188
- Next-day return correlation: -0.0563

### Nasdaq Composite

- Overlap window: 2016-05-05 to 2026-04-27
- Overlap observations: 2461
- Level correlation: 0.0962
- Same-day return correlation: 0.0240
- Next-day return correlation: -0.0560

### Dow Jones Industrial Average

- Overlap window: 2016-05-05 to 2026-04-27
- Overlap observations: 2461
- Level correlation: 0.1806
- Same-day return correlation: 0.0049
- Next-day return correlation: -0.0474

### VIX

- Overlap window: 2016-05-05 to 2026-04-27
- Overlap observations: 2461
- Level correlation: -0.0211
- Same-day return correlation: 0.0382
- Next-day return correlation: 0.0001

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
