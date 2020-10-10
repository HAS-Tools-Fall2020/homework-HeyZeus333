# data = np.ones((7,3))
# data_frame = pd.DataFrame(data, 
#                 columns = ['data1', 'data2', 'data3'],
#                 index=['a','b','c','d','e','f','g'])
# A) Change the values for all of the vowel rows to 3

# B) multiply the first 4 rows by 7

# C) Make the dataframe into a checkerboard  of 0's and 1's using loc

# D) Do the same thing without using loc
#%%
import pandas as pd
import numpy as np
data=[]
data_frame = pd.DataFrame([[1, np.nan, 2],
                            [2, 3, 5],
                            [np.nan, 4, 6]])
# # 1) Use the function fill.na to fill the na values with 999
data_frame= data_frame.fillna(999)
# 2) Turn the 999 values back to nas. See how many different ways you can do this
data_frame[data_frame == 999] = np.nan




# 2) Turn the 999 values back to nas. See how many different ways you can do this

# %%
Given the following series of flow values and days Assume that the flow has uncertainty of +/- 25%
Come up with a way to visualize this information
flow = np.random.randn(100)
day = range(len(y_data))
