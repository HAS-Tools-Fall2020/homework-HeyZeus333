# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../data', filename)
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

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==7))

# this gives a list of T/F where the criteria are met
(flow_data[:,3] > 600) & (flow_data[:,1]==7)

# this give the flow values where that criteria is met
flow_pick = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), 3]

# this give the year values where that criteria is met
year_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), 0]

# this give the all rows  where that criteria is met
all_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), ]

# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])
#%%
#Weeks
week1: 8/23-8/29
week2: 8/30-9/5
week3: 9/6-9/12
week4: 9/13-9/19
week5: 9/20-9/26
week6: 9/27-10/3
week7: 10/4-10/10
week8: 10/11-10/17
week9: 10/18-10/24
week10: 10/25-10/31
week11: 11/1-11/7
week12: 11/8-11/14
week13: 11/15-11/21
week14: 11/22-11/28
week15: 11/29-12/5
week16: 12/6-12/12
#%%
mean_2020_summer= np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==6) & (flow_data[:,1]==7) & (flow_data[:,1]==8),3])
mean_summer = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==6) & (flow_data[:,1]==7) & (flow_data[:,1]==8),3])
mean_summer_difference= mean_2020_summer/ mean_summer
Week1_mean = np.mean(flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3])
Week2_mean = np.mean(flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3])
Week2_mean_2 = np.mean(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week2_mean= (Week2_mean + Week2_mean_2)/2

Week3_mean = np.mean(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])
Week4_mean = np.mean(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3])
Week5_mean = np.mean(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3])
Week6_mean = np.mean(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3])
Week6_mean_2 = np.mean(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3])
Week6_mean= (Week6_mean + Week6_mean_2)/2

Week7_mean = np.mean(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3])
Week8_mean = np.mean(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3])
Week9_mean = np.mean(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3])
Week10_mean = np.mean(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3])
Week11_mean = np.mean(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 6), 3])
Week12_mean = np.mean(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 7) & (flow_data[:,2] <= 13), 3])
Week13_mean = np.mean(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 14) & (flow_data[:,2] <= 20), 3])
Week14_mean = np.mean(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 21) & (flow_data[:,2] <= 27), 3])
Week15_mean = np.mean(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 28) & (flow_data[:,2] <= 30), 3])
Week15_mean_2 = np.mean(flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week15_mean= (Week15_mean + Week15_mean_2)/2

Week16_mean = np.mean(flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])


# %%
mean_2020_summer_1= np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==6),3])
mean_2020_summer_2= np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==7),3])
mean_2020_summer_3= np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==8),3])
mean_summer_1 = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==6) & (flow_data[:,1]==7) & (flow_data[:,1]==8),3])
mean_summer_2 = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==6) & (flow_data[:,1]==7) & (flow_data[:,1]==8),3])
mean_summer_3 = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==6) & (flow_data[:,1]==7) & (flow_data[:,1]==8),3])
mean_summer_difference= mean_2020_summer/ mean_summer