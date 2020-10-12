# Starter code for week 6 illustrating how to build an AR model
# and plot it

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
# note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week7.txt'
filepath = os.path.join('', filename)
print(os.getcwd())
print(filepath)


# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()
# %%
# box plot showing me location of outliers from month 8 to 12
data_to_plot = [data.flow[(data.month >= 8)]]

fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.ylim([0, 336])
plt.title('Discharge Boxplot August-December')
fig.savefig('Discharge_Boxplot_Aug-Dec.png', bbox_inches='tight')
# %%
# making model ignore flow values that are considered outliers
flow_weekly = flow_weekly[
        (flow_weekly.flow <= 336)]
# flow_weekly = flow_weekly

# %%
# creation of lag timed series
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(3)
flow_weekly['flow_tm4'] = flow_weekly['flow'].shift(4)
# making my training period 2010-2015
train = flow_weekly[940:1170][['flow', 'flow_tm1',
                               'flow_tm2', 'flow_tm3', 'flow_tm4']]
# making testing from 2015-2020
test = flow_weekly[1170:][['flow', 'flow_tm1',
                           'flow_tm2', 'flow_tm3', 'flow_tm4']]


# %%
# linear regression with 4 time lags as inputs to the model
# you don't need to change training period (2010-2015)
model4 = LinearRegression()
y = train['flow'].values
x4 = train[['flow_tm1', 'flow_tm2', 'flow_tm3', 'flow_tm4']]
model4.fit(x4, y)
r_sq = model4.score(x4, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model4.intercept_, 2))
print('slope:', np.round(model4.coef_, 2))

# generate preditions for training phase and testing phase
# (training phase is used to generate coefecients and intercepts)
q_pred4_train = model4.predict(train[['flow_tm1', 'flow_tm2',
                                      'flow_tm3', 'flow_tm4']])
q_pred4_test = model4.predict(test[['flow_tm1', 'flow_tm2',
                                    'flow_tm3', 'flow_tm4']])

# %%
# projecting 2 weeks into the future using 4 time lags
# lists that start with the 4 most recent entries
lastweekx4 = [flow_weekly.flow[-4]]
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
    lastweekx4.append(wk3)
    # the prediction for week # i
    prediction = model4.intercept_ + model4.coef_[0] * wk1 + model4.coef_[1] \
        * wk2 + model4.coef_[2] * wk3 + model4.coef_[3] * wk4
    lastweek.append(prediction)
    # creates a list of just my predictions for week 1 then week 2
    weeklypred_4.append(prediction)
# print(weeklypred_4)
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
# a zoomed line plot of the testing period vs observed flow
fig, ax = plt.subplots()
ax.plot(test['flow'], color='grey', linewidth=2, label='observed')
ax.plot(test.index, q_pred4_test, color='orange', linestyle='--',
        label='testing')
ax.set(title="Model(testing) vs Observed",
       xlabel="Date", ylabel="Weekly Avg Flow [cfs]")
plt.xticks(rotation=45, fontsize=12)
ax.legend()
plt.savefig('Model(testing).png')
# %%
# a zoomed line plot of the training period vs observed flow
fig, ax = plt.subplots()
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred4_train, color='red', linestyle='--',
        label='modeled')
ax.set(title="Model(training) vs Observed", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]")

plt.xticks(rotation=45, fontsize=12)
ax.legend()
plt.savefig('Model(training).png')
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
print(weeklypred_4)
# %%
# a function I needed to include


def lo_hi(a_list):
    new_list = []
    for num in a_list:
        if num < 75:
            new_list.append('lower')
        else:
            new_list.append('higher')
    return new_list


flow_type = lo_hi(weeklypred_4)
print(f'1st will be {flow_type[0]} flow & 2nd will be {flow_type[1]} flow')

# %%
