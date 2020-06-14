# Iterating over numpy 1D array is similar to list
import numpy as np

a = np.arange(11)**2  # [  0   1   4   9  16  25  36  49  64  81 100]
for i in a:
    print(i**(1/2))  # print 0, 1, .. 10

# Iterating over 2D array
s = np.array([[71, 29, 84, 12],
              [90, 63, 15, 70],
              [42, 56, 87, 64]])
for i in s:
    print(i)  # it will print each row, which itself is an array

# if we want to iterate over each element of array we don't need to apply multiple loops, we can use flatten
for element in s.flatten():
    print(element)  # by default it perform row major flattening: Elements in row appear together

for element in s.flatten(order='F'):
    print(element)  # Now it will perform column major flattening: Elements in columns appear together

# Alternatively we can use np.nditer function and by providing order parameter as well. Major difference between is
# flattens actually returns a 1D result array, nditer just allows us to iterate over elements

for i in np.nditer(s, order='F'):
    print(i)

# Iteration over multi-dimensional array through nditer is read only operation. you can not assign any values to array

print(s)
for i in np.nditer(s, op_flags = ['readwrite']):
    i[...] = i * i  # ValueError: assignment destination is read-only, without flag, i[...] refers to current element
print(s)