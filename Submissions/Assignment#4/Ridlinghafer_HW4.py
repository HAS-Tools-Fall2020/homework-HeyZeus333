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


#%%
#Weeks dates
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
Week1= flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3]
Week2 = flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3]
Week2_2 = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3]

Week3= flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3]
Week4= flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3]
Week5 = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3]
Week6 = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3]
Week6_2 = flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3]

Week7= flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3]
Week8 = flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3]
Week9 = flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3]
Week10 = flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3]
Week11 = flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 1) & (flow_data[:,2] <= 7), 3]
Week12 = flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 8) & (flow_data[:,2] <= 14), 3]
Week13 = flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 15) & (flow_data[:,2] <= 21), 3]
Week14 = flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 22) & (flow_data[:,2] <= 28), 3]
Week15 = flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 29) & (flow_data[:,2] <= 30), 3]
Week15_2 = flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3]

Week16 = flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3]

#%%
data_to_plot = [Week1, Week2, Week2_2, Week3, Week4, Week5, Week6, Week6_2, Week7, Week8, Week9, Week10, Week11, Week12, Week13, Week14, Week15, Week15_2, Week16]
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.ylim([0, 500])
plt.title('Weekly Discharge Boxplot');
ax.set_xticklabels(['Week1', 'Week2', 'Week2_2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week6_2', 'Week7', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week15_2', 'Week16'])
plt.xticks(rotation=45,fontsize=12)
fig.savefig('BoxPlots.png', bbox_inches='tight')

#%%
# Finds each weeks mean value for years prior to 2020
Week1 = np.quantile(flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3], q=0.05)
Week2 = np.quantile(flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3], q=0.05)
Week2_2 = np.quantile(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3], q=0.05)
Week2= (Week2*2 + Week2_2*5)/7

Week3 = np.quantile(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3], q=0.05)
Week4 = np.quantile(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3], q=0.05)
Week5 = np.quantile(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3], q=0.05)
Week6 = np.quantile(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3], q=0.125)
Week6_2 = np.quantile(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3], q=0.125)
Week6= (Week6*4 + Week6_2*3)/7

Week7 = np.quantile(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3], q=0.125)
Week8 = np.quantile(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3], q=0.125)
Week9 = np.quantile(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3], q=0.125)
Week10 = np.quantile(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3], q=0.125)
Week11 = np.quantile(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 1) & (flow_data[:,2] <= 7), 3], q=0.125)
Week12 = np.quantile(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 8) & (flow_data[:,2] <= 14), 3], q=0.125)
Week13 = np.quantile(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 15) & (flow_data[:,2] <= 21), 3], q=0.125)
Week14 = np.quantile(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 22) & (flow_data[:,2] <= 28), 3], q=0.125)
Week15 = np.quantile(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 29) & (flow_data[:,2] <= 30), 3], q=0.125)
Week15_2 = np.quantile(flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3], q=0.125)
Week15= (Week15*2 + Week15_2*5)/7

Week16 = np.quantile(flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3], q=0.125)
#%%
#%%
# Finds each weeks mean value for years prior to 2020
Week1_min = min(flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3])
Week2_min = min(flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3])
Week2_min_2 = min(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week2_min = min(Week2_min,Week2_min_2)

Week3_min = min(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])
Week4_min = min(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3])
Week5_min = min(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3])
Week6_min = min(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3])
Week6_min_2 = min(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3])
Week6_min = min(Week6_min,Week6_min_2)

