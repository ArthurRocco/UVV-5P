#   Implementar o algoritmo de Dijkstra 
#       O usuário deve poder criar o grafo direcionado e ponderado	Após a criação, o usuário pode escolher um vértice inicial e o algoritmo deve calcular o custo para todos os vértices
#       Após calcular o custo, o algoritmo deve mostrar ao usuário a rota que oferece o menor custo
#       Não Utilizar bibliotecas externas (a não ser para UX/UI)

import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

class Grafo:
    """
    Classe que representa um grafo direcionado/ponderado.
    - vertices: dicionário {vértice: [(vizinho, peso), ...]}
    - posicoes: coordenadas (x,y) para desenhar cada vértice no canvas
    - direcionado: se True, arestas unilaterais; se False, bidirecionado
    """
    def __init__(self, direcionado=True):
        # Inicializa estruturas de dados
        self.vertices = {}     # mapeia cada vértice à sua lista de arestas
        self.posicoes = {}     # armazena coordenadas de exibição para cada vértice
        self.direcionado = direcionado   # tipo de grafo

    def adicionar_vertice(self, v):
        """Adiciona um vértice v ao grafo, se ainda não existir."""
        if v not in self.vertices:
            self.vertices[v] = []

    def adicionar_aresta(self, origem, destino, peso):
        """
        Cria uma aresta de origem→destino com determinado peso.
        Lança KeyError se algum vértice não existir.
        Em grafo não-direcionado, adiciona recíproca destino→origem.
        """
        if origem not in self.vertices or destino not in self.vertices:
            raise KeyError("Vértice não cadastrado.")
        # adiciona aresta principal
        self.vertices[origem].append((destino, peso))
        # se não direcionado, adiciona aresta de volta
        if not self.direcionado:
            self.vertices[destino].append((origem, peso))

    def remover_aresta(self, origem, destino, peso):
        """
        Desfaz a última aresta adicionada removendo uma ocorrência
        de (destino,peso) em origem (e recíproca, se apropriadamente bidirecional).
        """
        if origem in self.vertices:
            try:
                self.vertices[origem].remove((destino, peso))
            except ValueError:
                pass
        if not self.direcionado and destino in self.vertices:
            try:
                self.vertices[destino].remove((origem, peso))
            except ValueError:
                pass

    def limpar(self):
        """Remove todos os vértices e arestas do grafo."""
        self.vertices.clear()
        self.posicoes.clear()

    def dijkstra(self, inicio):
        """
        Implementação do algoritmo de Dijkstra sem uso de heapq:
        - dist: mapeia vértice → distância mínima desde início
        - prev: armazena antecessor para reconstruir caminho
        - visitados: conjunto de vértices já processados
        """
        # inicialização das distâncias
        dist = {v: float('inf') for v in self.vertices}
        prev = {v: None for v in self.vertices}
        dist[inicio] = 0
        visitados = set()

        # enquanto houver vértices não visitados
        while len(visitados) < len(self.vertices):
            # escolhe vértice não visitado com menor dist[v]
            u = None
            menor = float('inf')
            for v in self.vertices:
                if v not in visitados and dist[v] < menor:
                    menor = dist[v]
                    u = v
            # se não encontrou vértice alcançável, encerra
            if u is None:
                break
            visitados.add(u)

            # relaxa arestas saindo de u
            for (viz, peso) in self.vertices[u]:
                if viz in visitados:
                    continue
                nova = dist[u] + peso
                if nova < dist[viz]:
                    dist[viz] = nova
                    prev[viz] = u

        return dist, prev

    def obter_caminhos(self, inicio):
        """
        Reconstrói os caminhos a partir de 'inicio' até cada vértice.
        Retorna lista de strings descrevendo rotas e custos.
        """
        dist, prev = self.dijkstra(inicio)
        resultados = []
        for dest in self.vertices:
            if dest == inicio:
                continue  # ignora rota até si mesmo
            # se infinita, não há caminho
            if dist[dest] == float('inf'):
                resultados.append(f"Não há caminho de {inicio} para {dest}.")
            else:
                # reconstrói sequência de vértices do destino ao início
                seq = []
                u = dest
                while u is not None:
                    seq.insert(0, u)
                    u = prev[u]
                resultados.append(
                    f"Caminho {inicio}→{dest}: {'→'.join(seq)} (custo {dist[dest]:.0f})"
                )
        return resultados

#

## Modificações na Classe `Interface`

#A principal mudança estará na função `add_aresta`, onde ajustaremos a geometria da janela.

