import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

df = pd.read_csv(r'sun_power.csv', parse_dates=['sampled'])
df['date'] = df['sampled'].dt.date

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)

data = df.groupby([df['date'], df['sampled'].dt.hour])['solar_kw'].mean()
zeroLine = np.zeros(24)  # 24 assumes "hour" above

# Generate line plots
lines = []
i = 0
for row_date in reversed(df.date.unique()):
    # Small reduction of the X extents to get a cheap perspective effect
    xscale = 1 - i / 500.
    # Same for linewidth (thicker strokes on bottom)
    lw = 1.5 - i / 200.0
    series = pd.Series(zeroLine)  # data is sparse, fill with zeroes
    line_data = data[row_date].combine(series, max, fill_value=0)
    X = np.linspace(-1, 1, line_data.shape[-1])
    line, = ax.plot(xscale * X, i + line_data * 4, color="w", lw=lw)
    lines.append(line)
    i += 1

# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 365)

ax.set_xticks([]) # No ticks
ax.set_yticks([])
ax.set_ylabel("Dag på året")
ax.set_xlabel("Tid på dagen")
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

ax.text(0.5, 1.0, "Solcellsproduktion 2021, effekt (kw)", transform=ax.transAxes,
        ha="center", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=14)

plt.draw()
# plt.savefig('sun_plot.svg', dpi=600)
plt.savefig('sun_plot.png', dpi=600)
plt.show()
