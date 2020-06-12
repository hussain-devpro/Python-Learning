cities = ['Mumbai', 'Delhi', 'Pune', 'Indore']

for city in cities:
    print(city)

mapping = {'Mumbai': 'MH', 'Delhi': 'DH', 'Indore':'MP'}

for city in mapping:
    print(city, 'in state',mapping[city])

cities = ['Mumbai', 'Delhi', 'Pune', 'Indore']

for city in enumerate(cities):  # Enumerate functions provides the counter for each element in the iterable
    print(city)

for i, city in enumerate(cities):  # tuple unpacking can be used with enumerate function
    print(i, city)
