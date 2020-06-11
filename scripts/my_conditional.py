if True:
    print("It's True")  # Printed

if False:
    # noinspection PyUnreachableCode
    print("It's True")  # Not Printed

if bool('Eggs'):
    print("Eggs are available")  # Printed

if bool(''):
    print("Eggs are available")  # Not Printed

key = 40
if key > 20:
    print(f'{key} is Greater than 20')
else:
    print(f'{key} is Lesser than 20')

key = 10
if key > 20:
    print(f'{key} is Greater than 20')
else:
    print(f'{key} is Lesser than 20')

key = 15
if key > 20:
    print(f'{key} is Greater than 20')
elif key > 10:
    print(f'{key} is Lesser than 20 and greater than 10')
else:
    print(f'{key} is Lesser than 20 and 10')

key = 5
if key > 20:
    print(f'{key} is Greater than 20')
elif key > 10:
    print(f'{key} is Lesser than 20 and greater than 10')
else:
    print(f'{key} is Lesser than 20 and 10')

key = 5
if key > 20:
    print(f'{key} is Greater than 20')
elif key > 10:
    print(f'{key} is Lesser than 20 and greater than 10')
else:
    print('Place Holder')
    pass  # Place holder for further code.
