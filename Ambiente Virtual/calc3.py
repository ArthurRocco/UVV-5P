from sympy import Matrix

# augMat = Matrix([[3.0, 2.0, -4.0], [2.0, 3.0, 3.0], [5.0, -3, 1.0]])

solution_01 = augMat.rref()
print(solution_01)
