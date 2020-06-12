from my_exceptional import convert, string_log
from my_roots import sqrt

############################## my_exceptional ##############################

print(convert('one two seven'.split()))  # Results in 127
# print(convert('one two seven ten'.split()))  # Results in KeyError: 'ten' without exception handling
# Here 'KeyError' is the type of exception object and 'ten' is part of payload
# above exception occurs only when we are passing string
# print(convert(125))  # Results in TypeError: 'int' object is not iterable
# we need to handle each exception specifically

# We can also get the error message along with the exception by binding it to a object 'e'

# Following exception occurs due to programming errors only. We should not handled them. We should fix them.
# IndentationError, SyntaxError, NameError

print(string_log('one two seven'.split()))  # prints the log of converted number
# print(string_log('one two seven ten'.split()))  # Resulted in ValueError: math domain error
# As log of negative number is not possible which was the return code. It's un-python like way of handling the error.
# Due to this reason we should always re-raise the exception

############################## my_roots ##############################

print(sqrt(9))  # result 3.0
print(sqrt(2))  # result 1.414
# print(sqrt(-1))  # ZeroDivisionError: float division by zero  without exception handling
# since this type of exception can be avoided by careful programming, We should we always raise ValueError when function
# parameters are supplied with illegal values by using ValueError() constructor

# Some common exceptions are below
# IndexError: An Integer index out of range. l = [1,2,3]; L[4] results in IndexError: list index out of range
# ValueError: Object of correct type but with illegal values. int('abc'): results in ValueError: invalid literal for int
# KeyError: lookup in mapping field. d = {'a':1, 'b':2}; d['c'] results in KeyError: 'c'

# Also avoid Explicit Type checking using isinstance(variable, list): , because we can use same code for tuple as well
# We should not catch TypeError, Which increases function reusability and let the TypeError to arise on their own

# Its easier to ask for forgiveness than permission (EAFP)
# Basically we should not check for each and evey thing. Let the exception arise as it will be difficult to ignore hence
# it will get fixed quickly. And errors should never pass silently

# There is a finally block which will executes no matter how try block gets terminated either successfully or through
# exception. That is why always put all type of cleanup code finally block if we are not using context managers

# Platform specific code or action should be handled by ImportError and (EAFP)
