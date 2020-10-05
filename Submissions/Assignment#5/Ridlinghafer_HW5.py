# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

#filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :) 
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

#%%
week_1= '8/23-8/29'
week_2= '8/30-9/5'
week_3= '9/6-9/12'
week_4='9/13-9/19'
week_5= '9/20-9/26'
week_6= '9/27-10/3'
week_7= '10/4-10/10'
week_8= '10/11-10/17'
week_9= '10/18-10/24'
week_10= '10/25-10/31'
week_11= '11/1-11/7'
week_12= '11/8-11/14'
week_13= '11/15-11/21'
week_14= '11/22-11/28'
week_15= '11/29-12/5'
week_16= '12/6-12/12'
weeks=[]
weeks= [week_1,week_2,week_3,week_4,week_5,week_6,week_7,week_8,week_9,week_10,week_11,week_12,week_13,week_14,week_15,week_16]

# %%
week1 = data[(data.month == 8) & (data.day >= 23) & (data.day <= 29)]
week2 = data[((data.month == 8) & (data.day >= 30) & (data.day <= 31))]
week2 = week2.append(data[(data.month == 9) & (data.day >= 0) & (data.day <= 5)])
week3 = data[((data.month == 9) & (data.day >= 6) & (data.day <= 12))]
week4 = data[((data.month == 9) & (data.day >= 13) & (data.day <= 19))]
week5 = data[((data.month == 9) & (data.day >= 20) & (data.day <= 26))]
week6 = data[((data.month == 9) & (data.day >= 27) & (data.day <= 31))]
week6 = week6.append(data[(data.month == 10) & (data.day <= 3)])
week7 = data[((data.month == 10) & (data.day >= 4) & (data.day <= 10))]
week8 = data[((data.month == 10) & (data.day >= 11) & (data.day <= 17))]
week9 = data[((data.month == 10) & (data.day >= 18) & (data.day <= 24))]
week10 = data[((data.month == 10) & (data.day >= 25) & (data.day <= 31))]
week11 = data[((data.month == 11) & (data.day >= 0) & (data.day <= 7))]
week12 = data[((data.month == 11) & (data.day >= 8) & (data.day <= 14))]
week13 = data[((data.month == 11) & (data.day >= 15) & (data.day <= 21))]
week14 = data[((data.month == 11) & (data.day >= 22) & (data.day <= 28))]
week15 = data[((data.month == 11) & (data.day >= 29) & (data.day <= 31))]
week15 = week15.append(data[(data.month == 12) & (data.day <= 5)])
week16 = data[((data.month == 12) & (data.day >= 6) & (data.day <= 12))]
# %%
data_to_plot = [week1.flow, week2.flow, week3.flow, week4.flow, week5.flow, week6.flow, week7.flow, week8.flow, week9.flow, week10.flow, week11.flow, week12.flow, week13.flow, week14.flow, week15.flow, week16.flow]
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.ylim([0, 500])
plt.title('Weekly Discharge Boxplot');
ax.set_xticklabels(weeks)
plt.xticks(rotation=45,fontsize=12)
fig.savefig('BoxPlots.png', bbox_inches='tight')
# %%
yearly = data[(data.month < 8) & (data.month > 6)]
yearly = yearly.append(data[(data.month == 8) & (data.day <= 21)])
# %%
x=yearly.groupby('year')['flow'].describe()
y=yearly.groupby('year')['year'].mean()
# y1= yearly.groupby('year')['flow'].mean()
# y2= yearly.groupby('year')['flow'].min()
# y3= yearly.groupby('year')['flow'].quantile(q=0.25)
# y4=[]
# for i in range(32):
#         y4.append(47)
# print(y4)


#%%
# %matplotlib inline
# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# import numpy as np

# #plt.scatter(x=y, y= y1, marker='o', label='mean');
# #plt.scatter(x=y, y= y2, marker='o', label='min');
# plt.scatter(x=y, y= y3, marker='o', label='lowQ');
# plt.scatter(x=y, y= y4, marker='o', label='mean');

