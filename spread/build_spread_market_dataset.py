import csv
import math
from pathlib import Path

from fred_series_utils import fetch_fred_series, load_all_data_rows


BASE_PATH = Path(__file__).parent
SPREAD_PATH = BASE_PATH / 'all_data.js'
OUTPUT_CSV_PATH = BASE_PATH / 'spread_vs_market_indexes.csv'
OUTPUT_SUMMARY_PATH = BASE_PATH / 'spread_vs_market_summary.md'
OUTPUT_COMPLETE_CSV_PATH = BASE_PATH / 'spread_vs_market_indexes_complete.csv'
OUTPUT_COMPLETE_SUMMARY_PATH = BASE_PATH / 'spread_vs_market_complete_summary.md'

SERIES = {
    'sp500': {
        'label': 'S&P 500',
        'series_id': 'SP500',
        'cache_path': BASE_PATH / 'sp500_fred.txt',
    },
    'nasdaq': {
        'label': 'Nasdaq Composite',
        'series_id': 'NASDAQCOM',
        'cache_path': BASE_PATH / 'nasdaqcom_fred.txt',
    },
    'djia': {
        'label': 'Dow Jones Industrial Average',
        'series_id': 'DJIA',
        'cache_path': BASE_PATH / 'djia_fred.txt',
    },
    'vix': {
        'label': 'VIX',
        'series_id': 'VIXCLS',
        'cache_path': BASE_PATH / 'vixcls_fred.txt',
    },
}


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


def build_rows(spread_rows, market_series):
    rows = []
    last_closes = {key: None for key in market_series}

    for date, wti, brent in spread_rows:
        row = {
            'date': date,
            'wti': round(float(wti), 2),
            'brent': round(float(brent), 2),
            'spread': round(float(brent) - float(wti), 2),
            'spread_change': '',
        }

        if rows:
            row['spread_change'] = round(row['spread'] - rows[-1]['spread'], 4)

        for key, values in market_series.items():
            close_key = f'{key}_close'
            change_key = f'{key}_change'
            return_key = f'{key}_return'
            close = values.get(date)

            if close is None:
                row[close_key] = ''
                row[change_key] = ''
                row[return_key] = ''
                continue

            row[close_key] = close
            previous_close = last_closes[key]
            if previous_close is None:
                row[change_key] = ''
                row[return_key] = ''
            else:
                change = close - previous_close
                row[change_key] = round(change, 4)
                row[return_key] = round(change / previous_close, 8)
            last_closes[key] = close

        rows.append(row)

    return rows


def write_csv(rows, path, market_keys):
    fieldnames = ['date', 'wti', 'brent', 'spread', 'spread_change']
    for key in market_keys:
        fieldnames.extend([f'{key}_close', f'{key}_change', f'{key}_return'])

    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_complete_case_rows(rows, market_keys):
    complete_rows = []

    for source_row in rows:
        if any(source_row[f'{key}_close'] == '' for key in market_keys):
            continue

        row = {
            'date': source_row['date'],
            'wti': source_row['wti'],
            'brent': source_row['brent'],
            'spread': source_row['spread'],
            'spread_change': '',
        }

        for key in market_keys:
            row[f'{key}_close'] = source_row[f'{key}_close']
            row[f'{key}_change'] = ''
            row[f'{key}_return'] = ''

        if complete_rows:
            previous_row = complete_rows[-1]
            row['spread_change'] = round(row['spread'] - previous_row['spread'], 4)

            for key in market_keys:
                close_key = f'{key}_close'
                change_key = f'{key}_change'
                return_key = f'{key}_return'
                change = row[close_key] - previous_row[close_key]
                row[change_key] = round(change, 4)
                row[return_key] = round(change / previous_row[close_key], 8)

        complete_rows.append(row)

    return complete_rows


def build_summary(rows, series_meta, title, notes):
    lines = [
        f'# {title}',
        '',
        f'- Spread window: {rows[0]["date"]} to {rows[-1]["date"]}',
        f'- Spread observations: {len(rows)}',
        '',
        '## Correlations By Series',
        '',
    ]

    for key, meta in series_meta.items():
        close_key = f'{key}_close'
        return_key = f'{key}_return'
        available_rows = [row for row in rows if row[close_key] != '']
        available_change_rows = [
            row for row in available_rows
            if row['spread_change'] != '' and row[return_key] != ''
        ]

        level_corr = pearson(
            [row['spread'] for row in available_rows],
            [row[close_key] for row in available_rows],
        )
        same_day_corr = pearson(
            [row['spread_change'] for row in available_change_rows],
            [row[return_key] for row in available_change_rows],
        )

        next_day_corr = None
        if len(available_change_rows) >= 2:
            next_day_corr = pearson(
                [row['spread_change'] for row in available_change_rows[:-1]],
                [row[return_key] for row in available_change_rows[1:]],
            )

        lines.extend([
            f'### {meta["label"]}',
            '',
            f'- Overlap window: {available_rows[0]["date"]} to {available_rows[-1]["date"]}',
            f'- Overlap observations: {len(available_rows)}',
            f'- Level correlation: {format_corr(level_corr)}',
            f'- Same-day return correlation: {format_corr(same_day_corr)}',
            f'- Next-day return correlation: {format_corr(next_day_corr)}',
            '',
        ])

    lines.extend([
        '## Notes',
        '',
        *notes,
    ])
    return '\n'.join(lines) + '\n'


def main():
    spread_rows = load_all_data_rows(SPREAD_PATH)
    market_series = {
        key: fetch_fred_series(meta['series_id'], meta['cache_path'])
        for key, meta in SERIES.items()
    }
    rows = build_rows(spread_rows, market_series)
    complete_rows = build_complete_case_rows(rows, SERIES.keys())

    write_csv(rows, OUTPUT_CSV_PATH, SERIES.keys())
    OUTPUT_SUMMARY_PATH.write_text(build_summary(
        rows,
        SERIES,
        'Brent/WTI Spread vs Market Indexes',
        [
            '- The Brent-WTI spread itself only begins on 1987-05-20, the earliest official FRED overlap for the two spot benchmarks.',
            '- S&P 500 and DJIA daily FRED series available on this endpoint begin in 2016; Nasdaq begins in 1971 and VIX in 1990.',
            '- Blank market cells in the CSV indicate that the benchmark exists in the spread window but the selected market series does not.',
        ],
    ))
    write_csv(complete_rows, OUTPUT_COMPLETE_CSV_PATH, SERIES.keys())
    OUTPUT_COMPLETE_SUMMARY_PATH.write_text(build_summary(
        complete_rows,
        SERIES,
        'Brent/WTI Spread vs Market Indexes (Complete Case)',
        [
            '- This file keeps only rows where S&P 500, Nasdaq, DJIA, and VIX all have closes on the same date.',
            '- Spread, market changes, and market returns are recomputed against the previous retained complete-case row so the panel stays aligned.',
            '- In practice, this yields the shared four-index window beginning on 2016-03-21 and excludes dates like 2018-12-05 and the spread-only tail on 2026-03-23.',
        ],
    ))

    print(f'Wrote {len(rows)} rows to {OUTPUT_CSV_PATH.name}')
    print(f'Wrote summary to {OUTPUT_SUMMARY_PATH.name}')
    print(f'Wrote {len(complete_rows)} rows to {OUTPUT_COMPLETE_CSV_PATH.name}')
    print(f'Wrote summary to {OUTPUT_COMPLETE_SUMMARY_PATH.name}')


if __name__ == '__main__':
    main()
