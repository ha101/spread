import csv
from pathlib import Path

from fred_series_utils import fetch_fred_series, load_all_data_rows


BASE_PATH = Path(__file__).parent
OPEC_CSV_PATH = BASE_PATH / 'opec_basket.csv'
DAILY_SPREAD_PATH = BASE_PATH / 'all_data.js'
MONTHLY_SERIES = {
    'wti': {
        'series_id': 'MCOILWTICO',
        'cache_path': BASE_PATH / 'wti_monthly_fred.csv',
    },
    'brent': {
        'series_id': 'MCOILBRENTEU',
        'cache_path': BASE_PATH / 'brent_monthly_fred.csv',
    },
    'dubai': {
        'series_id': 'POILDUBUSDM',
        'cache_path': BASE_PATH / 'dubai_monthly_fred.csv',
    },
}
OUTPUT_PATH = BASE_PATH / 'benchmark_data.js'


def rounded_or_none(value):
    return None if value is None else round(float(value), 2)


def load_opec_basket_series(path):
    """Load OPEC basket CSV into {date_str: float}, matching FRED dict format."""
    data = {}
    if not path.exists():
        print(f'WARNING: {path.name} not found, OPEC basket will be empty')
        return data
    with open(path, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if len(row) >= 2 and row[1].strip() not in ('', '.'):
                try:
                    data[row[0]] = float(row[1])
                except ValueError:
                    pass
    return data


def load_monthly_series():
    series = {
        key: fetch_fred_series(meta['series_id'], meta['cache_path'])
        for key, meta in MONTHLY_SERIES.items()
    }
    series['opec'] = load_opec_basket_series(OPEC_CSV_PATH)
    return series


def build_daily_rows():
    return [
        [date, round(float(wti), 2), round(float(brent), 2)]
        for date, wti, brent in load_all_data_rows(DAILY_SPREAD_PATH)
    ]


def build_monthly_rows(series_by_key):
    all_dates = sorted(set().union(*[set(series) for series in series_by_key.values()]))
    rows = []

    for date in all_dates:
        wti = series_by_key['wti'].get(date)
        brent = series_by_key['brent'].get(date)
        dubai = series_by_key['dubai'].get(date)
        opec = series_by_key.get('opec', {}).get(date)

        # Keep months where at least two benchmarks exist so every retained row can form a spread.
        if sum(value is not None for value in (wti, brent, dubai, opec)) < 2:
            continue

        rows.append([
            date,
            rounded_or_none(wti),
            rounded_or_none(brent),
            rounded_or_none(dubai),
            rounded_or_none(opec),
        ])

    return rows


def format_js_value(value):
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f'"{value}"'
    return f'{value:.2f}'


def format_rows(rows):
    lines = ['[']
    for index, row in enumerate(rows):
        suffix = ',' if index < len(rows) - 1 else ''
        rendered = ', '.join(format_js_value(value) for value in row)
        lines.append(f'    [{rendered}]{suffix}')
    lines.append('  ]')
    return '\n'.join(lines)


def write_output(daily_rows, monthly_rows):
    contents = [
        'window.BENCHMARK_DATA = {',
        '  benchmarkLabels: {',
        '    wti: "WTI",',
        '    brent: "Brent",',
        '    dubai: "Dubai",',
        '    opec: "OPEC Basket",',
        '  },',
        '  daily: {',
        '    frequency: "daily",',
        '    columns: ["wti", "brent"],',
        f'    rows: {format_rows(daily_rows)},',
        '  },',
        '  monthly: {',
        '    frequency: "monthly",',
        '    columns: ["wti", "brent", "dubai", "opec"],',
        f'    rows: {format_rows(monthly_rows)},',
        '  },',
        '};',
        '',
    ]
    OUTPUT_PATH.write_text('\n'.join(contents))


def main():
    monthly_series = load_monthly_series()
    daily_rows = build_daily_rows()
    monthly_rows = build_monthly_rows(monthly_series)
    write_output(daily_rows, monthly_rows)

    print(f'Wrote {len(daily_rows)} daily rows and {len(monthly_rows)} monthly rows to {OUTPUT_PATH.name}')


if __name__ == '__main__':
    main()
