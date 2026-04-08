from pathlib import Path

from fred_series_utils import fetch_fred_series, load_all_data_rows, write_all_data_rows

try:
    from yfinance_utils import fetch_wti_and_brent
    HAS_YFINANCE = True
except ImportError:
    HAS_YFINANCE = False


BASE_PATH = Path(__file__).parent
ALL_DATA_PATH = BASE_PATH / 'all_data.js'
WTI_CACHE_PATH = BASE_PATH / 'wti_fred.csv'
BRENT_CACHE_PATH = BASE_PATH / 'brent_fred.csv'
WTI_YF_CACHE_PATH = BASE_PATH / 'wti_yf.csv'
BRENT_YF_CACHE_PATH = BASE_PATH / 'brent_yf.csv'


def fetch_fred_daily():
    """Fetch daily WTI and Brent from FRED. Returns (wti_dict, brent_dict)."""
    wti = fetch_fred_series('DCOILWTICO', WTI_CACHE_PATH)
    brent = fetch_fred_series('DCOILBRENTEU', BRENT_CACHE_PATH)
    return wti, brent


def fetch_yf_daily():
    """Fetch daily WTI and Brent from Yahoo Finance. Returns (wti_dict, brent_dict)."""
    return fetch_wti_and_brent(
        start_date='2000-01-01',
        wti_cache=WTI_YF_CACHE_PATH,
        brent_cache=BRENT_YF_CACHE_PATH,
    )


def merge_sources(fred_wti, fred_brent, yf_wti, yf_brent):
    """Merge FRED historical data with yfinance for recent days.

    FRED is treated as authoritative where available.
    yfinance fills in any dates beyond FRED's latest.
    """
    wti = dict(fred_wti)
    brent = dict(fred_brent)

    for date, price in yf_wti.items():
        if date not in wti:
            wti[date] = price

    for date, price in yf_brent.items():
        if date not in brent:
            brent[date] = price

    return wti, brent


def merge_official_history_with_local_overrides():
    existing_rows = load_all_data_rows(ALL_DATA_PATH) if ALL_DATA_PATH.exists() else []
    existing_by_date = {
        date: (float(wti), float(brent))
        for date, wti, brent in existing_rows
    }

    fred_wti, fred_brent = fetch_fred_daily()

    if HAS_YFINANCE:
        try:
            yf_wti, yf_brent = fetch_yf_daily()
            print(f'yfinance returned {len(yf_wti)} WTI and {len(yf_brent)} Brent rows')
        except Exception as err:
            print(f'yfinance fetch failed ({err}), using FRED only')
            yf_wti, yf_brent = {}, {}
    else:
        print('yfinance not installed, using FRED only')
        yf_wti, yf_brent = {}, {}

    wti_series, brent_series = merge_sources(fred_wti, fred_brent, yf_wti, yf_brent)

    common_dates = sorted(date for date in wti_series if date in brent_series)
    if not common_dates:
        raise ValueError('No overlapping Brent and WTI dates found')

    merged_rows = [
        [date, round(wti_series[date], 2), round(brent_series[date], 2)]
        for date in common_dates
    ]

    latest_official_date = common_dates[-1]
    local_tail_dates = sorted(date for date in existing_by_date if date > latest_official_date)
    for date in local_tail_dates:
        wti, brent = existing_by_date[date]
        merged_rows.append([date, round(wti, 2), round(brent, 2)])

    return merged_rows, common_dates[0], latest_official_date, local_tail_dates[-1] if local_tail_dates else None


def main():
    rows, earliest_overlap, latest_official, latest_local = merge_official_history_with_local_overrides()
    write_all_data_rows(ALL_DATA_PATH, rows)

    print(f'Wrote {len(rows)} spread rows to {ALL_DATA_PATH.name}')
    print(f'Earliest official Brent/WTI overlap: {earliest_overlap}')
    print(f'Latest data point: {latest_official}')
    if latest_local is not None:
        print(f'Preserved local override tail through: {latest_local}')
    else:
        print('No local override tail beyond official sources')


if __name__ == '__main__':
    main()
