# While Loops
a = 5  # its called predicate
while a != 0:
    print(a)
    a -= 1

# Since bool(0) is False, so we can replace above code with following
print("Another way to implement")
a = 5
while a:
    print(a)
    a -= 1
# However, we should avoid this type of coding as it is against the zen of Python (explicit is better than implicit).

print("Break Statement")
a = 5
while True:
    if a == 2:
        break  # Generally used in infinite loops
    print(a)
    a -= 1

print("Continue Statement")
a = 5
while a != 0:
    a -= 1
    if a == 2:
        continue  # Generally used to skip certain condition or scenarios
    print(a)

print('End')