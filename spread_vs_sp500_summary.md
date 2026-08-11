# Brent/WTI Spread vs S&P 500

- Source series:
  - Brent/WTI prices from `all_data.js`
  - S&P 500 from FRED series `SP500`
- Overlap window: 2016-08-11 to 2026-08-03
- Overlap observations: 2459

## Correlations

- Spread level vs S&P 500 level: 0.0562
- Daily spread change vs same-day S&P 500 return: 0.0162
- Daily spread change vs next-day S&P 500 return: -0.0539
- Daily spread change vs previous-day S&P 500 return: 0.0519

## Notes

- The Brent-WTI spread itself begins on 1987-05-20, but the public FRED daily S&P 500 series on this endpoint begins in 2016.
- `spread_change` is measured in dollars per barrel.
- `sp500_return` is a simple daily close-to-close return.
