import numpy as np

# Broadcasting: describes how NumPy treats array with different shapes during arithmetic operations. Subject to certain
# constraints, the smaller array is "broadcast" across the larger array so that they have compatible shapes.

# operation: operation performed on pair of array on element-by-element basis.
# constraints: shape of tow array are compared element-wise

a = np.array([1,1,1,1,1]) + 5
print(a)

# Broadcasting scalar: Here scalar value 5 is replicated as per the larger array so 5 becomes [5, 5, 5, 5, 5].
# Then simple arithmetic is performed between similar shaped array. Hence we get the result.
# similar things happens in case of multi-dimensional array as well
# here no actual copies are made, so broad casting is computationally and memory wise efficient

# Broadcasting Array: Either all dimension should match or at least last dimension should be 1.
# so that it can be stretched. If a dimension is 1 then all other should also match.

science_score = [65, 57, 47, 71, 39]
sports_score = [40, 37, 20, 38, 45]

student_score = np.array([science_score, sports_score])
print(student_score, student_score.shape) # it has shape of (2,5)

# every student get 20 marks in science practical by default and gets 35 marks in physical training
factor_1 = np.array([20, 25])
print(factor_1, factor_1.shape)

# final_score = student_score + factor_1  # ValueError: operands could not be broadcast together with shapes (2,5) (2,)

factor_2 = np.array([[20], [35]])  # it has shape of (2,1) which compatible with student score
print(factor_2, factor_2.shape)

# last dimension of smaller array is 1  and other dimension is matching with the larger array.
# so in this case array Broadcasting is possible
final_score = student_score + factor_2
print(final_score)
# [[85 77 67 91 59]
#  [75 72 55 73 80]]
