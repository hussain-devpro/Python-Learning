import numpy as np

a = np.arange(11)**2  # [  0   1   4   9  16  25  36  49  64  81 100]

# Indexing operation on 1D array is same as List or Tuple
print(a[0], a[5], a[-1], a[-7])  # 0, 25, 100, 16

# Slicing operation on 1D array is also same as List or Tuple
print(a[3:6])  # 9, 16, 25   Slicing starts from index 3 and upto index 6 but not including the 6

s = np.array([['John', 'Mary', 'Smith', 'Susy'],
              [90, 63, 15, 70],
              [42, 56, 87, 64]])

print(s[0], type(s[0]))  # ['John', 'Mary', 'Smith', 'Susy']  it prints the entire row0, Type: <class 'numpy.ndarray'>
print(s[1]) # ['90' '63' '15' '70']  it prints the entire row1
print(s[0, 2], type(s[0, 2])) # Smith. Type: <class 'numpy.str_'>, its numpy string, instead of regular string
print(s[1:, 1:3])  # [[63,15], [56,87]]
print(s[:,0], type(s[:,0])) # [John, 90, 42]  It will print column0 as row. Type: <class 'numpy.ndarray'>

# Each row/columns in multi-dimensional ndarray is also ndarray

