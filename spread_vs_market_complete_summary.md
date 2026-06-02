# Brent/WTI Spread vs Market Indexes (Complete Case)

- Spread window: 2016-06-02 to 2026-05-26
- Spread observations: 2461

## Correlations By Series

### S&P 500

- Overlap window: 2016-06-02 to 2026-05-26
- Overlap observations: 2461
- Level correlation: 0.1255
- Same-day return correlation: 0.0191
- Next-day return correlation: -0.0568

### Nasdaq Composite

- Overlap window: 2016-06-02 to 2026-05-26
- Overlap observations: 2461
- Level correlation: 0.0963
- Same-day return correlation: 0.0233
- Next-day return correlation: -0.0566

### Dow Jones Industrial Average

- Overlap window: 2016-06-02 to 2026-05-26
- Overlap observations: 2461
- Level correlation: 0.1759
- Same-day return correlation: 0.0070
- Next-day return correlation: -0.0476

### VIX

- Overlap window: 2016-06-02 to 2026-05-26
- Overlap observations: 2461
- Level correlation: -0.0275
- Same-day return correlation: 0.0372
- Next-day return correlation: -0.0004

## Notes

- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.
- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.
- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.
