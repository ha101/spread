import ast
import csv
import subprocess
from io import StringIO
from pathlib import Path
import re


FRED_GRAPH_URL = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}'


def load_all_data_rows(path):
    match = re.search(r'=\s*(\[[\s\S]*\])\s*;\s*$', path.read_text())
    if match is None:
        raise ValueError(f'Could not parse spread dataset from {path}')
    return ast.literal_eval(match.group(1))


def write_all_data_rows(path, rows):
    lines = ['window.ALL_DATA = [']
    for index, (date, wti, brent) in enumerate(rows):
        suffix = ',' if index < len(rows) - 1 else ''
        lines.append(f'  ["{date}", {wti:.2f}, {brent:.2f}]{suffix}')
    lines.append('];')
    path.write_text('\n'.join(lines) + '\n')


def parse_fred_csv_text(text):
    reader = csv.DictReader(StringIO(text))
    series = {}
    value_field = reader.fieldnames[1] if reader.fieldnames and len(reader.fieldnames) > 1 else None
    if value_field is None:
        raise ValueError('FRED CSV is missing the value column')

    for row in reader:
        value = row[value_field]
        if value in (None, '', '.'):
            continue
        series[row['observation_date']] = float(value)

    if not series:
        raise ValueError('No observations were parsed from FRED CSV text')
    return series


def fetch_fred_series(series_id, cache_path=None):
    url = FRED_GRAPH_URL.format(series_id=series_id)
    text = None

    try:
        result = subprocess.run(
            ['curl', '-sS', url],
            check=True,
            capture_output=True,
            text=True,
        )
        text = result.stdout
        if cache_path is not None:
            cache_path.write_text(text)
    except subprocess.CalledProcessError:
        if cache_path is None or not Path(cache_path).exists():
            raise
        text = Path(cache_path).read_text()

    return parse_fred_csv_text(text)
