import csv
from datetime import datetime, timedelta
from io import StringIO
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    yf = None


# Yahoo Finance futures tickers for crude benchmarks.
TICKERS = {
    'wti': 'CL=F',
    'brent': 'BZ=F',
}


def fetch_yfinance_daily(ticker, start_date=None, cache_path=None):
    """Fetch daily close prices from Yahoo Finance.

    Returns a dict of {date_str: close_price}.
    Falls back to cache_path on failure.
    """
    if yf is None:
        raise ImportError('yfinance is not installed')

    if start_date is None:
        start_date = '2000-01-01'

    series = {}
    try:
        df = yf.download(
            ticker,
            start=start_date,
            interval='1d',
            auto_adjust=True,
            progress=False,
        )
        if df.empty:
            raise ValueError(f'No data returned for {ticker}')

        for date_index, row in df.iterrows():
            date_str = date_index.strftime('%Y-%m-%d')
            close = row['Close']
            if hasattr(close, 'item'):
                close = close.item()
            close = float(close)
            if close > 0:
                series[date_str] = round(close, 2)

        if cache_path is not None and series:
            _write_cache(cache_path, series)

    except Exception:
        if cache_path is not None and Path(cache_path).exists():
            series = _read_cache(cache_path)
        else:
            raise

    return series


def fetch_wti_and_brent(start_date=None, wti_cache=None, brent_cache=None):
    """Fetch both WTI and Brent daily series. Returns (wti_dict, brent_dict)."""
    wti = fetch_yfinance_daily(TICKERS['wti'], start_date, wti_cache)
    brent = fetch_yfinance_daily(TICKERS['brent'], start_date, brent_cache)
    return wti, brent


def _write_cache(path, series):
    lines = ['observation_date,value']
    for date_str in sorted(series):
        lines.append(f'{date_str},{series[date_str]:.2f}')
    Path(path).write_text('\n'.join(lines) + '\n')


def _read_cache(path):
    text = Path(path).read_text()
    reader = csv.DictReader(StringIO(text))
    series = {}
    for row in reader:
        value = row.get('value', '')
        if value in (None, '', '.'):
            continue
        series[row['observation_date']] = float(value)
    return series
