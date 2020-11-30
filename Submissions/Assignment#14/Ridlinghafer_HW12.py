# %%
import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.style.use('seaborn')
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
%matplotlib inline

# %%
def read_input_file(filepath):
    """Reads in the input files located by the filepath <str> argument and returns a parsed dataframe."""
    
    frame = pd.read_csv(filepath)
    frame['Date'] = pd.to_datetime(frame['Date'], format='%d-%m-%Y')
    frame = frame.sort_values('Date', ascending=True).reset_index(drop=True)
    return frame
# %%
reservoir_levels = read_input_file(r'../../data/HW_14/chennai_reservoir_levels.csv')
rainfall = read_input_file(r'../../data/HW_14/chennai_reservoir_rainfall.csv')

# %%
def assign_temporal_categories(date):
    """Given a date, determines whether to color for 'Monsoon', 'Dry', or 'Regular' season."""
    
    if date.month in [2, 3, 4, 5] or date.month == 6 and date.day <= 15:
        return colors[2]
    elif date.month in [10, 11, 12]:
        return colors[1]
    else:
        return colors[0]

# Plot the reservoir levels per day summed across all 4 reservoirs
c = reservoir_levels['Date'].apply(assign_temporal_categories, colors)
chennai_reservoirs = reservoir_levels.iloc[:, 1:].sum(axis=1)

plt.figure(figsize=(16, 8))
plt.scatter(reservoir_levels['Date'].values, chennai_reservoirs, color=c, alpha=0.3)
plt.ylabel('Reservoir Levels Across Chennai (mcft)', size=14)
plt.xlabel('Date', size=14)
legend_labels = {'Normal Season':colors[0], 'Monsoon Season':colors[1], 'Dry Season':colors[2]}
leg_el = [mpatches.Patch(facecolor=value, edgecolor='k', label=key) for key, value in legend_labels.items()]
plt.legend(handles=leg_el, prop={'size':14})
plt.title('Reservoir Levels in Chennai per Day', size=16)

# %%
# Replace parts of url with variables
site = '09506000'
start = '2020-08-22'
end = '2020-11-28'  # Update end date each week to Saturday

url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + \
    site + "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + \
    end
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                              'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])

# %%
# Aggregate flow values to weekly
flow_weekly = data.resample("W-SAT", on='datetime').mean()

# %%
Jacob_pred = pd.read_csv(r'../../data/ridlinghaver.csv')
# %%
for i in range(1, 2):
    flow_weekly['flow_tm%s' % i] = flow_weekly['flow'].shift(i)
# %%
# finds the weekly percent change
pch = []
for i in range(2,len(flow_weekly)):
    pch.append((flow_weekly['flow'][i]-flow_weekly['flow_tm1'][i])/flow_weekly['flow_tm1'][i])


# %%
# Importing the statistics module 
import statistics

meanch = statistics.mean(pch) 
# print(mean(pch))
# %%
wk1 = flow_weekly['flow'][14] + flow_weekly['flow'][14] * meanch
wk2 = wk1 + wk1 * meanch
# %%
