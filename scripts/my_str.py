# String in python or immutable (once defined we cannot change it value) and sequence of unicode characters

import math

print('This is a string')
print("This is also a string")
print('first'"second")  # Adjacent string literals will concatenate the string.
print('''This is
a multi-line
string''')
s = 'This is \nalso a multiple \nstring'
print(s)
r = r'C:\home\nuser'  # raw string should not end with \
print(r)
a = str(456)  # string constructor with convert int, float,bool,None to string
b = str(1.62343)
c = str(True)
d = str(None)
print(a, type(a), b, type(b), c, type(c), d, type(d))
if d is None:
    print('d is none')
elif d == 'None':
    print('d is "None"')

mystr = "ABCDEF"  # String indexes starts from 0.
print(mystr[4], type(mystr[4]))  # Each index contains string type character only
# mystr[4] = 'Z'  It will result in TypeError: str object does not support item assignment

a,b = 'abc', 'def'
c = a * 2  # Repetition of string using * operator
d = a + b  # Concatenation of strings using + operator, however we should avoid them as it can generate temporaries
print(c, d)
e = "**".join([a, b])  # join method is used on separator along with list of objects (iterable)
print(e)


mystr = 'india is my county'
capstr = mystr.capitalize()
ttlstr = mystr.title()
print('\n', mystr, '\n', capstr, '\n', ttlstr)
origin, _, arrival = 'Mumbai-London'.partition('-')
print(origin,arrival)

# String Interpolation

print('The age of {} is {} years'.format('John', 32))  # if field name are used exactly ones
print('The age of {0} is {1}. {0} lives in {2}.'.format('Tony', 25, 'London'))  # if fields are used multiple times
print('The age of {name} is {age}. {name} lives in {city}.'.format(name='Marry', age = 25, city = 'New York'))
name, age, city = 'Jay', 21, 'Mumbai'
print(f'The age of {name} is {age}. {name} lives in {city}.') # f-strings are easiest to remember and most efficient
print(f"Match Constants pi = {math.pi:.3f} and e = {math.e}")  # f-string can contains function call, expression etc

print("Byte Examples")
# To convert from Byte to Str and viceversa, we need to know encoding method like UTF-8
# And we need to execute Encode or Decode function to do the conversion
# HTTP response are generally in Byte stream. So we need to use str.encode or byte.decode while dealing with HTTP data
b = b'This is a Byte'
print(b, type(b), b[2])
