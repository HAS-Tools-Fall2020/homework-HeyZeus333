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
from scipy import stats
#note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly 
flow_weekly = data.resample("W", on='datetime').mean()
#%%
# box plot showing me location of outliers from month 8 to 12
data_to_plot = [data.flow[(data.month >= 8)]]

fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.ylim([0, 335])
plt.title('Discharge Boxplot August-December');
fig.savefig('Discharge_Boxplot_Aug-Dec.png', bbox_inches='tight')
#%%
# making model ignore flow values that are considered outliers if this isn't done the prediction on the later weeks are far to high
flow_weekly = flow_weekly[(flow_weekly.flow <= 335)]
# flow_weekly = flow_weekly

# %%
# creation of lag timed series
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(3)
flow_weekly['flow_tm4'] = flow_weekly['flow'].shift(4)
# making my training period 2010-2015
train = flow_weekly[940:1170][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3', 'flow_tm4']]
#making testing from 2015-2020
test = flow_weekly[1170:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]

#%%
# if you'd rather use one time lag for you pred iction uncomment these two cells
# creating a model for the single time lag scenario
# model = LinearRegression()
# x=train['flow_tm1'].values.reshape(-1,1) 
# y=train['flow'].values
# model.fit(x,y)

# r_sq = model.score(x, y)

# #printing everything
# print('coefficient of determination:', np.round(r_sq,2)) 
# print('intercept:', np.round(model.intercept_, 2))
# print('slope:', np.round(model.coef_, 2))

# # generate preditions for training phase and testing phase (training phase is used to generate coefecients and intercepts then applied to each period)
# q_pred_train = model.predict(train['flow_tm1'].values.reshape(-1,1))
# q_pred_test = model.predict(test['flow_tm1'].values.reshape(-1,1))

#%%
# # projecting model 16 weeks into the future
# week1 = [flow_weekly.flow[-1]]
# weeklypred=[]
# for i in range(16):
#         last_week_flow = week1[i]
#         prediction = model.intercept_ + model.coef_ * last_week_flow
#         week1.append(prediction)
#         weeklypred.append(prediction)

# %%
# if you'd rather use two time lags for you pred iction uncomment these two cells


# linear regression with two time lags as inputs to the model 
# model2 = LinearRegression()
# x2=train[['flow_tm1','flow_tm2']]
# model2.fit(x2,y)
# r_sq = model2.score(x2, y)
# print('coefficient of determination:', np.round(r_sq,2))
# print('intercept:', np.round(model2.intercept_, 2))
# print('slope:', np.round(model2.coef_, 2))

# # generate preditions for training phase and testing phase (training phase is used to generate coefecients and intercepts then applied to each period)
# q_pred2_train = model2.predict(train[['flow_tm1', 'flow_tm2']])
# q_pred2_test = model2.predict(test[['flow_tm1', 'flow_tm2']])

#%%
# lastweekx2 = [flow_weekly.flow[-2]]
# lastweek = [flow_weekly.flow[-1]]
# weeklypred_2 =[]

# for i in range(16):
#         week1 = lastweek[i]
#         week2 = lastweekx2[i]
#         lastweekx2.append(week1)
#         prediction = model2.intercept_ + model2.coef_[0]* week1 +  model2.coef_[1]* week2 
#         lastweek.append(prediction)
#         weeklypred_2.append(prediction)

# %%
# linear regression with 3 time lags as inputs to the model 
model3 = LinearRegression()
x3=train[['flow_tm1','flow_tm2', 'flow_tm3']]
y=train['flow'].values
model3.fit(x3,y)
r_sq = model3.score(x3, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model3.intercept_, 2))
print('slope:', np.round(model3.coef_, 2))

# generate preditions for training phase and testing phase (training phase is used to generate coefecients and intercepts then applied to each period)
q_pred3_train = model3.predict(train[['flow_tm1', 'flow_tm2', 'flow_tm3']])
q_pred3_test = model3.predict(test[['flow_tm1', 'flow_tm2', 'flow_tm3']])

#%%
# projecting 16 weeks into the future using 3 time lags
# lists that start with the three most recent entries in the flow_weekly data AKA August 2020
lastweekx3= [flow_weekly.flow[-3]]
lastweekx2 = [flow_weekly.flow[-2]]
lastweek = [flow_weekly.flow[-1]]
#empty list in which your weekly prediction goes
weeklypred_3 =[]

