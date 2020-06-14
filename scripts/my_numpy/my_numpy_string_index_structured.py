import numpy as np

name = ['John', 'Mary', 'Smith', 'Susy']
id = [1, 2, 3, 4]
score = [83.1, 65.0, 47.8, 91.3]

student_data = np.zeros(4, dtype={'names': ('name', 'studentId', 'score'),
                                  'formats': ('U10', 'i4', 'f8')})
print(student_data)
# [('', 0, 0.)
# ('', 0, 0.)
# ('', 0, 0.)
# ('', 0, 0.)]
# dtype is dictionary with keys as names, formats, offsets, titles

# assigning the values
student_data['name'] = name
student_data['studentId'] = id
student_data['score'] = score

print(student_data)  # [('John', 1, 83.1) ('Mary', 2, 65. ) ('Smith', 3, 47.8) ('Susy', 4, 91.3)]
print(student_data[0])  # ('John', 1, 83.1) it will prints first row # we can use integer index as well
print(student_data['name'])  # ['John' 'Mary' 'Smith' 'Susy']
print(student_data[2]['name'], student_data[2]['score'],)  # Smith, 47.8
print(student_data[student_data['score'] > 70]['name'])  # John, Susy  # conditional indexing with structured data

