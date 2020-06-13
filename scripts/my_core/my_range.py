# Range is collection arithmetic progression of integers, there is no literal form

x = range(5)  # range starts from 0. It also does not include stop element (in this case 5)
print(x, type(x))

for i in x:
    print(i)

y = range(1, 5)  # range can start from user defined value as well start, stop
print(y, type(y))

for i in y:
    print(i)

z = range(1, 5, 2)  # user can specify the step between each element start, stop, step
print(z, type(z))

for i in z:
    print(i)

print(list(range(5)))

# range does not support keyword arguments
