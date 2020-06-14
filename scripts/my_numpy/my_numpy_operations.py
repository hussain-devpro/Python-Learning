import numpy as np
import pprint as pp

a = np.array([10, 10, 10])
b = np.array([5,5,5])

# All math operation will be performed element wise if arrays have same shape
pp.pprint(a+b)  # array([15, 15, 15])
pp.pprint(a-b)  # array([5, 5, 5])
pp.pprint(a*b)  # array([50, 50, 50])
pp.pprint(a/b)  # array([2., 2., 2.])
pp.pprint(a//b)  # array([2, 2, 2], dtype=int32)
pp.pprint(a**b)  # array([100000, 100000, 100000], dtype=int32)
pp.pprint(a%b)  # array([0, 0, 0], dtype=int32)

# Math operation can be performed with scalar value as well, It will be applied to all elements of arrary
pp.pprint(a+3)  # array([13, 13, 13])
pp.pprint(a-3)  # array([7, 7, 7])
pp.pprint(a*3)  # array([30, 30, 30])
pp.pprint(a/3)  # array([3.33333333, 3.33333333, 3.33333333])
pp.pprint(a//3)  # array([3, 3, 3], dtype=int32)
pp.pprint(a**3)  # array([1000, 1000, 1000], dtype=int32)
pp.pprint(a%3)  # array([1, 1, 1], dtype=int32)

# Conditional expression can be performed with each element of array as well
pp.pprint(a < 3)  # array([False, False, False])
pp.pprint(a == 10)  # array([True, True, True])

# Operation on multi-dimensional array of same size will also be element wise
A = np.array([[1,2], [3,4]])
B = np.array([[1,0], [2,0]])

print(A.shape, B.shape)

pp.pprint(A * B)  # array([[1, 0], [6, 0]])
pp.pprint((A + B) % 2)  # array([[0, 0], [1, 0]], dtype=int32)  # we can combine Array and Scalar operations as well

# If we want to perform matrix multiplication then we need to use following function.
pp.pprint(np.dot(A,B))   # array([[ 5,  0], [11,  0]])

a = np.array([1,2,3,4,5,6])
print(sum(a), min(a), max(a))  # 21 1 6 # These functions are performed in similar way to any iterables for 1D array
print(a.sum(), a.min(), a.max())  # 21 1 6 another way to do above operations

# For 2D array we get following result
A = np.array([[1,2], [3,4]])
print(sum(A), A.sum())  # [4 6], 10
# A:  1, 2    sum(A) => [4,6]  It will add all the values of column from top to bottom
#     3, 4    A.sum() => 10    It will add all the values of the array


A = np.array(np.arange(12)).reshape((3,4))
pp.pprint(A)

print(A.sum(axis=0))  # it will add all the columns # [12 15 18 21]
print(A.sum(axis=1))  # it will add all the rows # [6, 22, 38] # since its a last index so axis=-1 => # [6, 22, 38]
print(A.sum(axis=-1))  # numpy.AxisError: axis 2 is out of bounds for array of dimension 2

# axis parameter can be applied to min/max function
print(A.min(axis=0), A.max(axis=1))  # A.min => [0,1,2,3]       A.max => [3, 7, 11]

# trigonometric operations are available in numPy
angles_degrees = np.array([0, 30, 45, 60, 90])
angle_radians = angles_degrees * np.pi/180
pp.pprint(angle_radians)
# performing sin operations
pp.pprint(np.sin(angle_radians))
# other functions which are available are, np.cos, np.tan, np.degrees etc

# Statistical functions are also available
data = np.array([1,2,3,4,9,10])
print(np.mean(data))  # 45  1+2+3+4+9+10/6  => 4.8333   # mean and average are the same thing
print(np.median(data)) # 3.5
# To calculate the median Arrange your numbers in numerical order. Count how many numbers you have. If you have an
# odd number, divide by 2 and round up to get the position of the median number. If you have an even number, divide
# by 2. Go to the number in that position and average it with the number in the next higher position to get the median.

# We can create array from data sets as well
salaries = np.genfromtxt('numpy_dataset/salary.csv', delimiter=',')
pp.pprint(salaries)  # read the data from file:  array([60000., 58000., 56967., ..., 54647., 25000., 70000.])
print(salaries.shape)  # (1147, )   # it means its 1D array with total number of elements as 1147
print(f'Average Salary: {np.mean(salaries)} \n'
      f'Minimum Salary: {np.min(salaries)}  \n'
      f'Maximum Salary: {np.max(salaries)}  \n'
      f'Median Salary: {np.median(salaries)} \n'
      f'Standard Deviation {int(np.std(salaries))}  \n'
      f'Variance {int(np.var(salaries))}')

print(np.argmax(salaries))  # prints the index of highest salary
print(np.argmin(salaries))  # prints the index of lowest salary
print(np.argsort(salaries))  # prints the array of indexes of sorted salary
# multiple sorting algo can be specified using kind parameter with argsort
print(np.argsort(salaries, kind='mergesort'))  # prints the array of indexes of sorted salary
print(np.where(salaries > 100))
condition = salaries > np.mean(salaries)
print(np.extract(condition, salaries))
