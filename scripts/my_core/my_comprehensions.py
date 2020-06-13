# General syntax of Comprehensions
# [expr(item) for item in iterables]
#
# it replaces following code for list
#
# length = []
# for word in words:
#   length.append(len(word))

# Creating new iterables from existing iterables

from math import factorial
import os
import glob
import pprint

words = "In computer science and software engineering, reusability is the use of existing assets in some form " \
             "within the software product development process".split()
word_length_list = [len(word) for word in words]  # syntax to create list comprehension
word_length_tuple = tuple(len(word) for word in words) # syntax to create tuple comprehension
word_length_set = {len(word) for word in words} # syntax to create set comprehension
print(word_length_list, type(word_length_list))
print(word_length_tuple, type(word_length_tuple))
print(word_length_set, type(word_length_set))  # it will ignore duplicate values

# complex comprehension using expressions
fact_list = [factorial(i) for i in range(20)]
print(fact_list)

# length of number for factorial and ignoring duplicate values
fact_set = {len(str(factorial(i))) for i in range(20)}
print(fact_set)

# Dictionary Comprehension
country_to_capital = {'India': 'New Delhi',
                      'UK': 'London',
                      'USA': 'Washington DC',
                      'Russia': 'Moscow'}
# Inverting Key Value pair for lookup using dict comprehension
capital_to_country = {city:country for country, city in country_to_capital.items()}
print(capital_to_country)

# Creating a dict using os and glob module
file_sizes = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob('*.py')}
pprint.pprint(file_sizes)
