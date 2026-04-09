"""Fetch OPEC Reference Basket monthly prices from countryeconomy.com.

The page embeds a Google Charts dataMT array with monthly averages going
back to 2003.  We parse that array with a regex, merge with any existing
CSV cache, and write the result back so no historical data is ever lost.

Uses only the Python standard library (no requests / beautifulsoup).
"""

import csv
import re
import sys
import urllib.request
from pathlib import Path

BASE_PATH = Path(__file__).parent
CSV_PATH = BASE_PATH / 'opec_basket.csv'
URL = 'https://countryeconomy.com/raw-materials/opec'

USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
)


def fetch_page(url):
    """Fetch the HTML page content."""
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='replace')


def parse_opec_prices(html):
    """Extract (date_str, usd_price) pairs from the embedded JS dataMT array.

    The data lives inside a function like f_chartI() and looks like:
        {c:[{v:new Date(2026,3,1)},{v:117.33},{v:101.51}]}
    Month is 0-indexed in JavaScript Date().
    """
    # Find the dataMT array block
    pattern = re.compile(
        r'\{c:\[\{v:new Date\((\d{4}),(\d{1,2}),(\d{1,2})\)\},\{v:([\d.]+)\}',
        re.DOTALL,
    )

    rows = {}
    for match in pattern.finditer(html):
        year = int(match.group(1))
        month = int(match.group(2)) + 1  # JS months are 0-indexed
        day = int(match.group(3))
        price = float(match.group(4))
        date_str = f'{year:04d}-{month:02d}-{day:02d}'
        rows[date_str] = price

    return rows


def load_existing_csv(path):
    """Load the cached CSV into {date_str: price}."""
    data = {}
    if not path.exists():
        return data
    with open(path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if not header:
            return data
        for row in reader:
            if len(row) >= 2 and row[1].strip() not in ('', '.'):
                try:
                    data[row[0]] = round(float(row[1]), 2)
                except ValueError:
                    pass
    return data


def write_csv(path, data):
    """Write {date_str: price} to CSV, sorted by date."""
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['observation_date', 'OPEC_BASKET'])
        for date_str in sorted(data.keys()):
            writer.writerow([date_str, f'{data[date_str]:.2f}'])


def main():
    existing = load_existing_csv(CSV_PATH)
    existing_count = len(existing)

    try:
        html = fetch_page(URL)
        scraped = parse_opec_prices(html)
    except Exception as e:
        if existing_count > 0:
            print(f'WARNING: Fetch failed ({e}), keeping {existing_count} cached rows.')
            return
        else:
            print(f'ERROR: Fetch failed ({e}) and no cache exists.')
            sys.exit(1)

    if not scraped:
        if existing_count > 0:
            print(f'WARNING: No data parsed from page, keeping {existing_count} cached rows.')
            return
        else:
            print('ERROR: No data parsed and no cache exists.')
            sys.exit(1)

    # Merge: existing data takes precedence, scraped fills in new dates
    merged = {**scraped, **existing}

    new_count = len(merged) - existing_count
    write_csv(CSV_PATH, merged)
    print(f'OPEC basket: {len(merged)} rows total ({new_count} new) → {CSV_PATH.name}')


if __name__ == '__main__':
    main()
