class Matrix:
    def __init__(self, data):
        """
        Inicializa a matriz.
        :param data: Lista de listas representando a matriz.
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def print_matrix(self, decimals=3):
        """
        Imprime a matriz, linha por linha, com os números arredondados.
        :param decimals: Número de casas decimais para arredondamento.
        """
        for row in self.data:
            print([round(x, decimals) for x in row])

    @staticmethod
    def zeros(rows, cols):
        """
        Cria uma matriz de zeros.
        :param rows: Número de linhas.
        :param cols: Número de colunas.
        :return: Instância de Matrix preenchida com zeros.
        """
        return Matrix([[0.0 for _ in range(cols)] for _ in range(rows)])

    def coef_matrix(self):
        """
        Recupera a matriz de coeficientes (remove a última coluna, que geralmente é o vetor dos termos independentes).
        :return: Nova instância de Matrix com os coeficientes.
        """
        return Matrix([row[:-1] for row in self.data])

    def determinant(self):
        """
        Calcula o determinante da matriz a partir da forma triangular superior.
        O produto dos elementos da diagonal principal é o determinante.
        :return: Determinante da matriz.
        """
        if self.rows != self.cols:
            raise ValueError("Determinante definido apenas para matrizes quadradas!")
        n = self.rows
        # Cria uma cópia para evitar modificar a matriz original
        AM = [row[:] for row in self.data]
        
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

    def verifica_non_singularidade(self):
        """
        Verifica se a matriz é não singular (determinante diferente de zero).
        :return: True se não singular, senão levanta ArithmeticError.
        """
        if self.determinant() != 0:
            return True
        else:
            raise ArithmeticError("Matriz Singular!")

    def gauss_jordan(self):
        """
        Aplica o método de Gauss-Jordan para resolver o sistema linear.
        Supõe que a última coluna é o vetor de termos independentes.
        :return: Nova instância de Matrix com a matriz aumentada transformada.
        """
        # Cria uma cópia da matriz aumentada
        augMat = [row[:] for row in self.data]
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
        
        return Matrix(augMat)


# Exemplo de uso:
if __name__ == '__main__':
    # Matriz aumentada do sistema
    matriz_aumentada = [
#        [3.0, 2.0, -4.0, 3.0],
#        [2.0, 3.0, 3.0, 15.0],
#        [5.0, -3.0, 1.0, 14.0]
        
        [2, 3, 5],
        [4, -1, 7]

    ]
    
    matrix = Matrix(matriz_aumentada)
    
    # Recupera a matriz de coeficientes
    mc = matrix.coef_matrix()
    print("Matriz de Coeficientes:")
    mc.print_matrix()
    
    # Calcula o determinante
    det = mc.determinant()
    print("Determinante:", det)
    
    # Verifica a não singularidade
    print("Matriz não singular?", mc.verifica_non_singularidade())
    
    # Aplica o método de Gauss-Jordan e imprime a matriz resultante
    result = matrix.gauss_jordan()
    print("Matriz após Gauss-Jordan:")
    result.print_matrix()
