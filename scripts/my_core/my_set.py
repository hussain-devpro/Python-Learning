# set is unordered collection of unique elements
# set are mutable, so elements can be added are removed but each elements are immutable like keys in dict
s = {1, 3, 6, 7, 8}  # Even if we provide another duplicate literal it will get ignored
print(s, type(s))

d = {}  # creates a empty dict
s = set()  # creates a empty set

print(type(d), type(s))

l = [1,5,3,6,3,7,9]
s = set(l)  # create set from list, removes duplicate values
print(s)

for i in s:
    print(i)

s.add(100)
s.update(('1', 200))  # update sets with list or tuple, ignores duplicate values
s.remove(3)  # remove element from set, if element is not present then keyError is generated
print(s)

s1 = {1, 3, 5, 7, 9, 11}
s2 = {3, 6, 9, 12}

print(s1.union(s2), s1.union(s2) == s2.union(s1))  # all elements present in either set: or operation
print(s1.intersection(s2), s1.intersection(s2) == s2.intersection(s1))  # all elements present in both set: and operation
print(s1.difference(s2), s2.difference(s1), s1.difference(s2) == s2.difference(s1))  # Set1 - Set2
print(s1.symmetric_difference(s2))

# other set methods are issubset, issuperset, is_disjoint
