# Tuple are immutable sequence of objects

t = ('abc', 1.25, 4)
print(t, type(t), t[1], type(t[1]), len(t))

t2 = t + (3.45,)  # We can concatenate the tuple with + operator
print(t2, type(t2))

for item in t:
    print(item)

t3 = (t, t2)
print(t3[0][1])

a, b, c = t  # Referred as Tuple unpacking
print(a,b,c)

x, *_ = t2  # ignore all elements except first one while tuple unpacking
print(x)

*_, y = t2  # ignore all elements except last one while tuple unpacking
print(y)

x2, *_, y2 = t2
print(x2,y2)

l = [1,2,3,4,5]
t=tuple(l)  # Tuple constructor

# t[2] = 5 : TypeError: 'tuple' object does not support item assignment
print(type(l), type(t))