Week7_min = min(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3])
Week8_min = min(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3])
Week9_min = min(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3])
Week10_min = min(flow_data[(flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3])
Week11_min = min(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 1) & (flow_data[:,2] <= 7), 3])
Week12_min = min(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 8) & (flow_data[:,2] <= 14), 3])
Week13_min = min(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 15) & (flow_data[:,2] <= 21), 3])
Week14_min = min(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 22) & (flow_data[:,2] <= 28), 3])
Week15_min = min(flow_data[(flow_data[:,1]==11) & (flow_data[:,2] >= 29) & (flow_data[:,2] <= 30), 3])
Week15_min_2 = min(flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week15_min = min(Week15_min,Week15_min_2)

Week16_min = min(flow_data[(flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])


# %%
# Finds the predicted flow by multiplying the mean flow by the summer fraction
week1= Week1
week2= Week2
week3= Week3
week4= Week4
week5= Week5
week6= Week6
week7= Week7
week8= Week8
week9= Week9
week10= Week10
week11= Week11
week12= Week12
week13= Week13
week14= Week14
week15= Week15
week16= Week16
# Creates a list for Graphing
weeklypred= []

weeklypred.append(week1)
weeklypred.append(week2)
weeklypred.append(week3)
weeklypred.append(week4)
weeklypred.append(week5)
weeklypred.append(week6)
weeklypred.append(week7)
weeklypred.append(week8)
weeklypred.append(week9)
weeklypred.append(week10)
weeklypred.append(week11)
weeklypred.append(week12)
weeklypred.append(week13)
weeklypred.append(week14)
weeklypred.append(week15)
weeklypred.append(week16)
print(weeklypred)

Weeklymin= []

Weeklymin.append(Week1_min)
Weeklymin.append(Week2_min)
Weeklymin.append(Week3_min)
Weeklymin.append(Week4_min)
Weeklymin.append(Week5_min)
Weeklymin.append(Week6_min)
Weeklymin.append(Week7_min)
Weeklymin.append(Week8_min)
Weeklymin.append(Week9_min)
Weeklymin.append(Week10_min)
Weeklymin.append(Week11_min)
Weeklymin.append(Week12_min)
Weeklymin.append(Week13_min)
Weeklymin.append(Week14_min)
Weeklymin.append(Week15_min)
Weeklymin.append(Week16_min)
print(Weeklymin)
# %%
weeks= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#%%
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

plt.scatter(x=weeks, y=weeklypred, marker='o', label='predicted flow');
plt.scatter(x=weeks, y=Weeklymin, marker='o', label='min flow');
plt.xlabel('Week (#)')
plt.ylabel('Flow (cfs)');
plt.ylim([0, 250])
plt.title('Weekly Discharge Prediction');
plt.legend()
plt.savefig('Discharge_Prediction.png')


#%%
#Question 3
tot_Week2 = flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3]
tot_Week2_2 = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3]

tot_Week3= flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3]
tot_Week4= flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3]
tot_Week5 = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3]


Week2_n = flow_data[(flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31) & (flow_data[:,3] > weeklypred[1]), 3]
Week2_n_2 = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5) & (flow_data[:,3] > weeklypred[1]), 3]

Week3_n = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12) & (flow_data[:,3] > weeklypred[2]), 3]
Week4_n = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19) & (flow_data[:,3] > weeklypred[3]), 3]
Week5_n = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26) & (flow_data[:,3] > weeklypred[4]), 3]

print((Week2_n.size+Week2_n_2.size)/(tot_Week2.size+tot_Week2_2.size))
print(Week3_n.size/tot_Week3.size)
print(Week4_n.size/tot_Week4.size)
print(Week5_n.size/tot_Week5.size)


print(Week2_n.size+Week2_n_2.size)
print(Week3_n.size)
print(Week4_n.size)
print(Week5_n.size)


#%%
#START OF post 2010 data
#%%
Week1= flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3]
Week2 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3]
Week2_2 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3]

Week3= flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3]
Week4= flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3]
Week5 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3]
Week6 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3]
Week6_2 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3]

Week7= flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3]
Week8 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3]
Week9 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3]
Week10 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3]
Week11 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 1) & (flow_data[:,2] <= 7), 3]
Week12 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 8) & (flow_data[:,2] <= 14), 3]
Week13 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 15) & (flow_data[:,2] <= 21), 3]
Week14 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 22) & (flow_data[:,2] <= 28), 3]
Week15 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 29) & (flow_data[:,2] <= 30), 3]
Week15_2 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3]