class Interface:
    """
    Interface gráfica usando Tkinter para manipular e visualizar o grafo.
    - Botões para adicionar/remover arestas, limpar grafo, executar Dijkstra.
    - Canvas interativo: arraste nós e veja atualização em tempo real.
    """
    def __init__(self, master):
        self.master = master
        master.title("Dijkstra Interativo - Sem heapq")

        # Grafo e histórico de arestas para desfazer
        self.grafo = Grafo(direcionado=True)
        self.history = []  # pilha de tuplas (origem, destino, peso)
        self.dragging = None  # vértice atual sendo movido

        # Flags de configuração (direcionado, ponderado)
        self.var_direc = tk.BooleanVar(value=True)
        self.var_pond = tk.BooleanVar(value=True)

        # Painel de controle à esquerda
        ctrl = tk.Frame(master)
        ctrl.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        # Checkbox para alternar tipo de grafo
        tk.Checkbutton(ctrl, text="Direcionado", variable=self.var_direc,
                       command=self.toggle_direc).pack(anchor='w')
        tk.Checkbutton(ctrl, text="Ponderado", variable=self.var_pond).pack(anchor='w')
        # Botões de ação
        tk.Button(ctrl, text="Add Aresta", command=self.add_aresta).pack(fill=tk.X, pady=2)
        tk.Button(ctrl, text="Desfazer Última Aresta", command=self.undo_aresta).pack(fill=tk.X, pady=2)
        tk.Button(ctrl, text="Limpar Grafo", command=self.clear_graph).pack(fill=tk.X, pady=2)
        tk.Button(ctrl, text="Dijkstra", command=self.run).pack(fill=tk.X, pady=2)
        tk.Button(ctrl, text="Vertices", command=self.show_verts).pack(fill=tk.X, pady=2)
        # Área de texto para logs e resultados
        self.text = scrolledtext.ScrolledText(ctrl, width=30, height=20)
        self.text.pack(pady=5)

        # Canvas para desenho do grafo à direita
        self.canvas = tk.Canvas(master, width=600, height=600, bg='white')
        self.canvas.pack(side=tk.RIGHT, padx=5, pady=5)
        self.radius = 20  # raio dos nós
        # Eventos de mouse para arrastar nós
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_release)

    def toggle_direc(self):
        """Ativa/desativa grafo direcionado e redesenha."""
        self.grafo.direcionado = self.var_direc.get()
        self.redraw()

    def layout(self):
        """
        Posiciona automaticamente novos nós em grade se ainda não tiverem coordenadas.
        Distribuição em filas e colunas baseada na raiz quadrada do número de vértices.
        """
        n = len(self.grafo.vertices)
        if n == 0:
            return
        cols = int(n**0.5) + 1
        spacing_x = 600 / cols
        rows = (n // cols) + 1
        spacing_y = 600 / rows
        for idx, v in enumerate(self.grafo.vertices):
            if v not in self.grafo.posicoes:
                col = idx % cols
                row = idx // cols
                x = (col + 0.5) * spacing_x
                y = (row + 0.5) * spacing_y
                self.grafo.posicoes[v] = (x, y)

    def redraw(self):
        """Limpa e redesenha todas arestas e nós no canvas."""
        self.canvas.delete('all')
        # Desenha arestas com setas e pesos
        for u, adj in self.grafo.vertices.items():
            x1, y1 = self.grafo.posicoes[u]
            for v, p in adj:
                x2, y2 = self.grafo.posicoes[v]
                # Calcula direção unitária para desenhar linha entre perímetros
                dx, dy = x2 - x1, y2 - y1
                dist = (dx*dx + dy*dy)**0.5 or 1
                ux, uy = dx/dist, dy/dist
                start = (x1 + ux*self.radius, y1 + uy*self.radius)
                end   = (x2 - ux*self.radius, y2 - uy*self.radius)
                # seta opcional para grafo direcionado
                if self.var_direc.get():
                    self.canvas.create_line(*start, *end,
                                             arrow=tk.LAST,
                                             arrowshape=(10,12,4),
                                             width=2)
                else:
                    self.canvas.create_line(*start, *end, width=2)
                # desenha peso, se habilitado
                if self.var_pond.get():
                    mx, my = (start[0]+end[0])/2, (start[1]+end[1])/2
                    self.canvas.create_text(mx, my-10, text=str(p))
        # Desenha nós (círculos com rótulo)
        for v in self.grafo.vertices:
            x, y = self.grafo.posicoes[v]
            self.canvas.create_oval(x-self.radius, y-self.radius,
                                     x+self.radius, y+self.radius,
                                     fill='#eef', outline='#44a', tags=('node', v))
            self.canvas.create_text(x, y, text=str(v), tags=('node', v))

    def on_click(self, event):
        """Detecta clique sobre nó para iniciar arraste."""
        closest = self.canvas.find_closest(event.x, event.y)
        for tag in self.canvas.gettags(closest):
            if tag in self.grafo.vertices:
                self.dragging = tag
                break

    def on_drag(self, event):
        """Atualiza posição do nó enquanto arrasta e redesenha."""
        if self.dragging:
            self.grafo.posicoes[self.dragging] = (event.x, event.y)
            self.redraw()

    def on_release(self, event):
        """Encerra arraste ao soltar o botão."""
        self.dragging = None

    def add_aresta(self):
        """
        Abre uma única janela para inserir origem, destino e peso. Adiciona a aresta
        ao grafo, registra em history para undo e atualiza layout/desenho.
        A janela será centralizada na tela.
        """
        # Cria uma nova janela Toplevel
        input_window = tk.Toplevel(self.master)
        input_window.title("Adicionar Aresta")

        # Variáveis para armazenar as entradas
        origem_var = tk.StringVar()
        destino_var = tk.StringVar()
        peso_var = tk.StringVar(value="1")  # Valor padrão para peso

        # Função para pegar os valores e fechar a janela
        def submit_aresta():
            origem = origem_var.get().strip() # Remover espaços em branco
            destino = destino_var.get().strip() # Remover espaços em branco
            peso_str = peso_var.get().strip() # Remover espaços em branco

            if not origem or not destino:
                messagebox.showerror("Erro", "Origem e Destino não podem ser vazios.", parent=input_window)
                return

            try:
                peso = float(peso_str) if self.var_pond.get() else 1
            except ValueError:
                messagebox.showerror("Erro", "Peso deve ser um número válido.", parent=input_window)
                return

            # Adiciona os vértices ao grafo se não existirem
            for v in (origem, destino):
                self.grafo.adicionar_vertice(v)
            
            # Adiciona a aresta
            self.grafo.adicionar_aresta(origem, destino, peso)
            self.history.append((origem, destino, peso))
            self.text.insert(tk.END, f'{origem}→{destino} (peso {peso:.0f})\n')
            self.layout()
            self.redraw()
            input_window.destroy() # Fecha a janela de input

        # Layout da janela de input
        tk.Label(input_window, text="Origem:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(input_window, textvariable=origem_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_window, text="Destino:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(input_window, textvariable=destino_var).grid(row=1, column=1, padx=5, pady=5)

        # Exibe o campo de peso apenas se o grafo for ponderado
        if self.var_pond.get():
            tk.Label(input_window, text="Peso:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
            tk.Entry(input_window, textvariable=peso_var).grid(row=2, column=1, padx=5, pady=5)
        else:
            peso_var.set("1") # Garante que o peso seja 1 se não for ponderado

        tk.Button(input_window, text="Adicionar", command=submit_aresta).grid(row=3, column=0, columnspan=2, pady=10)

        # Atualiza a janela para obter as dimensões corretas
        input_window.update_idletasks()

        # Calcula a posição para centralizar a janela
        window_width = input_window.winfo_width()
        window_height = input_window.winfo_height()
        screen_width = input_window.winfo_screenwidth()
        screen_height = input_window.winfo_screenheight()

        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        input_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Garante que a janela de input seja modal
        input_window.transient(self.master)
        input_window.grab_set()
        self.master.wait_window(input_window)

    def undo_aresta(self):
        """Remove a última aresta adicionada, atualizando grafo e canvas."""
        if not self.history:
            messagebox.showinfo('Info', 'Nenhuma aresta para desfazer.')
            return
        o, d, p = self.history.pop()
        self.grafo.remover_aresta(o, d, p)
        self.text.insert(tk.END, f'Desfeito: {o}→{d} (peso {p})\n')
        self.redraw()

    def clear_graph(self):
        """Limpa completamente o grafo, histórico e canvas."""
        self.grafo.limpar()
        self.history.clear()
        self.text.delete('1.0', tk.END)
        self.canvas.delete('all')

    def run(self):
        """
        Solicita vértice inicial, executa Dijkstra e imprime
        todos os caminhos e custos no painel de texto.
        """
        start = simpledialog.askstring('Start', 'Vértice inicial:')
        if not start or start not in self.grafo.vertices:
            return
        self.text.insert(tk.END, '\n--- Dijkstra ---\n')
        for line in self.grafo.obter_caminhos(start):
            self.text.insert(tk.END, line + '\n')

    def show_verts(self):
        """Exibe todos os vértices cadastrados no painel de texto."""
        verts = ','.join(self.grafo.vertices.keys())
        self.text.insert(tk.END, 'Vertices: ' + verts + '\n')

if __name__ == '__main__':
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()



"""
Exemplos:

Exemplo Simples:

A → B (peso 2)
B → C (peso 9)
A → C (peso 5)
C → D (peso 1)


Grafo com ciclo e vértice isolado

A → B (peso 4)
A → C (peso 2)
B → C (peso 5)
B → D (peso 10)
C → E (peso 3)
E → D (peso 4)
D → C (peso 1)    # ciclo de retorno
F                 # vértice isolado (crie com Origem=F, Destino=F, Peso=0 mas depois ignore)


Grafo dirigido parcialmente desconectado

1 → 2 (1)
1 → 3 (4)
2 → 3 (2)
2 → 4 (7)
3 → 5 (3)
5 → 4 (2)
6 → 7 (5)   # componente separado
7 → 2 (1)
4 → 1 (6)   # volta para 1, formando ciclo


Grafo “maluco” com pesos zero e múltiplas rotas

S → A (0)
S → B (2)
A → C (1)
B → C (1)
C → D (3)
A → D (7)
B → D (4)
D → E (0)
E → F (5)
F → D (2)   # ciclo de peso positivo


Só direcionado, sem pesos (ponderado desmarcado)

A → B
B → C
C → D
D → B   # cria um ciclo B→C→D→B
E → F   # componente separado


Só ponderado, sem direção (direcionado desmarcado)
1 — 2 (3)
2 — 3 (5)
3 — 4 (2)
1 — 4 (10)
4 — 5 (1)

"""