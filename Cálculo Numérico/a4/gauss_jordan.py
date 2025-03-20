def print_matrix(M, decimals=3):
    """
    Print a matrix one row at a time
    :param M: The matrix to be printed
    """
    for row in M:
        print([round(x, decimals) for x in row])

def zeros_matrix(rows, cols):
    """
    Cria uma matriz de zeros
    :param rows: numero de linhas
    :param cols: numero de colunas
    :return: matriz quadrada de zeros
    """
    return [[0.0 for _ in range(cols)] for _ in range(rows)]

def coef_matrix(augMat):
    """
    Recupera a matriz Coeficientes para o calculo do Determinante
    :param augMat: Matriz aumentada
    :return: Matriz Coeficiente
    """
    rows = len(augMat)
    cols = len(augMat[0])
    return [row[:-1] for row in augMat]

def determinant(AM):
    """
    Calcula o determinante a partir da matriz triangular superior
    O produto da diagonal principal eh o valor do determinante
    :param AM: matriz de coeficientes
    :return: determinante da matriz
    """
    n = len(AM)
    AM = [row[:] for row in AM]  # Criar uma cópia para evitar modificar a original
    
    for fd in range(n):
        if AM[fd][fd] == 0:
            for j in range(fd + 1, n):
                if AM[j][fd] != 0:
                    AM[fd], AM[j] = AM[j], AM[fd]
                    break
            else:
                raise ValueError("Matriz singular!")
        
        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] -= crScaler * AM[fd][j]
    
    product = 1.0
    for i in range(n):
        product *= AM[i][i]
    return product

def verifica_non_singularidade(A):
    """
    Verifica se a matriz eh NAO SINGULAR
    :param A: Matriz a ser avaliada
    :return: boolean True ou raise ArithmeticError
    """
    if determinant(A) != 0:
        return True
    else:
        raise ArithmeticError("Matriz Singular!")

def GaussJordanMethod(augMat):
    n = len(augMat)
    m = len(augMat[0])
    
    for i in range(n):
        if augMat[i][i] == 0:
            for j in range(i + 1, n):
                if augMat[j][i] != 0:
                    augMat[i], augMat[j] = augMat[j], augMat[i]
                    break
            else:
                raise ValueError("Matriz singular!")
        
        divisor = augMat[i][i]
        for k in range(m):
            augMat[i][k] /= divisor
        
        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]
    
    print_matrix(augMat)

matrix = [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3.0, 1.0, 14.0]]
mc = coef_matrix(matrix)
print_matrix(mc)
det = determinant(mc)
print(det)
result = verifica_non_singularidade(mc)
print(result)
GaussJordanMethod(matrix)
