# NumPy package is fundamental package for scientific computing
# basic building block of NumPy is n-dimensional array

# Many math, science and engineering packages like SciPy, Pandas, Statsmodels etc are built on NumPy
# For development on windows, NumPy packages require Visual Studio Build Tools for C++

import numpy as np
import pprint as pp

# np.array will create a numpy ndarray
a = np.array([1,2,3,4])  # passing data as list
l = [1,2,3,4]
b = np.array((5,6,7,8))  # passing data as tuple
print(l, a, b, type(a), type(b))  # prints the array in square brackets and type of array is <class 'numpy.ndarray'>
# pp.pprint(l)  # it prints the list : [1, 2, 3, 4]
# pp.pprint(a)  # it prints the ndarray : array([1, 2, 3, 4])
array_of_zero = np.zeros((3, 4))  # it creates multi-dimensional array with desired shape i.e. 3 rows and 4 columns
pp.pprint(array_of_zero)  # it also initializes all elements with 0
# we can specify the shape with list as well. It will not impact anything for ex. np.zeros([3,4])

array_of_one = np.ones((3, 4), dtype=np.int16)  # similar to np.zeros but it initializes the array with value as 1
pp.pprint(array_of_one)  # we can specify the the type of data as well through dtype parameter

array_of_epmty = np.empty((3,4))  # it creates empty array
pp.pprint(array_of_epmty)

# array_of_zero and array_of_empty, both are initializes with 0. Following results in Pass.
if array_of_zero.all() == array_of_epmty.all():
    print("Pass")
else:
    print("Fail")

# np.eye allows us to create square matrix with 1 along the diagonal and 0 else where.
array_of_eye = np.eye(4)
pp.pprint(array_of_eye)  # diagonal starts from Top Left to Bottom right

array_of_even = np.arange(2, 20, 2)  # its a-range not arrange, start is included, but end is excluded, last arg is step
pp.pprint(array_of_even)  # array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])

array_of_odd = np.arange(1, 20, 2)
pp.pprint(array_of_odd)  # array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

array_of_sequence = np.arange(1, 10)  # step argument is optional, default value is 1
pp.pprint(array_of_sequence)  # array([1, 2, 3, 4, 5, 6, 7, 8, 9])

array_of_small_sequence = np.arange(6)  # start argument is also optional, default value is 0
pp.pprint(array_of_small_sequence)  # array([0, 1, 2, 3, 4, 5])

array_of_float = np.arange(0, 2, 0.3)  # step size can be float as well
pp.pprint(array_of_float)  # array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])

# numpy can create 2-d array if we pass list of lists or list of tuples etc
array_2d = np.array([[1,2,3], (4,5,6)])
pp.pprint(array_2d)

# every numpy array has shape attributes, through which we can find out its dimensions
print(array_2d.shape)  # results in (2,3) i.e. 2 rows 3 columns

# we can convert shape of the arrays as well
array_3r2c = array_of_small_sequence.reshape((3,2))
pp.pprint(array_3r2c)
# array([[0, 1],
#        [2, 3],
#        [4, 5]])

# While reshaping if exact elements are not available, it will results in error
# array_4r2c = array_of_small_sequence.reshape((4,2))  # ValueError: cannot reshape array of size 6 into shape (4,2)
# array_2r2c = array_of_small_sequence.reshape((2,2))  # ValueError: cannot reshape array of size 6 into shape (2,2)

# if already know the shape of array, and We would like to create an array in similar dimension
array_3r2c_copy = np.ones_like(array_3r2c)  # it will create the array but it will initialize it with 1
pp.pprint(array_3r2c_copy)
