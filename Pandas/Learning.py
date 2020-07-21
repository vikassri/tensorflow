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


# Conditional Selection
print(df)
print(df[df > 0])  # check the condition in dataframce
print(df[df['Z'] > 0]['X'])
print(df[df['Z'] > 0][['X', 'Y']])
print(df[(df['Z'] > 0) & (df['X'] > 1)])  # conditional selection
print(df.reset_index())
print(df)


# Multi Index
outside = "G1 G1 G1 G2 G2 G2".split(' ')
print(outside)
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# print
print(hier_index)
df = pd.DataFrame(np.random.randn(6, 2), hier_index, ['A', 'B'])
df.index.names = ['group', 'name']
print(df)
"""
                   A         B
group name
G1    1     0.302665  1.693723
      2    -1.706086 -1.159119
      3    -0.134841  0.390528
G2    1     0.166905  0.184502
      2     0.807706  0.072960
      3     0.638787  0.329646
              A         B
"""
df.loc['G1'].loc[[1]]['B']  # selecting the B first value

# cross-section
print(df.xs(1, level='name'))   # select the level 1 and
"""
group
G1     0.302665  1.693723
G2     0.166905  0.184502
"""

# Missing Data

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)
print(df.dropna())   # drop the rows with na values
print(df.dropna(axis=1))  # drop the columns with na values
# threshold is 2, to delete the row it should have 2 na
print(df.dropna(thresh=2))
print(df.fillna(value=df.mean()))   # fill the na with mean values

# Group By / Agg. methods
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 129, 240, 124, 243, 350]}
df = pd.DataFrame(data)
print(df.groupby('Company').sum())
print(df.groupby('Company').sum().loc['FB'])
print(df.groupby('Company').count())
print(df.describe().transpose())


# Merging, Joining and Concatenating
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'], 'C': [
                   'C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}, index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 'B': ['B4', 'B5', 'B6', 'B7'], 'C': [
                   'C4', 'C5', 'C6', 'C7'], 'D': ['D4', 'D5', 'D6', 'D7']}, index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'], 'B': ['B8', 'B9', 'B10', 'B11'], 'C': [
                   'C8', 'C9', 'C10', 'C11'], 'D': ['D8', 'D9', 'D10', 'D11']}, index=[8, 9, 10, 11])

print(pd.concat([df1, df2, df3]))        # vertically
print(pd.concat([df1, df2, df3], axis=1))  # Horizontally

left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'], 'C': [
    'C0', 'C1', 'C2', 'C3'], 'key': ['K1', 'K2', 'K3', 'K4']}, index=[0, 1, 2, 3])
right = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 'B': ['B4', 'B5', 'B6', 'B7'], 'C': [
                     'C4', 'C5', 'C6', 'C7'], 'key': ['K1', 'K2', 'K3', 'K4']}, index=[4, 5, 6, 7])

print(left)
print(right)

# Merge use columns
# merge on basis of common key, there are many method like inner/outer/left/right
print(pd.merge(left, right, how='inner', on='key'))

# Joining, use index instead of columns
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'], 'C': [
    'C0', 'C1', 'C2', 'C3'], 'K': ['K1', 'K2', 'K3', 'K4']}, index=[0, 1, 2, 3])
right = pd.DataFrame({'A1': ['A4', 'A5', 'A6', 'A7'], 'B1': ['B4', 'B5', 'B6', 'B7'], 'C1': [
                     'C4', 'C5', 'C6', 'C7'], 'K1': ['K1', 'K2', 'K3', 'K4']}, index=[0, 1, 6, 7])

print(left.join(right))

# Operations
df1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [444, 555, 666, 444], 'C': [
                   'abe', 'def', 'ghi', 'xyz']}, index=[0, 1, 2, 3])
print(df1)
print(df1['B'].unique())     # find the unique values
print(df1['B'].nunique())    # number of unique values
print(df1['B'].value_counts())  # count of unique values

print(df1[df1['A'] > 2])    # filter the df
# apply function


def times2(x):
    return x*2


print(df1['A'].apply(times2))  # apply the method to all the values of column A
# apply the method to all the values of column A
print(df1['A'].apply(lambda x: x*2))

# Sorting
print(df1.sort_values(by='B'))

# Data intpu and output
# converting csv into json
df = pd.read_csv('Pandas/data.csv',
                 names=['a', 'b', 'c']).to_json('Pandas/data.json')

# reading from url
df = pd.read_html('https://www.fdic.gov/Bank/individual/failed/banklist.html')
print(df[0].head())
