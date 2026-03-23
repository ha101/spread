import ast
import re
from datetime import datetime
from pathlib import Path

import matplotlib
import matplotlib.dates as mdates
import numpy as np

matplotlib.use('Agg')
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).with_name('all_data.js')
OUTPUT_PATH = Path(__file__).with_name('wti_brent_spread.png')


def parse_iso_date(value):
    return datetime.strptime(value, '%Y-%m-%d')


def load_rows(path):
    match = re.search(r'=\s*(\[[\s\S]*\])\s*;\s*$', path.read_text())
    if match is None:
        raise ValueError(f'Could not parse dataset from {path}')
    return ast.literal_eval(match.group(1))


def trailing_year(rows):
    latest_date = parse_iso_date(rows[-1][0])
    try:
        cutoff = latest_date.replace(year=latest_date.year - 1)
    except ValueError:
        cutoff = latest_date.replace(year=latest_date.year - 1, day=28)
    return [row for row in rows if parse_iso_date(row[0]) > cutoff]


rows = trailing_year(load_rows(DATA_PATH))
dates = [parse_iso_date(date) for date, _, _ in rows]
spreads = [brent - wti for _, wti, brent in rows]

fig, ax = plt.subplots(figsize=(14, 6))

# Color positive spread green, negative red
colors = ['#2ca02c' if spread >= 0 else '#d62728' for spread in spreads]
ax.bar(dates, spreads, width=1.5, color=colors, alpha=0.7, edgecolor='none')

# Add a zero line
ax.axhline(y=0, color='black', linewidth=0.5, linestyle='-')

# Moving average
window = 20
if len(spreads) >= window:
    ma = np.convolve(spreads, np.ones(window) / window, mode='valid')
    ma_dates = dates[window - 1:]
    ax.plot(ma_dates, ma, color='#1f77b4', linewidth=2, label=f'{window}-day MA')
    ax.legend(loc='upper left', fontsize=10)

ax.set_title('Brent – WTI Crude Oil Spread ($/bbl)', fontsize=16, fontweight='bold', pad=15)
ax.set_ylabel('Spread ($/bbl)', fontsize=12)
ax.set_xlabel('')

date_locator = mdates.AutoDateLocator(minticks=5, maxticks=8)
date_formatter = mdates.ConciseDateFormatter(date_locator)
date_formatter.formats = ['%Y', '%b %Y', '%b %d', '%H:%M', '%H:%M', '%S']
date_formatter.zero_formats = ['%Y', '%Y', '%b %Y', '%b %d', '%H:%M', '%S']
date_formatter.offset_formats = ['', '%Y', '%Y', '%Y-%b-%d', '%Y-%b-%d', '%Y-%b-%d %H:%M']
ax.xaxis.set_major_locator(date_locator)
ax.xaxis.set_major_formatter(date_formatter)
ax.tick_params(axis='x', labelrotation=0, pad=8)

ax.grid(axis='y', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Annotate key stats
avg_spread = np.mean(spreads)
min_spread = min(spreads)
max_spread = max(spreads)
current = spreads[-1]
ax.annotate(
    f'Current: ${current:.2f}',
    xy=(dates[-1], current),
    xytext=(-80, 20),
    textcoords='offset points',
    fontsize=9,
    color='#333',
    arrowprops=dict(arrowstyle='->', color='#666', lw=0.8),
)

# Add stats text box
stats_text = f'Avg: ${avg_spread:.2f}  |  Min: ${min_spread:.2f}  |  Max: ${max_spread:.2f}'
ax.text(0.5, -0.18, stats_text, transform=ax.transAxes, fontsize=10, ha='center', color='#555')

plt.tight_layout()
plt.savefig(OUTPUT_PATH, dpi=150, bbox_inches='tight')
plt.close()
print(f'Chart saved to {OUTPUT_PATH.name}')