Week16 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3]

#%%
data_to_plot = [Week1, Week2, Week2_2, Week3, Week4, Week5, Week6, Week6_2, Week7, Week8, Week9, Week10, Week11, Week12, Week13, Week14, Week15, Week15_2, Week16]
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.ylim([0, 500])
plt.title('Weekly Discharge Boxplot');
ax.set_xticklabels(['Week1', 'Week2', 'Week2_2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week6_2', 'Week7', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week15_2', 'Week16'])
plt.xticks(rotation=45,fontsize=12)
fig.savefig('Boxplot_2010.png', bbox_inches='tight')
#%%
#mean values
Post_2010_Week1 = np.quantile(flow_data[(flow_data[:,0]>=2010) &(flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3], q=0.05)
Post_2010_Week2 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3], q=0.05)
Post_2010_Week2_2 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3], q=0.05)
Post_2010_Week2= (Post_2010_Week2*2 + Post_2010_Week2_2*5)/7

Post_2010_Week3 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3], q=0.05)
Post_2010_Week4 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3], q=0.05)
Post_2010_Week5 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3], q=0.05)
Post_2010_Week6 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3], q=0.125)
Post_2010_Week6 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3], q=0.125)
Post_2010_Week6_2 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3], q=0.125)
Post_2010_Week6= (Post_2010_Week6*4 + Post_2010_Week6_2*3)/7

Post_2010_Week7 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3], q=0.125)
Post_2010_Week8 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3], q=0.125)
Post_2010_Week9 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3], q=0.125)
Post_2010_Week10 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3], q=0.125)
Post_2010_Week11 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 1) & (flow_data[:,2] <= 7), 3], q=0.125)
Post_2010_Week12 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 8) & (flow_data[:,2] <= 14), 3], q=0.125)
Post_2010_Week13 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 15) & (flow_data[:,2] <= 21), 3], q=0.125)
Post_2010_Week14 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 22) & (flow_data[:,2] <= 28), 3], q=0.125)
Post_2010_Week15 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 29) & (flow_data[:,2] <= 30), 3], q=0.125)
Post_2010_Week15_2 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3], q=0.125)
Post_2010_Week15= (Post_2010_Week15*2 + Post_2010_Week15_2*5)/7

Post_2010_Week16 = np.quantile(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3], q=0.125)



# %%
#%%
# Finds each weeks mean value for years prior to 2020
Week1_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3])
Week2_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3])
Week2_min_2 = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week2_min = min(Week2_min,Week2_min_2)

Week3_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])
Week4_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3])
Week5_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3])
Week6_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3])
Week6_min_2 = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3])
Week6_min = min(Week6_min,Week6_min_2)

Week7_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3])
Week8_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3])
Week9_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3])
Week10_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3])
Week11_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 1) & (flow_data[:,2] <= 7), 3])
Week12_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 8) & (flow_data[:,2] <= 14), 3])
Week13_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 15) & (flow_data[:,2] <= 21), 3])
Week14_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 22) & (flow_data[:,2] <= 28), 3])
Week15_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==11) & (flow_data[:,2] >= 29) & (flow_data[:,2] <= 30), 3])
Week15_min_2 = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week15_min = min(Week15_min,Week15_min_2)

Week16_min = min(flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])

Weeklymin= []

Weeklymin.append(Week1_min)
Weeklymin.append(Week2_min)
Weeklymin.append(Week3_min)
Weeklymin.append(Week4_min)
Weeklymin.append(Week5_min)
Weeklymin.append(Week6_min)
Weeklymin.append(Week7_min)
Weeklymin.append(Week8_min)
Weeklymin.append(Week9_min)
Weeklymin.append(Week10_min)
Weeklymin.append(Week11_min)
Weeklymin.append(Week12_min)
Weeklymin.append(Week13_min)
Weeklymin.append(Week14_min)
Weeklymin.append(Week15_min)
Weeklymin.append(Week16_min)
print(Weeklymin)