# plt.ylabel('Flow (cfs)');
# plt.ylim([0, 100])
# plt.title('Weekly Discharge Prediction');
# plt.xticks(rotation=45,fontsize=10)
# plt.legend()
# plt.savefig('Discharge_Prediction.png')
# %%
yearly = data[(data.month < 8) & (data.month > 6) & (data.year >=2011) & (data.year <=2016)]
yearly = yearly.append(data[(data.month == 8) & (data.day <= 21) & (data.year >=2011) & (data.year <=2016)])
yearly = yearly.append(data[(data.month == 8) & (data.day <= 21) & (data.year ==2019)])
yearly = yearly.append(data[(data.month < 8) & (data.month > 6) & (data.year ==2019)])
# %%
xmean=yearly.groupby('year')['flow'].mean()
print(xmean)
# %%
x1=yearly.groupby('year')['flow'].quantile(0.09)
print(x1.mean())
x2=yearly.groupby('year')['flow'].quantile(0.1)
print(x2.mean())
x3=yearly.groupby('year')['flow'].quantile(0.11)
print(x3.mean())
#%%
 yearly = data[(data.year >=2011) & (data.year <=2016)]
 yearly = yearly.append(data[(data.year ==2019)])
#%%
week1 = yearly[(yearly.month == 8) & (yearly.day >= 23) & (yearly.day <= 29)]
week2 = yearly[((yearly.month == 8) & (yearly.day >= 30) & (yearly.day <= 31))]
week2 = week2.append(yearly[(yearly.month == 9) & (yearly.day >= 0) & (yearly.day <= 5)])
week3 = yearly[((yearly.month == 9) & (yearly.day >= 6) & (yearly.day <= 12))]
week4 = yearly[((yearly.month == 9) & (yearly.day >= 13) & (yearly.day <= 19))]
week5 = yearly[((yearly.month == 9) & (yearly.day >= 20) & (yearly.day <= 26))]
week6 = yearly[((yearly.month == 9) & (yearly.day >= 27) & (yearly.day <= 31))]
week6 = week6.append(yearly[(yearly.month == 10) & (yearly.day <= 3)])
week7 = yearly[((yearly.month == 10) & (yearly.day >= 4) & (yearly.day <= 10))]
week8 = yearly[((yearly.month == 10) & (yearly.day >= 11) & (yearly.day <= 17))]
week9 = yearly[((yearly.month == 10) & (yearly.day >= 18) & (yearly.day <= 24))]
week10 = yearly[((yearly.month == 10) & (yearly.day >= 25) & (yearly.day <= 31))]
week11 = yearly[((yearly.month == 11) & (yearly.day >= 0) & (yearly.day <= 7))]
week12 = yearly[((yearly.month == 11) & (yearly.day >= 8) & (yearly.day <= 14))]
week13 = yearly[((yearly.month == 11) & (yearly.day >= 15) & (yearly.day <= 21))]
week14 = yearly[((yearly.month == 11) & (yearly.day >= 22) & (yearly.day <= 28))]
week15 = yearly[((yearly.month == 11) & (yearly.day >= 29) & (yearly.day <= 31))]
week15 = week15.append(yearly[(yearly.month == 12) & (yearly.day <= 5)])
week16 = yearly[((yearly.month == 12) & (yearly.day >= 6) & (yearly.day <= 12))]
# %%
data_to_plot = [week1.flow, week2.flow, week3.flow, week4.flow, week5.flow, week6.flow, week7.flow, week8.flow, week9.flow, week10.flow, week11.flow, week12.flow, week13.flow, week14.flow, week15.flow, week16.flow]
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.ylim([0, 500])
plt.title('Weekly Discharge Boxplot');
ax.set_xticklabels(weeks)
plt.xticks(rotation=45,fontsize=12)
fig.savefig('BoxPlots_lateryears.png', bbox_inches='tight')


#%%
week_q1 = week1.flow.quantile(0.11)
week_q2 = week2.flow.quantile(0.11)
week_q3 = week3.flow.quantile(0.11)
week_q4 = week4.flow.quantile(0.11)
week_q5 = week5.flow.quantile(0.11)
week_q6 = week6.flow.quantile(0.11)
week_q7 = week7.flow.quantile(0.11)
week_q8 = week8.flow.quantile(0.11)
week_q9 = week9.flow.quantile(0.11)
week_q10 = week10.flow.quantile(0.11)
week_q11 = week11.flow.quantile(0.11)
week_q12 = week12.flow.quantile(0.11)
week_q13 = week13.flow.quantile(0.11)
week_q14 = week14.flow.quantile(0.11)
week_q15 = week15.flow.quantile(0.11)
week_q16 = week16.flow.quantile(0.11)
data_to_plot = [week_q1, week_q2, week_q3, week_q4, week_q5, week_q6, week_q7, week_q8, week_q9, week_q10, week_q11, week_q12, week_q13, week_q14, week_q15, week_q16]



#%%
#data_to_plot = [week1, week2, week3, week4, week5, week6, week7, week8, week9, week10, week11, week12, week13, week14, week15, week16]

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

plt.scatter(x=weeks, y=data_to_plot, marker='o', label='predicted flow');

