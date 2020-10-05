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
yearly = {}
#yearly = []
for i in range(1990,2021):
    yearly['%d'%i] = [data.flow[(data.year == i)]]
    # year = [yearly.get('%i'%i)]
# print(yearly)

# %%
yearly = pd.DataFrame.from_dict(yearly, orient='index', columns= ['2020'])
# %%
import concat from pandas
#%%
yearly.dtypes
#%%
#yearlytest['2020'] = yearly['2020'].astype(int)
yearly.to_excel(r'C:\Course_Materials\Yearly.xlsx', index = False)

# %%
