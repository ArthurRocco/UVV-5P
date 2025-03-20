from scipy import linalg

A = [[3.0, 2., -4.0], [2.0, 3.0, 3.0], [5.0, -3, 1.0]]
b = [3.0, 15.0, 14.0]

solution_01 = linalg.solve(A,b)
print(solution_01)