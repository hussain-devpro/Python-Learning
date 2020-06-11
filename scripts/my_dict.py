# Dictionary is object with key, value pair
# Internally Dictionaries maintains reference for Key object and value object
# Keys are immutable, so string, numbers, tuples are fine
# order may vary between different run of the program
from pprint import pprint as pp

d = {'a': 1, 'b': 2}
d['b'] = 3  # value of object with key as 'b' will be updated
d['c'] = 5  # since key is not available, so it will get inserted into the dict
print(d, type(d), d['a'])
d2 = d.copy()
print(d2)
# dictionary copy is by default shallow.

d3 = {'d' : 8}
d.update(d3)
print(d)

for key in d:  # if we want to retrieve only values then we should use d.values(), for both d.items()
    print(f"{key} => {d[key]}")

pp(d)
