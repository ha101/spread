import csv
import math
from pathlib import Path

from fred_series_utils import fetch_fred_series, load_all_data_rows


BASE_PATH = Path(__file__).parent
DATA_PATH = BASE_PATH / 'all_data.js'
SP500_CACHE_PATH = BASE_PATH / 'sp500_fred.txt'
OUTPUT_CSV_PATH = BASE_PATH / 'spread_vs_sp500.csv'
OUTPUT_SUMMARY_PATH = BASE_PATH / 'spread_vs_sp500_summary.md'
SP500_SERIES_ID = 'SP500'


def pearson(x_values, y_values):
    if len(x_values) != len(y_values) or len(x_values) < 2:
        return None

    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    x_denominator = math.sqrt(sum((x - x_mean) ** 2 for x in x_values))
    y_denominator = math.sqrt(sum((y - y_mean) ** 2 for y in y_values))
    if x_denominator == 0 or y_denominator == 0:
        return None
    return numerator / (x_denominator * y_denominator)


def format_corr(value):
    return 'n/a' if value is None else f'{value:.4f}'


def build_rows(spread_rows, sp500_series):
    rows = []
    last_sp500_close = None

    for date, wti, brent in spread_rows:
        sp500_close = sp500_series.get(date)
        if sp500_close is None:
            continue

        row = {
            'date': date,
            'wti': round(float(wti), 2),
            'brent': round(float(brent), 2),
            'spread': round(float(brent) - float(wti), 2),
            'spread_change': '',
            'sp500_close': sp500_close,
            'sp500_change': '',
            'sp500_return': '',
        }

        if rows:
            row['spread_change'] = round(row['spread'] - rows[-1]['spread'], 4)

        if last_sp500_close is not None:
            sp500_change = sp500_close - last_sp500_close
            row['sp500_change'] = round(sp500_change, 4)
            row['sp500_return'] = round(sp500_change / last_sp500_close, 8)
        last_sp500_close = sp500_close
        rows.append(row)

    return rows


def write_csv(rows, path):
    fieldnames = [
        'date',
        'wti',
        'brent',
        'spread',
        'spread_change',
        'sp500_close',
        'sp500_change',
        'sp500_return',
    ]
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_summary(rows):
    level_spread = [row['spread'] for row in rows]
    level_sp500 = [row['sp500_close'] for row in rows]
    change_rows = [row for row in rows if row['spread_change'] != '' and row['sp500_return'] != '']

    next_day_corr = None
    prev_day_corr = None
    if len(change_rows) >= 2:
        next_day_corr = pearson(
            [row['spread_change'] for row in change_rows[:-1]],
            [row['sp500_return'] for row in change_rows[1:]],
        )
        prev_day_corr = pearson(
            [row['spread_change'] for row in change_rows[1:]],
            [row['sp500_return'] for row in change_rows[:-1]],
        )

    return f"""# Brent/WTI Spread vs S&P 500

- Source series:
  - Brent/WTI prices from `all_data.js`
  - S&P 500 from FRED series `{SP500_SERIES_ID}`
- Overlap window: {rows[0]['date']} to {rows[-1]['date']}
- Overlap observations: {len(rows)}

## Correlations

- Spread level vs S&P 500 level: {format_corr(pearson(level_spread, level_sp500))}
- Daily spread change vs same-day S&P 500 return: {format_corr(pearson([row['spread_change'] for row in change_rows], [row['sp500_return'] for row in change_rows]))}
- Daily spread change vs next-day S&P 500 return: {format_corr(next_day_corr)}
- Daily spread change vs previous-day S&P 500 return: {format_corr(prev_day_corr)}

## Notes

- The Brent-WTI spread itself begins on 1987-05-20, but the public FRED daily S&P 500 series on this endpoint begins in 2016.
- `spread_change` is measured in dollars per barrel.
- `sp500_return` is a simple daily close-to-close return.
"""


def main():
    spread_rows = load_all_data_rows(DATA_PATH)
    sp500_series = fetch_fred_series(SP500_SERIES_ID, SP500_CACHE_PATH)
    rows = build_rows(spread_rows, sp500_series)
    if not rows:
        raise ValueError('No overlapping dates between spread data and S&P 500 data')

    write_csv(rows, OUTPUT_CSV_PATH)
    OUTPUT_SUMMARY_PATH.write_text(build_summary(rows))

    print(f'Wrote {len(rows)} rows to {OUTPUT_CSV_PATH.name}')
    print(f'Wrote summary to {OUTPUT_SUMMARY_PATH.name}')


if __name__ == '__main__':
    main()
