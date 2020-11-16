
# %%
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset

# %%
# Net CDF file historical time series
data_path = os.path.join('../../data',
                         'rain.nc')

# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
# shows prate is parameter of interest
dataset
# %%
# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata

# %%
# shows the list of values
dataset['prate']['lat'].values
dataset['prate']['lon'].values

# %%
# Now lets take a slice: Grabbing data for just one point
# 34.56, 248.15
lat = dataset["prate"]["lat"].values[28]
lon = dataset["prate"]["lon"].values[132]
print("Long, Lat values:", lon, lat)
# %%
precip = dataset["prate"].sel(lat=lat,lon=lon)
precip.shape

# use x-array to plot timeseries
precip.plot.line()
precip_val = precip.values

# Convert to dataframe
precip = precip.to_dataframe()

# converts to inches/day
precip['prate'] = precip['prate'] * 86400 / 25.4


# %%
# Second dataset
# %%
# Net CDF file historical time series
data_path = os.path.join('../../data',
                         'temp2.nc')

# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
# look at it shows that air is parameter of interest
dataset
# %%

# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata

# %%
# Now to grab out data first lets look at spatail coordinates:
dataset['tmax']['lat'].values.shape
# The first 4 lat values
# %%
dataset['tmax']['lat'].values
dataset['tmax']['lon'].values
# %%

# 248.15, 34.56
# Now lets take a slice: Grabbing data for just one point
lat = dataset["tmax"]["lat"].values[10]
lon = dataset["tmax"]["lon"].values[96]
print("Long, Lat values:", lon, lat)
# %%
temp = dataset["tmax"].sel(lat=lat,lon=lon)

# use x-array to plot timeseries
temp.plot.line()
precip_val = temp.values

#Conver to dataframe
temp = temp.to_dataframe()

# converts to celcius
temp['tmax'] = temp['tmax']
# %%

# %%
# Step 1: Import USGS flow data

# Replace parts of url with variables
site = '09506000'
start = '2015-01-01'
end = '2020-11-11'  # Update end date each week to Saturday

url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + \
    site + "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + \
    end
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                              'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])
# %%
data = data.reset_index(drop=True)
precip = precip.reset_index(drop=True)
temp = temp.reset_index(drop=True)
data = data.join(precip['prate'])
data = data.join(temp['tmax'])
# %%
info = [data['datetime'], data["flow"], temp["tmax"], precip['prate']]

headers = ['datetime', "flow", "temp", "precip"]

data2 = pd.concat(info, axis=1, keys=headers)
pd.to_datetime(data2['datetime'])

data2['year'] = pd.DatetimeIndex(data2['datetime']).year
data2['month'] = pd.DatetimeIndex(data2['datetime']).month
data2['day'] = pd.DatetimeIndex(data2['datetime']).day
# %%
# Aggregate flow values to weekly
flow_weekly = data2.resample("W-SAT", on='datetime').mean()
flow_weekly = flow_weekly[(flow_weekly.flow <= 345)]
# %%
for i in range(1, 4):
    flow_weekly['flow_tm%s' % i] = flow_weekly['flow'].shift(i)
# done for temp as well
for i in range(1, 3):
    flow_weekly['temp%s' % i] = flow_weekly['temp'].shift(i)
# done for temp as well
for i in range(1, 3):
    flow_weekly['precip%s' % i] = flow_weekly['precip'].shift(i)

# %%
from sklearn.linear_model import LinearRegression
import numpy as np
# %%
# used this to see how data from this month has behaved in last 5 years
descibe = data2.flow[(data2['month'] == 11) & (data2['day'] > 15)].min()
# %%
train = flow_weekly[3:-12][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3',
                               'precip', 'temp',
                               'temp1', 'precip1']]

# Next create regression model based on training period above
model4 = LinearRegression()
y = train['flow'].values
x4 = train[['flow_tm1', 'flow_tm2', 'flow_tm3',
            'precip', 'temp']]#, 'temp1']]
model4.fit(x4, y)
r_sq = model4.score(x4, y)

# Print model parameters and r2
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model4.intercept_, 2))
print('slope:', np.round(model4.coef_, 2))

# %%
# projecting 2 weeks into the future using 4 time lags
# lists that start with the 4 most recent entries
T = [25.79,20]
T2 = [16.53, 25.79]
P = [0,0]
lastweekx3 = [flow_weekly.flow[-3]]
lastweekx2 = [flow_weekly.flow[-2]]
lastweek = [flow_weekly.flow[-1]]
# empty list for predictions
weeklypred_4 = []

