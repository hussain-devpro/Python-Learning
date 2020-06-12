# iterable objects: it can be passed to iter() function to produce iterator
# iterator objects: it can be passed to next() function to get the next value

iterable = ['A', 'B', 'C', 'D']
iterator = iter(iterable)

print(iterable, type(iterable))
print(iterator, type(iterator))
print(next(iterator), next(iterator), next(iterator), next(iterator))


# print(next(iterator))  # after reaching at the end of iterable python raises StopIteration exception


# Generator functions: Iterable defined by function
# It has Lazy Evaluations i.e. compute next value by demand
# It can model sequence of no definite end (Like steams of data from sensors or active log file
# It must contains yield keyword at least ones in the definition

def my_gen():
    yield 1
    yield 'ABC'
    yield 3.45


g = my_gen()
print(g, type(g))
print(next(g), next(g), next(g))
# print(next(g)) # like any other iterable, it will generate StopIteration exception

# Each call to generator will results in new generator objects.
# And it can be used all the places where iterable are being used like for loops.
# Generators are single use object
for i in my_gen():
    print(i)


# Fibonacci series using generator
def my_fibo():
    yield 0
    yield 1
    a = 0
    b = 1
    while True:
        yield a + b
        a, b = b, a + b
        if b > 150:
            break


for i in my_fibo():
    if i > 100:
        break
    else:
        print(i)

# generator expression (comprehension)
# generator expression are enclosed in parenthesis ()
l = (x * x for x in my_fibo())
print(l, type(l))
print(list(l)[:])

# itertool.count() method provides the open ended range function

# some iterable functions are as follows
# sum: sum of all values, sum([1,2,3,4,5]) => 15
# any: logical or operation, any([True, False, False]) => True
# all: logical and operation, all([True, False, False]) => False
# zip: synchronize iteration across two or more iterables

sun = [12, 14, 15, 17, 15, 13, 20]
mon = [15, 14, 13, 12, 18, 19, 16]

for item in zip(sun, mon):
    print(item)  # result in sequence of tuple (12, 15) (14, 14) (15, 13) ... etc
