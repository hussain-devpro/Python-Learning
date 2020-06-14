import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
i = x.view()  # i, j both contains the shallow copy of x
j = x.view()

print(x, type(x), id(x))
print(i, type(i), id(i))  # all array has different id
print(j, type(j), id(j))

if i is x:
    print("View is same as original object")
else:
    print("View is different")

if i.base is x:  # base is unique to numpy array only, it is not available for simple list
    print("Both object reference have same base")
else:
    print("bases are also different")

# update the object using view j
j[0] = 100
print (i, j, x)  # All array will be updated, because they have same base.

# create new array object and assign to view i
i = np.arange(5)
print (i, j, x)  # Object through ref i will be updated, but there will not be any effect on x and j.

# Reshape the view j (which is pointing to original object)
j.shape = (2,4)

print(j)  # Contains the same data, however shape gets modified
print(x)  # no effect on original object

# Above was possible because view performs shallow copy of array

x = np.array([1,2,3,4,5,6,7,8])
i = x.copy()  # performs deep copy of array
print(x, i)
print(i is x)
print(i.base is x)

# update the i with new value
i[0] = 100
print(x,i) # only i is getting modified, no effect on x



