# Classe Node representa um nó em uma árvore binária.
class Node:
    def __init__(self, value):
        self.value = value  # Armazena o valor do nó.
        self.left = None    # Filho à esquerda.
        self.right = None   # Filho à direita.

# Classe rotinaArvore implementa uma árvore binária com diversos métodos.
class rotinaArvore:
    def __init__(self):
        self.root = None  # Raiz da árvore.

    # Método insert insere um novo valor na árvore.
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Método recursivo de inserção.
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Percurso Pré-ordem.
    def pre_order(self, node, path=[]):
        if node:
            path.append(node.value)
            self.pre_order(node.left, path)
            self.pre_order(node.right, path)
        return path

    # Percurso In-ordem.
    def in_order(self, node, path=[]):
        if node:
            self.in_order(node.left, path)
            path.append(node.value)
            self.in_order(node.right, path)
        return path

    # Percurso Pós-ordem.
    def post_order(self, node, path=[]):
        if node:
            self.post_order(node.left, path)
            self.post_order(node.right, path)
            path.append(node.value)
        return path

    # Calcula a altura da árvore.
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    # Determina o tipo da árvore:
    # Se for cheia (full) retorna "Árvore binária Perfeita",
    # se for completa (complete) retorna "Árvore Binária Completa",
    # caso contrário, retorna "Árvore Binária".
    def tree_type(self):
        if not self.root:
            return "Empty Tree"
        d = self.height(self.root) + 1
        is_full = self._is_perfect(self.root, d)
        is_complete = self._is_complete(self.root, 0, self.count_nodes())
        if is_full:
            return "Árvore Binária Perfeita"
        elif is_complete:
            return "Árvore Binária Completa"
        else:
            return "Árvore Binária"

    # Verifica se a árvore é perfeita CORRIGIDO.
    def _is_perfect(self, root, d, level=0):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return d == level + 1
        if root.left is None or root.right is None:
            return False
        return self._is_perfect(root.left, d, level + 1) and self._is_perfect(root.right, d, level + 1)

    # Verifica se a árvore é completa CORRIGIDO de acordo com a definição de que a estrutura de dados em que todos os níveis, exceto o último, 
    # estão totalmente preenchidos e os nós do último nível estão posicionados o mais à esquerda possível.
    def _is_complete(self, root, index, numberNodes):
        if root is None:
            return True
        if index >= numberNodes:
            return False
        return (self._is_complete(root.left, 2 * index + 1, numberNodes) and
                self._is_complete(root.right, 2 * index + 2, numberNodes))

    # Conta o número total de nós na árvore.
    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)


# ------------------------------------------------------------------
# Exemplo 1: Árvore Binária Completa CORRIGIDA (mas não cheia)

# De acordo com a definição que a estrutura de dados em que todos os níveis, exceto o último, estão totalmente preenchidos 
# e os nós do último nível estão posicionados o mais à esquerda possível. 

# Estrutura desejada:
#         4
#       /   \
#      2     6
#     /    
#    1      
# Nota: o nó 6 possui apenas o filho à esquerda.
tree_completa = rotinaArvore()
values_completa = [4, 2, 6, 1]

# Outros exemplos de completa: [10, 5, 15, 2, 7], [4, 2, 6, 1, 3, 5], [30, 15, 45, 10, 20, 40, 50, 5, 12]

for val in values_completa:
    tree_completa.insert(val)

# ------------------------------------------------------------------
# Exemplo 2: Árvore Binária Cheia (perfeita)
# Estrutura desejada:
#           8
#         /   \
#        4     12
#       / \   /  \
#      2   6 10  14
tree_cheia = rotinaArvore()
values_cheia = [8, 4, 12, 6, 2, 10, 14]
for val in values_cheia:
    tree_cheia.insert(val)

# ------------------------------------------------------------------
# Exemplo 3: Árvore Binária Estrita (não completa nem cheia)
#         15
#        /
#       10
#      /  \
#     5    12
#             \
#             13
tree_estrita = rotinaArvore()
values_estrita = [15, 10, 5, 12, 13]
for val in values_estrita:
    tree_estrita.insert(val)

# ------------------------------------------------------------------
# Exibindo os resultados:

print("Exemplo de Árvore Binária Completa:")
print("Percurso Pré-ordem:", tree_completa.pre_order(tree_completa.root, []))
print("Percurso In-ordem:", tree_completa.in_order(tree_completa.root, []))
print("Percurso Pós-ordem:", tree_completa.post_order(tree_completa.root, []))
print("Altura:", tree_completa.height(tree_completa.root))
print("Tipo:", tree_completa.tree_type())

print("\n" + "-"*50 + "\n")

print("Exemplo de Árvore Binária Cheia:")
print("Percurso Pré-ordem:", tree_cheia.pre_order(tree_cheia.root, []))
print("Percurso In-ordem:", tree_cheia.in_order(tree_cheia.root, []))
print("Percurso Pós-ordem:", tree_cheia.post_order(tree_cheia.root, []))
print("Altura:", tree_cheia.height(tree_cheia.root))
print("Tipo:", tree_cheia.tree_type())

print("\n" + "-"*50 + "\n")

print("Exemplo de Árvore Binária Estrita:")
print("Percurso Pré-ordem:", tree_estrita.pre_order(tree_estrita.root, []))
print("Percurso In-ordem:", tree_estrita.in_order(tree_estrita.root, []))
print("Percurso Pós-ordem:", tree_estrita.post_order(tree_estrita.root, []))
print("Altura:", tree_estrita.height(tree_estrita.root))
print("Tipo:", tree_estrita.tree_type())
