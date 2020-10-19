#%%
# input stuff
name = input('what is your name ')
animal = input('what is your favorite animal ')
print(name + "'s favorite animal is a " + animal)

# %%
#more input
weight = input('how much do you weigh in lbs? ')
print(0.453592*int(weight))

# %%
#formatted string
name = 'Jake'
print(f"{name}'s favorite animal is a {animal}")
list = [1,2,3,4,5,6]
print(3 in list)
# %%
name.replace('J',"M")
#%%
print(3 in list)
list = [1,2,3,4,5,6]
#shows operator trick that multiplies list by 3 and then returns to list
for i in range(6):
    list[i] *=3.3
print(list)
for i in range(6):
    list[i] *= 1
print(list)
# %%
print(abs(-1))
print(round(-1.5))


# %%
import math

# %%
math.degrees(3.14)
# %%
# else if and logical operators
credit= input('What is your credit score')
credit= int(credit)
income= input('what is your monthly income?')
income= int(income)
carprice= 30000
if credit >= 800 and income >= 50000:
    downpayment = 0.05
elif credit >= 700 or income >=35000:
    downpayment = 0.10
elif 700 > credit >= 500 or 35000> income >= 25000:
    downpayment = 0.15
else:
    downpayment = 1
downpayment *= carprice
print(f'Today you will pay ${downpayment}')


# %%
# come back and try to make a password name that requires sybol and number
# #password(input('password'))
# passphrase = []
# password = '50@six'
# #password = int(password[0])
# for i in range(5):
#     if int(password[i]) == BaseException:
#         passphrase = passphrase.append('True')
#     # else:
#     #     passphrase = passphrase.append('False')
# print(passphrase)


# %%
# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
#%%
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

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
# yearly = {}
#yearly = []
for i in range(1990,2021):
    yearly['%s'%i] = [data.flow[('year'[] == i)]]
    # year = [yearly.get('%i'%i)]
# print(yearly)

# %%
yearly = pd.DataFrame.from_dict(yearly, orient='index', columns= ['2020'])
# %%
import concat from pandas
#%%
#yearlytest = yearly.astype(str)
yearlytest= yearlytest.astype(int)
#%%
#yearlytest['2020'] = yearly['2020'].astype(int)
yearly.to_excel(r'C:\Course_Materials\Yearly1.xlsx', index = False)

# %%
data2= data.copy()

for i in range(1989,2021):
    data2['%i'%i] = data.flow[data.year == i]
#%%
myguess = 3
if myguess == 3:
        print(f"let's see what's behind door # {myguess} you were incorrect")
else:
        print(f"let's see what's behind door # {myguess} you are a winnner")
# %%
myguess = input('which door would you like to choose')
myguess = int(myguess)
if myguess == 3:
        print(f"let's see what's behind door # {myguess} you were incorrect")
else:
        print(f"let's see what's behind door # {myguess} you are a winnner")
#%%
#%%
# data2= data.copy()
# months = []

# for i in range(1,13):
#     data2['%i'%i] = data.flow[data.month == i].dropna()
#     months.append('%i'%i)
    
#%%
# data_to_plot = [ data2['7'].dropna(), data2['8'].dropna(), data2['9'].dropna(), data2['10'].dropna(), data2['11'].dropna(), data2['12'].dropna()]

# fig = plt.figure(1, figsize=(9, 6))

# # Create an axes instance
# ax = fig.add_subplot(111)

# # Create the boxplot
# bp = ax.boxplot(data_to_plot)
# plt.ylim([0, 500])
# plt.title('Discharge Boxplot');
# ax.set_xticklabels(months[6:])
# # plt.xticks(rotation=45,fontsize=12)
# fig.savefig('BoxPlots.png', bbox_inches='tight')
#%%
#%%

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt



# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x =train['flow']
# y = train['flow_tm1']
# z =train['flow_tm2']

# my_cmap = plt.get_cmap('hsv')

# x5= ax.scatter(x, y, z, c= (x+y+z), cmap = my_cmap, marker='o')


# fig.colorbar(x5, ax = ax, shrink = 0.5, aspect = 5)
# ax.set_xlabel('flow t')
# ax.set_ylabel('flow t-1')
# ax.set_zlabel('flow t-2')

# plt.show()
# %%
# predictions over time
forecasts_1=np.zeros([nstudent,len(weeks)])
forecasts_2=np.zeros([nstudent,len(weeks)]) # The 2week forecasts for this week

for i in range(nstudent):
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    for n in range(1, forecast_week+1):
        forecasts_1[i,n-1] = temp.loc[(n), '1week']
        forecasts_2[i,n-1] = temp.loc[(n), '2week']

# %%
# compiled into data frames you can use for graphing
weekly_forecast1w = pd.DataFrame({}, index=firstnames)
weekly_forecast2w = pd.DataFrame({}, index=firstnames)

for i in range(16):
    weekly_forecast1w.insert(i,'week_%s'%(i+1), forecasts_1[:,i], True)
    weekly_forecast2w.insert(i,'week_%s'%(i+1), forecasts_2[:,i], True)