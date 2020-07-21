import numpy as np

# simple array
arr = np.array(range(0, 10))
print(arr)

# matrix (4x4)
mat = np.array([range(0, 4), range(4, 8), range(8, 12)])
print(mat)

# np arange , similar to simple array
print(np.arange(0, 10))

# with Step of two
print(np.arange(0, 10, 2))

# Np zeros and ones
print(np.zeros((2, 3)))  # matrix of 2x3
print(np.ones((2, 3)))  # matrix of 2x3

# linear spacing
print(np.linspace(0, 5, 5))  # 10 evenly distributed points from 0, 5

# eyes matrix or identity matrics
print(np.eye(3))
print(np.eye(4))

# random
print(np.random.rand(5))  # random distribution
print(np.random.randn(5))  # random  normal distribution
print(np.random.randint(10, 100, 16))  # get 15 randon number
arr = np.random.randint(10, 100, 16)
print(arr.reshape(4, 4))  # reshape to make a matrix

# Max/Min and locations
print(arr.min())  # minimum value of array
print(arr.max())  # maximum value of array
print(arr.argmax())  # maximum value index
print(arr.argmin())  # min value index

# shape of arr
print(arr.shape)  # current share of arr
print(arr.dtype)  # type of arr

# Indexing and Selection
arr = np.arange(0, 10)
print(arr[4:8])   # its similar to python indexing
print(arr[2:])   # rest of arr from 2nd index

# Broadcasting of value
arr[:3] = 100
print(arr)  # replace the value to [100 100 100   3   4   5   6   7   8   9]

# indexing in 2d array
arr_2d = np.array([range(0, 3), range(4, 7), range(8, 11)])
print(arr_2d)
"""
[[ 0  1  2]
 [ 4  5  6]
 [ 8  9 10]]
"""
# extract the 5 , we can see its at 1st (array starts from 0) row and 1st value
print(arr_2d[1, 1])

print(arr_2d[0, ])  # get first row
print(arr_2d[:, 1:2])  # middle column
print(arr_2d[1:, :2])  # both square 4, 5, 8, 9
print(arr_2d[:2, 1:])  # print 1, 2, 5, 6
print(arr_2d[1:, 1:])  # print 5,9, 6, 10

# Check the arr and do validation
arr = np.arange(0, 11)  # print 1,2,3,4,5,6,7,8,9,10
print(arr[arr > 5])
print(arr > 5)  # provide the true and false of value which are greater the 5

# Operations
print(arr + arr)  # add
print(arr - arr)  # minux
print(arr * arr)  # multiply
print(arr.sum())  # sum of the array
print(arr.std())  # std deviation
print(arr_2d.sum(axis=1))
