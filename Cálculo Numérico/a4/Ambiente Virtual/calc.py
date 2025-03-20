import numpy as np

A = np.array([[3.0, 2., -4.0], [2.0, 3.0, 3.0], [5.0, -3, 1.0]])
b = np.array([3.0, 15.0, 14.0])

#print(A, '\n')
#print(b)

solution_01 = np.linalg.solve(A,b)
print(solution_01)