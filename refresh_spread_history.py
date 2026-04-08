from pathlib import Path

from fred_series_utils import fetch_fred_series, load_all_data_rows, write_all_data_rows


BASE_PATH = Path(__file__).parent
ALL_DATA_PATH = BASE_PATH / 'all_data.js'
WTI_CACHE_PATH = BASE_PATH / 'wti_fred.csv'
BRENT_CACHE_PATH = BASE_PATH / 'brent_fred.csv'


def merge_official_history_with_local_overrides():
    existing_rows = load_all_data_rows(ALL_DATA_PATH) if ALL_DATA_PATH.exists() else []
    existing_by_date = {
        date: (float(wti), float(brent))
        for date, wti, brent in existing_rows
    }

    wti_series = fetch_fred_series('DCOILWTICO', WTI_CACHE_PATH)
    brent_series = fetch_fred_series('DCOILBRENTEU', BRENT_CACHE_PATH)

    common_dates = sorted(date for date in wti_series if date in brent_series)
    if not common_dates:
        raise ValueError('No overlapping Brent and WTI dates were fetched from FRED')

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
    print(f'Latest official overlap from FRED: {latest_official}')
    if latest_local is not None:
        print(f'Preserved local override tail through: {latest_local}')
    else:
        print('No local override tail beyond the official FRED overlap')


if __name__ == '__main__':
    main()
