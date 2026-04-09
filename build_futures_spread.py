"""Build futures spread data for Brent-WTI at various tenors.

For each trading day, determines which CME contract represents N months out,
fetches Brent and WTI prices for that contract, and computes the spread.
Uses front-month continuous tickers (CL=F, BZ=F) for the 1m tenor.
Outputs futures_data.js for the website.
"""

from datetime import date, timedelta
from pathlib import Path

from yfinance_utils import (
    MONTH_CODES,
    fetch_futures_contract,
    fetch_yfinance_daily,
    _read_cache,
)

BASE_PATH = Path(__file__).parent
CACHE_DIR = BASE_PATH / 'futures_cache'
OUTPUT_PATH = BASE_PATH / 'futures_data.js'

TENORS = [1, 2, 3, 6, 12, 24]
TENOR_LABELS = ['1m', '2m', '3m', '6m', '12m', '24m']

# How far back to attempt fetching contracts.
START_YEAR = 2015


def contract_month_for_tenor(trading_date, tenor_months):
    """Given a trading date and a tenor in months, return (year, month) of the
    target contract.

    Convention: on any day in month M, the contract N months out is the one
    with delivery month M + N.  For example, on any day in April 2026 with
    tenor=1, the target is May 2026.
    """
    month = trading_date.month + tenor_months
    year = trading_date.year
    while month > 12:
        month -= 12
        year += 1
    return year, month


def enumerate_contracts(start_year, end_year):
    """Return a list of (year_2digit, month_index, month_code, full_year) for
    all contract months from start_year through end_year inclusive."""
    contracts = []
    for year in range(start_year, end_year + 1):
        y2 = year % 100
        for mi, code in enumerate(MONTH_CODES):
            contracts.append((y2, mi + 1, code, year))
    return contracts


def fetch_front_month_series():
    """Fetch front-month continuous contract data for WTI and Brent.

    Returns (wti_dict, brent_dict) where each is {date_str: price}.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    wti = fetch_yfinance_daily('CL=F', '2000-01-01', CACHE_DIR / 'CL_front.csv')
    brent = fetch_yfinance_daily('BZ=F', '2000-01-01', CACHE_DIR / 'BZ_front.csv')
    return wti, brent


def fetch_all_contracts(contracts):
    """Fetch WTI (CL) and Brent (BZ) prices for every contract in the list.

    Returns two dicts keyed by (full_year, month) -> {date_str: price}.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    wti_by_contract = {}
    brent_by_contract = {}

    for y2, month_num, code, full_year in contracts:
        key = (full_year, month_num)

        # Skip contracts that expired long ago (more than 2 months before today).
        contract_expiry_approx = date(full_year, month_num, 1)
        if contract_expiry_approx < date.today() - timedelta(days=60):
            # Only use cached data for expired contracts.
            wti_cache = CACHE_DIR / f'CL{code}{y2:02d}.csv'
            bz_cache = CACHE_DIR / f'BZ{code}{y2:02d}.csv'
            if wti_cache.exists():
                wti_by_contract[key] = _read_cache(wti_cache)
            if bz_cache.exists():
                brent_by_contract[key] = _read_cache(bz_cache)
            continue

        try:
            wti_by_contract[key] = fetch_futures_contract('CL', code, y2, CACHE_DIR)
        except Exception as exc:
            print(f'  Warning: CL{code}{y2:02d} fetch failed: {exc}')

        try:
            brent_by_contract[key] = fetch_futures_contract('BZ', code, y2, CACHE_DIR)
        except Exception as exc:
            print(f'  Warning: BZ{code}{y2:02d} fetch failed: {exc}')

    return wti_by_contract, brent_by_contract


def build_front_month_spread(wti_front, brent_front):
    """Build the 1m spread from continuous front-month tickers."""
    common_dates = sorted(set(wti_front) & set(brent_front))
    return [
        [d, round(brent_front[d] - wti_front[d], 2)]
        for d in common_dates
    ]


def build_tenor_series(wti_by_contract, brent_by_contract, tenor_months):
    """Build a daily spread series for a given tenor.

    Returns a sorted list of [date_str, spread_value].
    """
    # Collect all trading dates from all contracts.
    all_dates = set()
    for series in list(wti_by_contract.values()) + list(brent_by_contract.values()):
        all_dates.update(series.keys())

    rows = []
    for date_str in sorted(all_dates):
        parts = date_str.split('-')
        if len(parts) != 3:
            continue
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
        try:
            trading_date = date(y, m, d)
        except ValueError:
            continue

        target_year, target_month = contract_month_for_tenor(trading_date, tenor_months)
        key = (target_year, target_month)

        wti_price = wti_by_contract.get(key, {}).get(date_str)
        brent_price = brent_by_contract.get(key, {}).get(date_str)

        if wti_price is not None and brent_price is not None:
            spread = round(brent_price - wti_price, 2)
            rows.append([date_str, spread])

    return rows


def format_js_rows(rows):
    """Format rows as a JS array string."""
    lines = ['[']
    for i, row in enumerate(rows):
        suffix = ',' if i < len(rows) - 1 else ''
        lines.append(f'    ["{row[0]}", {row[1]:.2f}]{suffix}')
    lines.append('    ]')
    return '\n'.join(lines)


def write_output(tenor_rows):
    """Write futures_data.js."""
    parts = ['window.FUTURES_DATA = {']
    labels = ', '.join(f'"{t}"' for t in TENOR_LABELS)
    parts.append(f'  tenors: [{labels}],')

    for label, rows in zip(TENOR_LABELS, tenor_rows):
        parts.append(f'  "{label}": {{')
        parts.append(f'    rows: {format_js_rows(rows)},')
        parts.append('  },')

    parts.append('};')
    parts.append('')
    OUTPUT_PATH.write_text('\n'.join(parts))


def main():
    today = date.today()
    end_year = today.year + 2
    contracts = enumerate_contracts(START_YEAR, end_year)
    print(f'Enumerating {len(contracts)} contract months from {START_YEAR} to {end_year}')

    print('Fetching front-month continuous data...')
    wti_front, brent_front = fetch_front_month_series()
    print(f'  CL=F: {len(wti_front)} days, BZ=F: {len(brent_front)} days')

    print('Fetching individual contract data...')
    wti_by_contract, brent_by_contract = fetch_all_contracts(contracts)
    print(f'  WTI contracts with data: {len(wti_by_contract)}')
    print(f'  Brent contracts with data: {len(brent_by_contract)}')

    tenor_rows = []
    for tenor, label in zip(TENORS, TENOR_LABELS):
        if tenor == 1:
            rows = build_front_month_spread(wti_front, brent_front)
        else:
            rows = build_tenor_series(wti_by_contract, brent_by_contract, tenor)
        tenor_rows.append(rows)
        if rows:
            print(f'  {label}: {len(rows)} days ({rows[0][0]} to {rows[-1][0]})')
        else:
            print(f'  {label}: 0 days')

    write_output(tenor_rows)
    print(f'Wrote {OUTPUT_PATH.name}')


if __name__ == '__main__':
    main()
