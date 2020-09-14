# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
path= "..\..\data"
filepath = os.path.join(path, filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
# print(min(flow))
# print(max(flow))
# print(np.mean(flow))
# print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
week1 = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if 30 <= flow[i] <= 60 and month[i] == 9 and 13 <= day[i] <= 19:
                week1.append(flow[i])

week2= []
for i in range(len(flow)):
        if 30 <= flow[i] <=60 and month[i] == 9 and 20 <= day[i] <= 26:
                week2.append(flow[i])



# blist=[]
# for i in range(len(flow)):
#         if flow [i] < 600 and month[i] == 9 and day[i] == 2:
#                 blist.append(i)


# see how many times the criteria was met by checking the length
# of the index list that was generated
#print(len(ilist))


# %%

# print(np.mean(week1))
# print(np.mean(week2))
# print(np.mean(week3))
# print(np.mean(week4))
# print(np.mean(week5))
# print(np.mean(week6))
# print(np.mean(week7))
# print(np.mean(week8))
# print(np.mean(week9))
# print(np.mean(week10))
# print(np.mean(week11))
# print(np.mean(week12))
# print(np.mean(week13))
# print(np.mean(week14))
# print(np.mean(week15))
# print(np.mean(week16))

# %%
weeklymean= []

weeklymean.append(np.mean(week1))
weeklymean.append(np.mean(week2))
# weeklymean.append(np.mean(week3))
# weeklymean.append(np.mean(week4))
# weeklymean.append(np.mean(week5))
# weeklymean.append(np.mean(week6))
# weeklymean.append(np.mean(week7))
# weeklymean.append(np.mean(week8))
# weeklymean.append(np.mean(week9))
# weeklymean.append(np.mean(week10))
# weeklymean.append(np.mean(week11))
# weeklymean.append(np.mean(week12))
# weeklymean.append(np.mean(week13))
# weeklymean.append(np.mean(week14))
# weeklymean.append(np.mean(week15))
# weeklymean.append(np.mean(week16))
print(weeklymean)
# %%
weeklymin= []

weeklymin.append(min(week1))
weeklymin.append(min(week2))
# weeklymin.append(min(week3))
# weeklymin.append(min(week4))
# weeklymin.append(min(week5))
# weeklymin.append(min(week6))
# weeklymin.append(min(week7))
# weeklymin.append(min(week8))
# weeklymin.append(min(week9))
# weeklymin.append(min(week10))
# weeklymin.append(min(week11))
# weeklymin.append(min(week12))
# weeklymin.append(min(week13))
# weeklymin.append(min(week14))
# weeklymin.append(min(week15))
# weeklymin.append(min(week16))

print(weeklymin)

#%%
weeklymax= []

weeklymax.append(max(week1))
weeklymax.append(max(week2))

print(weeklymax)
#%%
weeklystd= []

weeklystd.append(np.std(week1))
weeklystd.append(np.std(week2))
# weeklystd.append(np.std(week3))
# weeklystd.append(np.std(week4))
# weeklystd.append(np.std(week5))
# weeklystd.append(np.std(week6))
# weeklystd.append(np.std(week7))
# weeklystd.append(np.std(week8))
# weeklystd.append(np.std(week9))
# weeklystd.append(np.std(week10))
# weeklystd.append(np.std(week11))
# weeklystd.append(np.std(week12))
# weeklystd.append(np.std(week13))
# weeklystd.append(np.std(week14))
# weeklystd.append(np.std(week15))
# weeklystd.append(np.std(week16))

print(weeklystd)
# %%
#weeks= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# %%
# A simple x, y scatter plot using lists from above
# %matplotlib inline
# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# import numpy as np

# plt.scatter(x=weeks, y=weeklymin, marker='o');
# plt.xlabel('Week (#)')
# plt.ylabel('Min Flow (cfs)');
# plt.ylim([0, 250])
# plt.title('Weekly Min Discharge');
# %%
# A simple x, y scatter plot using lists from above
# %matplotlib inline
# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# import numpy as np

# plt.scatter(x=weeks, y=weeklymean, marker='o', label='mean flow');
# plt.scatter(x=weeks, y=weeklymin, marker='o', label='min flow');
# plt.xlabel('Week (#)')
# plt.ylabel('Flow (cfs)');
# plt.ylim([0, 250])
# plt.title('Weekly Discharge');
# plt.legend()
