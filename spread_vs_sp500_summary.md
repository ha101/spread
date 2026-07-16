# Brent/WTI Spread vs S&P 500

- Source series:
  - Brent/WTI prices from `all_data.js`
  - S&P 500 from FRED series `SP500`
- Overlap window: 2016-07-18 to 2026-07-13
- Overlap observations: 2462

## Correlations

- Spread level vs S&P 500 level: 0.0624
- Daily spread change vs same-day S&P 500 return: 0.0175
- Daily spread change vs next-day S&P 500 return: -0.0575
- Daily spread change vs previous-day S&P 500 return: 0.0521

## Notes

- The Brent-WTI spread itself begins on 1987-05-20, but the public FRED daily S&P 500 series on this endpoint begins in 2016.
- `spread_change` is measured in dollars per barrel.
- `sp500_return` is a simple daily close-to-close return.