# Creates a list for Graphing

Post_2010_Weeklypred= []

Post_2010_Weeklypred.append(Post_2010_Week1)
Post_2010_Weeklypred.append(Post_2010_Week2)
Post_2010_Weeklypred.append(Post_2010_Week3)
Post_2010_Weeklypred.append(Post_2010_Week4)
Post_2010_Weeklypred.append(Post_2010_Week5)
Post_2010_Weeklypred.append(Post_2010_Week6)
Post_2010_Weeklypred.append(Post_2010_Week7)
Post_2010_Weeklypred.append(Post_2010_Week8)
Post_2010_Weeklypred.append(Post_2010_Week9)
Post_2010_Weeklypred.append(Post_2010_Week10)
Post_2010_Weeklypred.append(Post_2010_Week11)
Post_2010_Weeklypred.append(Post_2010_Week12)
Post_2010_Weeklypred.append(Post_2010_Week13)
Post_2010_Weeklypred.append(Post_2010_Week14)
Post_2010_Weeklypred.append(Post_2010_Week15)
Post_2010_Weeklypred.append(Post_2010_Week16)
print(Post_2010_Weeklypred)

#%%
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

plt.scatter(x=weeks, y=Post_2010_Weeklypred, marker='o', label='predicted flow');
plt.scatter(x=weeks, y=Weeklymin, marker='o', label='min flow');
plt.xlabel('Week (#)')
plt.ylabel('Flow (cfs)');
plt.ylim([0, 250])
plt.title('Post_2010_Weekly Discharge Prediction');
plt.legend()
plt.savefig('Post_2010_Discharge_Prediction.png')
#%%
#Question 3
tot_Week2 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3]
tot_Week2_2 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3]

tot_Week3= flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3]
tot_Week4= flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3]
tot_Week5 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3]
tot_Week6 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3]

Week2_n = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31) & (flow_data[:,3] > weeklypred[1]), 3]
Week2_n_2 = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5) & (flow_data[:,3] > weeklypred[1]), 3]

Week3_n = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12) & (flow_data[:,3] > weeklypred[2]), 3]
Week4_n = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19) & (flow_data[:,3] > weeklypred[3]), 3]
Week5_n = flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26) & (flow_data[:,3] > weeklypred[4]), 3]

print((Week2_n.size+Week2_n_2.size)/(tot_Week2.size+tot_Week2_2.size))
print(Week3_n.size/tot_Week3.size)
print(Week4_n.size/tot_Week4.size)
print(Week5_n.size/tot_Week5.size)


print(Week2_n.size+Week2_n_2.size)
print(Week3_n.size)
print(Week4_n.size)
print(Week5_n.size)
#%%
#START OF pre 2000 data

Pre_2000_Week1 = np.quantile(flow_data[(flow_data[:,0]<=2000) &(flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3], q=0.05)
Pre_2000_Week2 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3], q=0.05)
Pre_2000_Week2_2 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3], q=0.05)
Pre_2000_Week2= (Pre_2000_Week2*2 + Pre_2000_Week2_2*5)/7

Pre_2000_Week3 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3], q=0.05)
Pre_2000_Week4 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3], q=0.05)
Pre_2000_Week5 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3], q=0.05)
Pre_2000_Week6 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3], q=0.125)
Pre_2000_Week6_2 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==10) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 3), 3], q=0.125)
Pre_2000_Week6= (Pre_2000_Week6*4 + Pre_2000_Week6_2*3)/7