plt.ylabel('Flow (cfs)');
plt.ylim([0, 250])
plt.title('Weekly Discharge Prediction');
plt.xticks(rotation=45,fontsize=10)
plt.legend()
plt.savefig('Discharge_Prediction.png')
#%%
#data_to_plot = np.asarray(data_to_plot)
print(data_to_plot)
# %%
#Questions on HW

Q2=data.flow.describe()
Q3= data.groupby('month')['flow'].describe()#also Q5
Q4= data.sort_values('flow')
Q4_a= Q4.head(5)
Q4_b= Q4.tail(5)
Q6= data[(data.flow >= .95*week_q1) & (data.flow <= 1.05*week_q1)]
Q5max_index= data.groupby('month')['flow'].idxmax()
Q5max= data.groupby('month')['flow'].max()
Q5max_y= data.year.iloc[Q5max_index]
print([Q5max_y,Q5max])
Q5min_index= data.groupby('month')['flow'].idxmin()
Q5min= data.groupby('month')['flow'].min()
Q5min_y= data.year.iloc[Q5min_index]
print([Q5min_y,Q5min])

# %%
# from pandas import DataFrame
# monthly = pd.DataFrame(columns = ["month","flow","year"])
# monthly2 = pd.DataFrame(columns = ["month","flow","year"])
# Q5_a = []
# Q5_b = []
# for month in range(1,13):
#         Q= data[(data.month == month)]
#         max = Q.max()
#         min = Q.min()
#         data.loc(max.flow)
#         # idmax= Q.idxmax()
#         # idmin= Q.idxmin()
#         #Flow= Q.index(max())
#         #Q5_a.append(data.flow[(data.month == i)].max())
#         # Q5_b.append(data[(data.month == i)].min())
#         monthly = monthly.append({'month': month, 'flow': max.flow, 'year': data.year}, ignore_index=True)
#         monthly2 = monthly2.append({'month': month, 'flow': min.flow, 'year': data.year}, ignore_index=True)
#         # Q5_b = DataFrame (Q5_b,columns=['flow','year','month'])
# # print (Q5_a)
# #print (Q5_b)

        
                
#%%       
# Q5_a= data.pivot_table(index='year')
# Q5_b= data.groupby('month')['flow'].min()
# print(data.iloc[Q5_a])

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

#filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)
#%%
yearly = data[(data.month > 7) & (data.month < 9) & (data.year >=2011) & (data.year <=2016)]
yearly = yearly.append(data[(data.month == 9) & (data.day < 26) & (data.year >=2011) & (data.year <=2016)])
yearly = yearly.append(data[(data.month == 9) & (data.day < 26) & (data.year >=2019)])
yearly = yearly.append(data[(data.month > 7) & (data.month < 9) &(data.year >=2019)])

# %%
xmean=yearly.groupby('year')['flow'].mean()
print(xmean)

#%%
yearly = data[(data.month > 7) & (data.month < 9) & (data.year >=2011) & (data.year <=2016)]
yearly = yearly.append(data[(data.month == 9) & (data.day < 26) & (data.year >=2011) & (data.year <=2016)])
yearly = yearly.append(data[(data.month == 9) & (data.day < 26) & (data.year ==2019)])
yearly = yearly.append(data[(data.month > 7) & (data.month < 9) & (data.year ==2019)])
# %%
x1=yearly.groupby('year')['flow'].quantile(0.00)
print(x1.mean())
print(x1.std())
# x2=yearly.groupby('year')['flow'].quantile(0.02)
# print(x2.mean())
# x3=yearly.groupby('year')['flow'].quantile(0.03)
# print(x3.mean())
percent_error = 1.00+((47.882-x1.mean())/x1.mean())
#percent_error2 = 1.00+((47.882-(x1.mean()+x1.std()))/(x1.mean()+x1.std()))
print(percent_error)
#print(percent_error2)
#%%
#print((percent_error+percent_error2)/2)
#%%
#%%
yearly = data[(data.month > 7) & (data.year >=2011) & (data.year <=2016)]
yearly = yearly.append(data[(data.month > 7) & (data.year ==2019)])
# %%
week6 = yearly[((yearly.month == 9) & (yearly.day >= 27) & (yearly.day <= 31))]
week6 = week6.append(yearly[(yearly.month == 10) & (yearly.day <= 3)])
week7 = yearly[((yearly.month == 10) & (yearly.day >= 4) & (yearly.day <= 10))]
# %%
week_q6 = week6.flow.quantile(0)
week_q7 = week7.flow.quantile(0.0)
#multiplies by percent error
print(percent_error*week_q6)
print(percent_error*week_q7)
#%%
data.dtypes


# %%