for i in range(2):
    wk1 = lastweek[i]
    wk2 = lastweekx2[i]
    wk3 = lastweekx3[i]
    wk4 = P[i]
    # appends to last week so that they refer to next time step
    lastweekx2.append(wk1)
    lastweekx3.append(wk2)
        # the prediction for week # i
    prediction = model4.intercept_ + model4.coef_[0] * wk1 + model4.coef_[1] \
        * wk2 + model4.coef_[2] * wk4 + model4.coef_[3] * wk4 + T[i] * model4.coef_[4]
    lastweek.append(prediction)
    # creates a list of just my predictions for week 1 then week 2
    weeklypred_4.append(prediction)
print(np.round(weeklypred_4, 2))

# %%
weeklytemp = []
for i in range(8, 13):
    if i < 11:
        q = 0.9
    else: q = 0.4
    weeklytemp.append(data2['temp'][(data2['month'] == i)
                                    & (data2['day'] <= 7)].quantile(q))
    weeklytemp.append(data2['temp'][(data2['month'] == i) & (data2['day'] > 7) &
                                           (data2['day'] <= 14)].quantile(q))
    weeklytemp.append(data2['temp'][(data2['month'] == i) & (data2['day'] > 14)
                                           & (data2['day'] <= 21)].quantile(q))
    weeklytemp.append(data2['temp'][(data2['month'] == i)
                                           & (data2['day'] >= 22)].quantile(q))
weeklytemp = weeklytemp[3:19]

# copied then temp 1 week prior to semester start
# is inserted at begining of list
weeklytemp2 = weeklytemp.copy()
weeklytemp2[0:0] = [41.2]

# rounding
weeklytemp = np.round(weeklytemp, decimals=2)
weeklytemp2 = np.round(weeklytemp, decimals=2)
# %%
# adjusting model for 16 week prediction 
# removed 1 precip lag and 1 flow lag
model4 = LinearRegression()
y = train['flow'].values
x4 = train[['flow_tm1', 'flow_tm2',
            'precip', 'temp', 'temp1']]
model4.fit(x4, y)
r_sq = model4.score(x4, y)
# %%
# data2[(data2['prcp (mm/day)'] > 0) & (data.year > 2010)].mean()
# projecting 16 weeks into the future
# The + 8 is added to start at 8/21

lastweekx3 = [0]
lastweekx2 = [flow_weekly.flow[-(2 + 12)]]
lastweek = [flow_weekly.flow[-(1 + 12)]]
weeklypred = []
for i in range(16):
    wk1 = lastweek[i]
    wk2 = lastweekx2[i]
    wk3 = lastweekx3[i]
    wk4 = weeklytemp[i]
    wk5 = weeklytemp2[i]
    lastweekx2.append(wk1)
    lastweekx3.append(0)
    # added a bernoulli variable multiplied by 10 mm
    # this way rain could impact the model
    prediction = model4.intercept_ + model4.coef_[0] * wk1 + model4.coef_[1] \
        * wk2 + model4.coef_[2] * wk3 + model4.coef_[3] * wk4 + model4.coef_[4] * wk5
    lastweek.append(prediction)
    weeklypred.append(prediction)
print(np.round(weeklypred, 2))
# %%
# shows a plot of 16 week prediction
# creates unique name list of each week from 1 to 16
weeks = []
for i in range(16):
    weeks.append('week# ' '%s' % (i+1))
# creates a plot of my prediction for each week of the semester

plt.style.use('seaborn-whitegrid')


plt.scatter(x=weeks, y=weeklypred, marker='o', label='predicted flow')
plt.scatter(x=weeks[0:11],
            y=flow_weekly.flow[(flow_weekly['year'] == 2020)
            & (flow_weekly['month'] >= 8) & (flow_weekly['day'] >= 20) |
            (flow_weekly['year'] == 2020) & (flow_weekly['month'] >= 9)],
            marker='o', label='observed')

plt.ylabel('Flow (cfs)')
plt.ylim([0, 200])
plt.title('Weekly Discharge Prediction')
plt.xticks(rotation=45, fontsize=10)
plt.legend()
plt.savefig('Discharge_Prediction.png')

# %%
monthlytemp = []
for i in range(8, 13):
    monthlytemp.append(data2['temp'][(data2['month'] == i)])

#%%
data_to_plot = [monthlytemp[0], monthlytemp[1], monthlytemp[2], monthlytemp[3], monthlytemp[4]]
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.ylim([0, 50])
plt.title('Monthly Temp Boxplot')
ax.set_xticklabels(['August', 'Sept', 'Oct', 'Nov', 'Dec'])
plt.xticks(rotation=45,fontsize=12)
fig.savefig('BoxPlots.png', bbox_inches='tight')


# %%
