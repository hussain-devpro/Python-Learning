def greet():
    """Function with no parameter"""
    print('Hi')


def greet_name(name):
    """Function with parameter"""
    print(f'Hi {name}')


def greet_fullname(firstname, lastname):
    """Function with multiple parameters"""
    print(f'Hi {firstname} {lastname}')


# Arguments with default value must come after those without the default values
# Keyword arguments must be specified only after all positional arguments
# Since function arguments are evaluated only once when they are defined. So Default arguments must always contains
# immutable objects like number or string or bool etc. It should never contain mutable objects like list, otherwise
# there may be unintended consequences.
def greet_defaultname(firstname, lastname='Smith'):
    """Function with default value parameters"""
    print(f'Hi {firstname} {lastname}')


def updatelist(newlist):
    newlist.append(25)
    return newlist


def replacelist(fnew):
    fnew=[4,5,6]
    return fnew


def replace_content(fnew):
    fnew[0] = 4
    fnew[1] = 5
    fnew[2] = 6
    return fnew

greet()
greet_name('John')
greet_fullname('John', 'Smith')  # invoking function with positional argument
greet_fullname(lastname='Ann', firstname='Marry')  # invoking function with keyword arguments
greet_defaultname(firstname='Susy')  # invoking function with only 1 keyword arguments

# Wisdom
# while passing arguments objecte reference are getting passed to function not the actual arguments. So if we modify
# the object using the same reference then original object will also get modified. Else if we assign a new object the
# object reference than changes in object will not reflect to original object.

mylist = [1,2,3,4,5]
newlist = updatelist(mylist)
print(mylist)  # passing list is getting updated as both list points to same object
print(newlist)

f=[1,2,3]
g=replacelist(f)
print(f)  # passing list will not get modified as function internally pointed to new list.
print(g)

f=[1,2,3]
g=replace_content(f)
print(f)  # passing list will get modified as function internally updating the list without modifiying the object ref.
print(g)

count = 0

def show_count():
    print(count)
def set_count(c):
    count = c
def modify_count(c):
    global count
    count = c

set_count(5)
show_count()
modify_count(7)
show_count()