Pre_2000_Week7 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==10) & (flow_data[:,2] >= 4) & (flow_data[:,2] <= 10), 3], q=0.125)
Pre_2000_Week8 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==10) & (flow_data[:,2] >= 11) & (flow_data[:,2] <= 17), 3], q=0.125)
Pre_2000_Week9 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==10) & (flow_data[:,2] >= 18) & (flow_data[:,2] <= 24), 3], q=0.125)
Pre_2000_Week10 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==10) & (flow_data[:,2] >= 25) & (flow_data[:,2] <= 31), 3], q=0.125)
Pre_2000_Week11 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==11) & (flow_data[:,2] >= 1) & (flow_data[:,2] <= 7), 3], q=0.125)
Pre_2000_Week12 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==11) & (flow_data[:,2] >= 8) & (flow_data[:,2] <= 14), 3], q=0.125)
Pre_2000_Week13 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==11) & (flow_data[:,2] >= 15) & (flow_data[:,2] <= 21), 3], q=0.125)
Pre_2000_Week14 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==11) & (flow_data[:,2] >= 22) & (flow_data[:,2] <= 28), 3], q=0.125)
Pre_2000_Week15 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==11) & (flow_data[:,2] >= 29) & (flow_data[:,2] <= 30), 3], q=0.125)
Pre_2000_Week15_2 = np.quantile(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==12) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3], q=0.125)
Pre_2000_Week15= (Pre_2000_Week15*2 + Pre_2000_Week15_2*5)/7

Pre_2000_Week16 = np.mean(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==12) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])



# %%
# Creates a list for Graphing
Pre_2000_Weeklypred= []

Pre_2000_Weeklypred.append(Pre_2000_Week1)
Pre_2000_Weeklypred.append(Pre_2000_Week2)
Pre_2000_Weeklypred.append(Pre_2000_Week3)
Pre_2000_Weeklypred.append(Pre_2000_Week4)
Pre_2000_Weeklypred.append(Pre_2000_Week5)
Pre_2000_Weeklypred.append(Pre_2000_Week6)
Pre_2000_Weeklypred.append(Pre_2000_Week7)
Pre_2000_Weeklypred.append(Pre_2000_Week8)
Pre_2000_Weeklypred.append(Pre_2000_Week9)
Pre_2000_Weeklypred.append(Pre_2000_Week10)
Pre_2000_Weeklypred.append(Pre_2000_Week11)
Pre_2000_Weeklypred.append(Pre_2000_Week12)
Pre_2000_Weeklypred.append(Pre_2000_Week13)
Pre_2000_Weeklypred.append(Pre_2000_Week14)
Pre_2000_Weeklypred.append(Pre_2000_Week15)
Pre_2000_Weeklypred.append(Pre_2000_Week16)
print(Pre_2000_Weeklypred)

#%%
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

plt.scatter(x=weeks, y=Pre_2000_Weeklypred, marker='o', label='predicted flow');
plt.xlabel('Week (#)')
plt.ylabel('Flow (cfs)');
plt.ylim([0, 250])
plt.title('Pre_2000_Weekly Discharge Prediction');
plt.legend()
plt.savefig('Pre_2000_Discharge_Prediction.png')

#%%
#Question 3
tot_Week2 = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3]
tot_Week2_2 = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3]

tot_Week3= flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3]
tot_Week4= flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3]
tot_Week5 = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3]
tot_Week6 = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3]

Week2_n = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31) & (flow_data[:,3] > weeklypred[1]), 3]
Week2_n_2 = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5) & (flow_data[:,3] > weeklypred[1]), 3]

Week3_n = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12) & (flow_data[:,3] > weeklypred[2]), 3]
Week4_n = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19) & (flow_data[:,3] > weeklypred[3]), 3]
Week5_n = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26) & (flow_data[:,3] > weeklypred[4]), 3]
Week6_n = flow_data[(flow_data[:,0]<=2000) & (flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30) & (flow_data[:,3] > weeklypred[5]), 3]

print((Week2_n.size+Week2_n_2.size)/(tot_Week2.size+tot_Week2_2.size))
print(Week3_n.size/tot_Week3.size)
print(Week4_n.size/tot_Week4.size)
print(Week5_n.size/tot_Week5.size)


