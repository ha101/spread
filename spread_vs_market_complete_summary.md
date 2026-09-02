# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-09-02 to 2026-09-01
- Spread observations: 2463

## Correlations By Series

### S&P 500

- Overlap window: 2016-09-02 to 2026-09-01
- Overlap observations: 2463
- Level correlation: 0.0643
- Same-day return correlation: 0.0173
- Next-day return correlation: -0.0543

### Nasdaq Composite

- Overlap window: 2016-09-02 to 2026-09-01
- Overlap observations: 2463
- Level correlation: 0.0336
- Same-day return correlation: 0.0213
- Next-day return correlation: -0.0548

### Dow Jones Industrial Average

- Overlap window: 2016-09-02 to 2026-09-01
- Overlap observations: 2463
- Level correlation: 0.1050
- Same-day return correlation: 0.0050
- Next-day return correlation: -0.0439

### VIX

- Overlap window: 2016-09-02 to 2026-09-01
- Overlap observations: 2463
- Level correlation: -0.0465
- Same-day return correlation: 0.0374
- Next-day return correlation: -0.0055

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
