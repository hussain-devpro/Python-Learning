import numpy as np

a = np.array([['India', 'UK', 'France', 'Germany'],
              ['New Delhi', 'London', 'Paris', 'Berlin']])

print(a, a.shape, a.size)  # 2 row and 4 Columns

# Another method to flatten the array is ravel function. Copy of the array is created only when needed.
x = a.ravel(order='F')  # works similar to flatten and nditer

print(x, type(x))
# To transpose an array i.e. converting rows to columns and columns to row
b = a.T
print(a, a.shape, a.size)  # No changes in source array
print(b, b.shape, b.size)  # 4 rows and 2 columns

a = np.arange(12)
print(a)
b = a.reshape(-1, 3)  # Here -1 is unknown dimension. It means row number will be calculated according to columns
print(b)
# b = a.reshape(-1, -1)  # ValueError: can only specify one unknown dimension
# b = a.reshape(5, -1)  # ValueError: cannot reshape array of size 12 into shape (5,newaxis)

x = np.arange(9)
print(x)
# Splitting the array horizontally, we have to pass int as index to split the array
# if it can not split the array in equal size then we get following error
# ValueError: array split does not result in an equal division
x1, x2, x3 = np.split(x, 3)
print(x1, x2, x3)

y = np.array([['India', 'UK', 'France', 'Germany'],
              ['New Delhi', 'London', 'Paris', 'Berlin']])

# to split the 2-D array horizontally, here 2 specify the section for equal split
h1, h2 = np.hsplit(y, 2)
print(h1)
print(h2)
# np.hsplit(y, 3)  # Fails. ValueError: array split does not result in an equal division

v1, v2 = np.vsplit(y, 2)
print(v1)
print(v2)