print(Week2_n.size+Week2_n_2.size)
print(Week3_n.size)
print(Week4_n.size)
print(Week5_n.size)
# %%
# 2 week forcast
filename = 'streamflow_week4.txt'
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
#This cell finds the Fraction of summer 2020 flow to that of summer flow before the year 2000
mean_2020_summer_1= np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==6),3])
mean_2020_summer_2= np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==7),3])
mean_2020_summer_3= np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==8) & (flow_data[:,2] <= 21),3])
mean_2020_summer=(mean_2020_summer_1 + mean_2020_summer_2 + mean_2020_summer_3)/3

mean_summer_1 = np.mean(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,0] <=2019) & (flow_data[:,1]==6),3])
mean_summer_2 = np.mean(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,0] <=2019) & (flow_data[:,1]==7),3])
mean_summer_3 = np.mean(flow_data[(flow_data[:,0]<=2000) & (flow_data[:,0] <=2019) & (flow_data[:,1]==8) & (flow_data[:,2] <= 21),3])
mean_summer=(mean_summer_1 + mean_summer_2 + mean_summer_3)/3

mean_summer1_fraction= mean_2020_summer_1/ mean_summer_1
mean_summer2_fraction= mean_2020_summer_2/ mean_summer_2
mean_summer3_fraction= mean_2020_summer_3/ mean_summer_3
mean_summer_fraction= mean_2020_summer/ mean_summer
print(mean_summer_fraction)
print(mean_summer1_fraction)
print(mean_summer2_fraction)
print(mean_summer3_fraction)
#%%
# Finds each weeks mean value for 2020
Week1_mean_2020 = np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3])
Week2_mean_2020 = np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3])
Week2_mean_2_2020 = np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week2_mean_2020= (Week2_mean_2020*2 + Week2_mean_2_2020*5)/7

Week3_mean_2020 = np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])
Week4_mean_2020 = np.mean(flow_data[(flow_data[:,0] ==2020) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3])

# Finds each weeks mean value for years prior to 2020
Week1_mean_f = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==8) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 29), 3])
Week2_mean_f = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==8) & (flow_data[:,2] >= 30) & (flow_data[:,2] <= 31), 3])
Week2_mean_2_f = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==9) & (flow_data[:,2] >= 0) & (flow_data[:,2] <= 5), 3])
Week2_mean_f= (Week2_mean_f*2 + Week2_mean_2_f*5)/7

Week3_mean_f = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==9) & (flow_data[:,2] >= 6) & (flow_data[:,2] <= 12), 3])
Week4_mean_f = np.mean(flow_data[(flow_data[:,0] <=2019) & (flow_data[:,1]==9) & (flow_data[:,2] >= 13) & (flow_data[:,2] <= 19), 3])
#fractions 
Week1_frac= Week1_mean_2020/Week1_mean_f
Week2_frac= Week2_mean_2020/Week2_mean_f
Week3_frac= Week3_mean_2020/Week3_mean_f
Week4_frac= Week4_mean_2020/Week4_mean_f
average_frac= (Week1_frac + Week2_frac + Week3_frac + Week4_frac)/4
#%%
print(Week1_mean_f)
print(Week2_mean_f)
print(Week3_mean_f)
print(Week4_mean_f)
#%%
#print
print(Week1_frac)
print(Week2_frac)
print(Week3_frac)
print(Week4_frac)
print(average_frac)
# %%
# applying fraction to the next 2 weeks
Week1_m = np.mean(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 20) & (flow_data[:,2] <= 26), 3])
Week2_m = np.mean(flow_data[(flow_data[:,1]==9) & (flow_data[:,2] >= 27) & (flow_data[:,2] <= 30), 3])
#compared weekly means to first 4 weeks of semester to determine if lo and high flow spliting is required or not
print(Week1_m)
print(Week2_m)
#%%
# Hi and Lo flow spliting of fraction
Hi_flo_frac= (Week1_frac + Week3_frac)/2
Lo_flo_frac= (Week2_frac + Week4_frac)/2
# week 1 had Hi flow where Week2 had low flow
week1_forecast= Week1_m * Hi_flo_frac
week2_forecast= Week2_m * Lo_flo_frac

print()
print(week1_forecast)
print(week2_forecast)
# %%
