import numpy as np
import pandas as pd


labels = ['a', 'b', 'c']    # Normal Array
my_data = [10, 20, 30]      # Normal Array
arr = np.array(my_data)     # Numpy Array
da = dict(zip(labels, my_data))  # dictionary

# Series
print(pd.Series(my_data))  # this is have single arrar with default index 0,1,2
"""
0    10
1    20
2    30
dtype: int64
"""
print(pd.Series(my_data, labels))  # replace in index with labesl
"""
a    10
b    20
c    30
dtype: int64
"""
print(pd.Series(da))  # create data with dictonary

# create series
s1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
s2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(s1 + s2)  # Add the values from each other
print(s1 - s2)  # subtract the values from each other

#  Dataframe
np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), [
                  'A', "B", 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df[['W', 'Y']])  # selecting the columns
df['NEW'] = 1          # Adding new column
print(df)              # printing the dataframe
df.drop('NEW', axis=1, inplace=True)  # droping the column in same dataframe
print(df)  # printing the dataframce
print(df.drop('E', axis=0))  # droping the E row

print(df.loc['A'])   # Selcting the row
print(df.iloc[0])   # Selcting the row
print(df.loc['A', 'Y'])
print(df.loc[['A', 'B'], ['Y', 'Z']])
