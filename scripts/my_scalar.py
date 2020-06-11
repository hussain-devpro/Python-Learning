# Integer
# int has unlimited precision
print("Integer")
print(10)  # decimal precision
print(0b10)  # binary precision
print(0o10)  # octal precision
print(0x10)  # hexadecimal precision
print(int(3.5))  # int constructor
print(int(-3.5))  # int constructor (Rounding always towards 0)
print(int('100'))  # int constructor str to integer directly
print(int('100',
          2))  # int constructor with base. Output will be in Decimal format. If Wrong data is provided then it will consider the base as 10.

# Float
# almost 15-16 digits of precision
print("Floating Point")
print(3.5)
print(3e5)  # Scientific Notation
print(1.616e-35)  # Scientific Notation of Plank constant, Python switches the output in readable format
print(float(7))  # float constructor
print(float('1.625'))  # float constructor, str to float
print(float('nan'))  # special meaning nan = not a number (We can't use this with int constructor)
print(float('inf'))  # special meaning inf = infinity (We can't use this with int constructor)
print(float('-inf'))  # special meaning -inf = negative infinity (We can't use this with int constructor)
print(3.0 + 1)  # result of any calculation of int and float is promoted to float

# None
# represent as absence of any value. Use for null values.
print("None Type")
print(None)
a = None
print(a is None)  # print as True by checking the variable is null

# Bool
# Boolean logical values
print("Bool")
print(True)
print(False)
# Bool constructor results in False in case of Zero, every other case it returns True
print(bool(0))  # False
print(bool(34))  # True
print(bool(-1))  # True
print(bool(0.0))  # False
print(bool(1.35))  # True
print(bool(-1.0))  # True
# Empty collections like list or strings are False
print(bool([]))  # False
print(bool([1, 2]))  # True
print(bool(''))  # False
print(bool('abc'))  # True
print(bool("False"))  # True, as this is consider as non empty string
print(bool("True"))  # True