for i in range(16):
        #refers to three most recent entries 
        week1 = lastweek[i]
        week2 = lastweekx2[i]
        week3 = lastweekx3[i]
        # appends to last week so that they refer to next time step
        lastweekx2.append(week1)
        lastweekx3.append(week2)
        # the prediction for week # i
        prediction = model3.intercept_ + model3.coef_[0]* week1 + model3.coef_[1]* week2 +  model3.coef_[2]* week3
        # appends the prediction to last week so you can continue loop
        lastweek.append(prediction)
        # creates a list of just my predictions for weeks 1 through 16
        weeklypred_3.append(prediction)
# un hash the next line if you'd like to print to copy and paste to excel forcast sheet
print(weeklypred_3)

#%%
# next few cells are plots if you decide to use model 1 or 2 make sure to change whats being plotted 
# shows a plot of post 2005 data for the training period, and testing period
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='full')
ax.plot(train['flow'], 'r:', label='training')
ax.plot(test['flow'], color='orange', linestyle='--', label='testing')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]", xlim=[datetime.date(2005, 1, 1), datetime.date(2020, 8, 23)])
ax.legend()
plt.savefig('Observed_flow.png')
#%%
# a zoomed line plot of the testing period vs observed flow
fig, ax = plt.subplots()
ax.plot(test['flow'], color='grey', linewidth=2, label='observed')
ax.plot(test.index, q_pred3_test, color='orange', linestyle='--', 
        label='testing')
ax.set(title="Model(testing) vs Observed", xlabel="Date", ylabel="Weekly Avg Flow [cfs]")
plt.xticks(rotation=45,fontsize=12)
ax.legend()
plt.savefig('Model(testing).png')
#%%
# a zoomed line plot of the training period vs observed flow
fig, ax = plt.subplots()
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred3_train, color='red', linestyle='--', 
        label='modeled')
ax.set(title="Model(training) vs Observed", xlabel="Date", ylabel="Weekly Avg Flow [cfs]")

plt.xticks(rotation=45,fontsize=12)
ax.legend()
plt.savefig('Model(training).png')
#%%
# 5. Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
              color='blueviolet', label='observations')
ax.set(xlabel='flow t-1', ylabel='flow t')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred3_train), label='AR model')
ax.legend()
plt.savefig('AR_model.png')
# %%
# creates unique name list of each week from 1 to 16
weeks = []
for i in range (16):
        # this is done because python counts 1 behind 
        i=i+1
        weeks.append('week# ' '%s'%i)
# creates a plot of my prediction for each week of the semester
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

plt.scatter(x=weeks, y=weeklypred_3, marker='o', label='predicted flow');

plt.ylabel('Flow (cfs)');
plt.ylim([0, 250])
plt.title('Weekly Discharge Prediction');
plt.xticks(rotation=45,fontsize=10)
plt.legend()
plt.savefig('Discharge_Prediction.png')


# %%
# Re-uploading data for 2 week forcast make sure to change to 'streamflow_week7.txt'
filename = 'streamflow_week6.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly 
flow_weekly = data.resample("W", on='datetime').mean()

#%%
# making model ignore flow values that are considered outliers if this isn't done the prediction on the later weeks are far to high
flow_weekly = flow_weekly[(flow_weekly.flow <= 335)]

# %%
# linear regression with 4 time lags as inputs to the model you don't need to change training period (2010-2015)
model4 = LinearRegression()
y=train['flow'].values
x4=train[['flow_tm1','flow_tm2', 'flow_tm3', 'flow_tm4']]
model4.fit(x4,y)
r_sq = model4.score(x4, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model4.intercept_, 2))
print('slope:', np.round(model4.coef_, 2))


#%%
# projecting 16 weeks into the future using 4 time lags
lastweekx4= [flow_weekly.flow[-4]]
lastweekx3= [flow_weekly.flow[-3]]
lastweekx2 = [flow_weekly.flow[-2]]
lastweek = [flow_weekly.flow[-1]]
weeklypred_4 =[]

for i in range(2):
        week1 = lastweek[i]
        week2 = lastweekx2[i]
        week3 = lastweekx3[i]
        week4 = lastweekx4[i]
        lastweekx2.append(week1)
        lastweekx3.append(week2)
        lastweekx4.append(week3)
        prediction = model4.intercept_ + model4.coef_[0]* week1 + model4.coef_[1]* week2 +  model4.coef_[2]* week3 +  model4.coef_[3]* week4
        lastweek.append(prediction)
        # creates a list of just my predictions for week 1 then week 2
        weeklypred_4.append(prediction)
#%%
#prints the list of week 1 prediction then the second week
print(weeklypred_4)
# %%
