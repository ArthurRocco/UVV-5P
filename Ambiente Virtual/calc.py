import numpy as np

A = np.array([[3.0, 2., -4.0], [2.0, 3.0, 3.0], [5.0, -3, 1.0]])
b = np.array([3.0, 15.0, 14.0])

#print(A, '\n')
#print(b)

solution_01 = np.linalg.solve(A,b)
print(solution_01)


A = np.array([[0, 2, 0, 1,], [2, 2, 3, 2,], [4, -3, 0, 1], [6, 1, -6, -5]])
b = np.array([0, -2, -7, 6])

solution_02 = np.linalg.solve(A,b)
print(solution_02)