# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-11-14 to 2026-11-03
- Spread observations: 2457

## Correlations By Series

### S&P 500

- Overlap window: 2016-11-14 to 2026-11-03
- Overlap observations: 2457
- Level correlation: 0.1797
- Same-day return correlation: 0.0181
- Next-day return correlation: -0.0500

### Nasdaq Composite

- Overlap window: 2016-11-14 to 2026-11-03
- Overlap observations: 2457
- Level correlation: 0.1592
- Same-day return correlation: 0.0225
- Next-day return correlation: -0.0486

### Dow Jones Industrial Average

- Overlap window: 2016-11-14 to 2026-11-03
- Overlap observations: 2457
- Level correlation: 0.1931
- Same-day return correlation: 0.0064
- Next-day return correlation: -0.0430

### VIX

- Overlap window: 2016-11-14 to 2026-11-03
- Overlap observations: 2457
- Level correlation: -0.0723
- Same-day return correlation: 0.0299
- Next-day return correlation: -0.0028

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
