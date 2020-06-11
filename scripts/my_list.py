# List is sequence of objects and mutable
import copy

a = ['a', 'b', 'c', 'd', 'e']
a[3] = 7
print(a, type(a), a[2])

b = []  # Empty list
b.append(1.1)  # Append method with insert element at end of the list.
b.append(2.2)
print(b)

s = 'India is my country'
l = list(s)  # list constructor will convert string to list. Even blank space characters are elements of list.
print(l, type(l))

l = [1, 4, 3, 7, 5, 9]
print(l[0], l[-1], l[len(l) - 1])  # Negative indexes can be used to get last elements
print(l[1:4], l[1:-1], l[:4])  # Slicing operation, we can provide start and stop index.

l1 = l  # only object reference are getting copied. Both References are pointing to same object.
print(l1 is l)

l2 = l[:]  # New list is getting generated, which is being pointed by new reference l2
# another way to copy is l2 = l.copy(), which is more readable
# another way to copy is l2 = list(l), can be used with other iterable like tuple, set, string
print(l2 is l)

# Above copy method are shallow copy. Creates new list, containing the same object references as the source list.
# These don't copy the referred to objects
print("Nested List Deep Copy")

a = [[1, 2], [3, 4]]
b = a[:]
print(a is b)  # Results is False
print(a[0], b[0], a[0] is b[0])  # Result is True due to Shallow Copy
a[0] = ['a', 'b']  # Rebinding the object reference to newly constructed list
print(a[0], b[0], a[0] is b[0])  # Result is False
a[1].append(5)  # Second element of Object reference of a and b pointing to same object
print(a)
print(b)

# To perform deep copy of nested list or any iterables, need to check copy module
print("Deep Copy Example")
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[1].append(5)  # Second element of Object reference of a and b pointing to different object so only a will get updated
print(a)
print(b)

print("Repetition Examples")
a = [0] * 5  # Repetition of values for initialization of iterable for immutable object
b = [[1, 2]] * 5  # Repetition of nested list of mutable objects, it will repeat the object reference instead of object
print(a, b)
b[2].append(3)
print(b)

l = 'the quick brown fox jumps over the lazy dog'.split()
print(l, l.index('fox'), l.count('the'), 'lazy' in l, 'dog' not in l)
del l[3]  # remove the element using position or index
print(l)
l.remove('lazy')
print(l)
l.insert(6, 'lazy')
print(l)

l = [15, 4, 9]
l.reverse()  # updates the original list and returns nothing (None)
print(l)
l.sort(reverse=True)  # updates the original list and returns nothing (None)
print(l)
l.sort()  # updates the original list and returns nothing (None)
print(l)


def sort_algo(x):
    return x % 7


l.sort(key=sort_algo)  # here key argument can be anything, for example for string it can be len function
print(l)

# There is sorted and reversed functions available which returns iterator and new list. It doesn't change the original
