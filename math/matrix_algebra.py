import numpy as np

# Matrix Algebra

# Variables
A = np.array([[1, 2, 3],
              [2, 7, 4]])
B = np.array([[1, -1],
              [0, 1]])
C = np.array([[5, -1],
              [9, 1],
              [6, 0]])
D = np.array([[3, -2, -1],
              [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1],
              [8],
              [0],
              [5]])


# 1. Matrix Dimensions
# Write the dimensions of each matrix

# 1.1) A
one_point_one_answer = A.shape
# one_point_one_answer = (2, 3)

# 1.2) B
one_point_two_answer = B.shape
# one_point_two_answer = (2, 2)

# 1.3) C
one_point_three_answer = C.shape
# one_point_three_answer = (3, 2)

# 1.4) D
one_point_four_answer = D.shape
# one_point_four_answer = (2, 3)

# 1.5) u
one_point_five_answer = u.shape
# one_point_five_answer = (1, 4)

# 1.6) w
one_point_six_answer = w.shape
# one_point_six_answer = (4, 1)

# 2. Vector Operations
# Perform the following operations. Assume α = 6
alpha = 6

# 2.1) u + v
two_point_one_answer = u+v
# two_point_one_answer = [ 9  7 -4  9]

# 2.2) u - v
two_point_two_answer = u-v
# two_point_two_answer = [ 3 -3 -2  1]

# 2.3) αu
two_point_three_answer = alpha*u
# two_point_three = [ 36  12 -18  30]

# 2.4) u * v
two_point_four_answer = u*v
# two_point_four_answer = [18 10  3 20]


# 2.5) ||u||
# we could loop through the indices and square them
two_point_five_answer = np.linalg.norm(u)


# 3. Matrix Operations
# Evaluate each of the following expressions, if it is defined; else fill in with "not defined." Do your work by
# hand on scratch paper

# 3.1) A + C
# three_point_one_answer = A + C
# three_point_one_answer gives us a ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
# this answer is undefined

# 3.2) A - C^T
three_point_two_answer = A - C.transpose()
# [[-4 -7 -3], [ 3  6  4]]

# 3.3) C^T + 3D
three_point_three_answer = C.transpose() + 3*D
# three_point_three_answer = [[14  3  3], [ 2  7  9]]

# TODO figure out what's up here?
# 3.4) BA
three_point_four_answer = np.dot(B, A)
# three_point_four_answer = [[-1 -5 -1], [ 2  7  4]]

# 3.5) BA^T
# three_point_five_answer = B*A.transpose()
# three_point_five_answer = ValueError: operands could not be broadcast together with shapes (2,2) (3,2)
# this answer is undefined
