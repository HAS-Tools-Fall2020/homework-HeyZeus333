# %%
# Import the modules we will use

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import scipy
from scipy.stats import bernoulli

# %%                     )
#Replace parts of my url with variables 
site = '09506000'
start = '1989-01-01'
end = '2020-10-31'
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                      parse_dates=['datetime'])
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek
#Example accessing it as a csv
# %%
# adding precipt data to compare
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.9455&lon=-113.2549" \
       "&vars=prcp&years=&format=csv"
data2 = pd.read_table(url, delimiter=',', skiprows=6)
data2 = data2[3285:]
data2 = data2.reset_index(drop=True)
data = data.join(data2['prcp (mm/day)'])

# %%
# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# got rid of extreme outliers
flow_weekly = flow_weekly[
        (flow_weekly.flow <= 450)]
# %%
# looking for dates I wanted
flow_weekly.iloc[1386]
# %%
# creation of lag timed series
# the loop names each column flow_tm%i and shifts it by i
for i in range(1, 4):
    flow_weekly['flow_tm%s' % i] = flow_weekly['flow'].shift(i)


# making my training period 2010-2015
train = flow_weekly[945:1168][['flow', 'flow_tm1',
                               'flow_tm2', 'flow_tm3', 'prcp (mm/day)']]
# making testing from 2015-2020
test = flow_weekly[1168:1385][['flow', 'flow_tm1',
                           'flow_tm2', 'flow_tm3', 'prcp (mm/day)']]


# %%
# linear regression with 4 time lags as inputs to the model
# you don't need to change training period (2010-2015)
model4 = LinearRegression()
y = train['flow'].values
x4 = train[['flow_tm1', 'flow_tm2', 'flow_tm3', 'prcp (mm/day)']]
model4.fit(x4, y)
r_sq = model4.score(x4, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model4.intercept_, 2))
print('slope:', np.round(model4.coef_, 2))

# generate preditions for training phase and testing phase
# (training phase is used to generate coefecients and intercepts)
q_pred4_train = model4.predict(train[['flow_tm1', 'flow_tm2',
                                      'flow_tm3', 'prcp (mm/day)']])
q_pred4_test = model4.predict(test[['flow_tm1', 'flow_tm2',
                                    'flow_tm3', 'prcp (mm/day)']])

# %%
# projecting 2 weeks into the future using 4 time lags
# lists that start with the 4 most recent entries
lastweekx4 = [0]
lastweekx3 = [flow_weekly.flow[-3]]
lastweekx2 = [flow_weekly.flow[-2]]
lastweek = [flow_weekly.flow[-1]]
# empty list for predictions
weeklypred_4 = []

for i in range(2):
    wk1 = lastweek[i]
    wk2 = lastweekx2[i]
    wk3 = lastweekx3[i]
    wk4 = lastweekx4[i]
    # appends to last week so that they refer to next time step
    lastweekx2.append(wk1)
    lastweekx3.append(wk2)
    lastweekx4.append(0)
    # the prediction for week # i
    prediction = model4.intercept_ + model4.coef_[0] * wk1 + model4.coef_[1] \
        * wk2 + model4.coef_[2] * wk3 + model4.coef_[3] * wk4
    lastweek.append(prediction)
    # creates a list of just my predictions for week 1 then week 2
    weeklypred_4.append(prediction)
# print(weeklypred_4)
# %%
data2[(data2['prcp (mm/day)'] > 0) & (data.year > 2010)].mean()
# projecting 16 weeks into the future
# The + 8 is added to start at 8/21
lastweekx4 = [2.00]
lastweekx3 = [flow_weekly.flow[-(3 + 10)]]
lastweekx2 = [flow_weekly.flow[-(2 + 10)]]
lastweek = [flow_weekly.flow[-(1 + 10)]]
weeklypred = []
for i in range(16):
    wk1 = lastweek[i]
    wk2 = lastweekx2[i]
    wk3 = lastweekx3[i]
    wk4 = lastweekx4[i]
    lastweekx2.append(wk1)
    lastweekx3.append(wk2)
    # added a bernoulli variable multiplied by 10 mm
    # this way rain could impact the model
    lastweekx4.append(10*(bernoulli.rvs(size=1,p=0.15)))
    prediction = model4.intercept_ + model4.coef_[0] * wk1 + model4.coef_[1] \
        * wk2 + model4.coef_[2] * wk3 + model4.coef_[3] * wk4
    lastweek.append(prediction)
    weeklypred.append(prediction)
# print(weeklypred)
# %%
# shows a plot of 16 week prediction
# creates unique name list of each week from 1 to 16
weeks = []
for i in range(16):
    weeks.append('week# ' '%s' % (i+1))
# creates a plot of my prediction for each week of the semester

plt.style.use('seaborn-whitegrid')


plt.scatter(x=weeks, y=weeklypred, marker='o', label='predicted flow')
plt.scatter(x=weeks[0:10],
            y=flow_weekly.flow[(flow_weekly.year == 2020)
            & (flow_weekly.month >= 8) & (flow_weekly.day >= 20) |
            (flow_weekly.year == 2020) & (flow_weekly.month >= 9)],
            marker='o', label='observed')

plt.ylabel('Flow (cfs)')
plt.ylim([0, 200])
plt.title('Weekly Discharge Prediction')
plt.xticks(rotation=45, fontsize=10)
plt.legend()
plt.savefig('Discharge_Prediction.png')
# %%
# shows a plot of post 2005 data for the training period, and testing period
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='full')
ax.plot(train['flow'], 'r:', label='training')
ax.plot(test['flow'], color='orange', linestyle='--', label='testing')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       xlim=[datetime.date(2005, 1, 1), datetime.date(2020, 8, 23)])
ax.legend()
plt.savefig('Observed_flow.png')

# %%
# 5. Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
           color='blueviolet', label='observations')
ax.set(xlabel='flow t-1', ylabel='flow t')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred4_train), label='AR model')
ax.legend()
plt.savefig('AR_model.png')
# %%
# prints the prediction that you will use
print(f'The prediction for week 1 is {str(weeklypred_4[0].round(2))} cfs '
      f'and week 2 is {str(weeklypred_4[1].round(2))} cfs')

# %%
