import numpy as np

a = np.arange(12) ** 2
print(a)  # [  0   1   4   9  16  25  36  49  64  81 100 121]

# simple index
print(a[0], a[4], a[7])  # 0 16 49

# complex index, creating 1D numpy array with list or numpy array of index
# for creating numpy array we can pass list or another numpy array as index

index_1 = [0, 4, 7]
print(index_1, type(index_1))  # [0, 4, 7] <class 'list'>
print(a[index_1], type(a[index_1]))  # [ 0 16 49] <class 'numpy.ndarray'>

index_2 = np.array([0, 4, 7])
print(index_2, type(index_2))  # [0 4 7] <class 'numpy.ndarray'>
print(a[index_2], type(a[index_2]))  # [ 0 16 49] <class 'numpy.ndarray'>

print(a[[0, 1, 2]], type(a[[0, 1, 2]]))  # [0 1 4] <class 'numpy.ndarray'>

# complex index, creating 2D array, by passing 2D index array to 1D numpy array
# final array does not depends upon original array, it depends upon (array of index)
index_3 = np.array([[1, 4], [8, 3]])
print(index_3, type(index_3))  # [[1, 4], [8, 3]] <class 'numpy.ndarray'>
print(a[index_3], type(a[index_3]))  # [[1, 16], [64, 9]] <class 'numpy.ndarray'>

b = np.arange(12).reshape(3,4)**2
print(b)
row = np.array([[0, 2], [1, 2]])
col = np.array([[0, 0], [3, 3]])
print(b[row,col])
# [[  0  64]     b[0, 0], b[2, 0]
#  [ 49 121]]    b[1, 3], b[2, 3]
print(b[0, 0], b[2, 0], b[1, 3], b[2, 3])  # 0 64 49 121

# row and col are both are of same shape. Now lets assign some values
b[row,col] = -100
print(b)
# This way can update multiple individual elements using single assignment
# We can assign multiple value in 1D array using this method as well
a = np.arange(12) ** 2
print(a)  # [  0   1   4   9  16  25  36  49  64  81 100 121]
index_1 = [0, 4, 7]
a[index_1] = 999
print(a)  # [999   1   4   9 999  25  36 999  64  81 100 121]

for i in np.nditer(a[a > 100]):  # Its called conditional indexing, notice the indexing with the array name inside []
    print(i)

# Indexing with Boolean
a = np.arange(16).reshape(4,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
index_b1 = a > 9  # here we are creating boolean index array with condition on original array
print(index_b1)
# Result of conditional evaluation on numpy array is array of boolean with the same shape as the original
print(a[index_b1])  # [10 11 12 13 14 15]  # it is same as a[a > 9]
print(a[a > 9])

index_b2 = a < 6
print(index_b2)

print(np.count_nonzero(index_b2))  # 6 : since True is considered as non-zero
print(np.sum(a < 6))  # 6 it will again sum/count of elements (not its value) which matches the condition

print(np.sum((a < 6), axis=1))  # [4 2 0 0] # row wise conditional index
print(np.sum((a < 6), axis=0))  # [2 2 1 1] # col wise conditional index

print(np.any(a > 50))  # False  # if any elements satisfy the condition
print(np.all(a < 50))  # True  # if all elements satisfy the condition

# if we use axis parameter, it will always results in either row wise or column wise computation data

print(np.any((a > 10), axis=1))  # [False, False, True, True]  # if any elements satisfy the condition row wise
print(np.any((a > 10), axis=0))  # [True, True, True, True]  # if any elements satisfy the condition row wise

# np.concatenate, np.stack, np.hstack, np.vstack
# above methods can be used to merge two arrays, concatenate and stack both require axis parameter for the direction
