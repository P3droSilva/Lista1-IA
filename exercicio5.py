from collections import deque

class Vertice:
    def __init__(self, cidade):
        self.cidade = cidade
        self.adjacentes = []
        self.visitado = False

    def adiciona_adjacente(self, vertice, custo):
        if vertice not in self.adjacentes:
            self.adjacentes.append([vertice, custo])


class Grafo:
    def __init__(self):
        self.vertices = []

    def adiciona_vertice(self, vertice):
        self.vertices.append(vertice)

    def adiciona_aresta(self, vertice_origem, vertice_destino, custo):
        vertice_origem.adiciona_adjacente(vertice_destino, custo)
        vertice_destino.adiciona_adjacente(vertice_origem, custo)

    def reset_visitas(self):
        for vertice in self.vertices:
            vertice.visitado = False

    def cria_vertices(self):
        cidades = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for cidade in cidades:
            vertice = Vertice(cidade)
            self.adiciona_vertice(vertice)

    def cria_arestas(self):
        for vertice in self.vertices:
            for acao in [oper1, oper2, oper3, oper4, oper5, oper6, oper7, oper8, oper9, oper10, oper11, oper12]:
                novo_estado = acao(vertice)
                if novo_estado:
                    novo_vertice = self.procura_estado(novo_estado)
                    if novo_vertice and estado_valido(novo_vertice):
                        self.adiciona_aresta(vertice, novo_vertice, novo_estado[1])

    def procura_estado(self, estado):
        for vertice in self.vertices:
            if vertice.cidade == estado[0]:
                return vertice
        return None

    def print_grafo(self):
        print("\n\nGrafo:\n\n")
        for vertice in self.vertices:
            print("Cidade {}".format(vertice.cidade))
            print("  Adjacentes:")
            for adjacente in vertice.adjacentes:
                print("    Cidade {}  Custo {}".format(adjacente[0].cidade, adjacente[1]))
            print()

class Resolucao:

    def __init__(self, estado_inicial, estado_final):
        self.grafo = Grafo()
        self.grafo.cria_vertices()
        self.grafo.cria_arestas()
        self.estado_inicial = None
        self.estado_final = None

        for vertice in self.grafo.vertices:
            if vertice.cidade == estado_inicial:
                self.estado_inicial = vertice

            if vertice.cidade == estado_final:
                self.estado_final = vertice

        self.grafo.print_grafo()


    def busca_em_largura(self):
        fila = deque([(self.estado_inicial, [], 0)])   
        nos_abertos = []
        nos_fechados = []
        arvore_busca = {self.estado_inicial: []}

        while fila:
            vertice_atual, passo_a_passo_atual, custo_total = fila.popleft()   
            vertice_atual.visitado = True
            if vertice_atual not in nos_abertos:
                nos_abertos.append(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca, custo_total   

            for adjacente in vertice_atual.adjacentes:
                if not adjacente[0].visitado:

                    custo_adjacente = adjacente[1]  

                    if adjacente[0] not in nos_abertos:
                        nos_abertos.append(adjacente[0])
                        fila.append((adjacente[0], passo_a_passo_atual + [(adjacente[0], custo_adjacente)], custo_total + custo_adjacente))
                         
                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente[0])

                else:
                    nos_fechados.append(adjacente[0])

    

        self.grafo.reset_visitas()
        return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca, custo_total   

    def busca_em_profundidade(self):
        pilha = [(self.estado_inicial, [], 0)]   
        nos_abertos = []
        nos_fechados = []
        arvore_busca = {self.estado_inicial: []}

        while pilha:
            vertice_atual, passo_a_passo_atual, custo_total = pilha.pop()   
            vertice_atual.visitado = True
            if vertice_atual not in nos_abertos:
                nos_abertos.append(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca, custo_total   

            for adjacente in vertice_atual.adjacentes:
                if not adjacente[0].visitado:
                    
                    custo_adjacente = adjacente[1]  

                    if adjacente[0] not in nos_abertos:
                        nos_abertos.append(adjacente[0])
                        pilha.append((adjacente[0], passo_a_passo_atual + [(adjacente[0], custo_adjacente)], custo_total + custo_adjacente))

                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente[0])
                else:
                    nos_fechados.append(adjacente[0])

        self.grafo.reset_visitas()
        return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca, custo_total   
    
    def busca_gulosa(self):
        fila = [(self.estado_inicial, [], 0)]  # Fila de prioridade ordenada pela heurística
        nos_abertos = []
        nos_fechados = []
        arvore_busca = {self.estado_inicial: []}

        while fila:
            fila.sort(key=lambda x: x[2])
            vertice_atual, passo_a_passo_atual, custo_total = fila.pop(0)
            vertice_atual.visitado = True
            if vertice_atual not in nos_abertos:
                nos_abertos.append(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca, custo_total

            for adjacente in vertice_atual.adjacentes:
                if not adjacente[0].visitado:
                    
                    custo_adjacente = adjacente[1]
                    
                    if adjacente[0] not in nos_abertos:
                        nos_abertos.append(adjacente[0])
                        fila.append((adjacente[0], passo_a_passo_atual + [(adjacente[0], custo_adjacente)], custo_total + custo_adjacente))
                        
                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente[0])
                else:
                    nos_fechados.append(adjacente[0])

        self.grafo.reset_visitas()
        return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca, custo_total

    

def estado_valido(vertice):
    if vertice.cidade in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        return True

def oper1(vertice):
    if vertice.cidade == "A":
        return ["B", 1]
    
def oper2(vertice):
    if vertice.cidade == "A":
        return ["C", 9]

def oper3(vertice):
    if vertice.cidade == "A":
        return ["D", 4]
    
def oper4(vertice):
    if vertice.cidade == "B":
        return ["C", 7]
    
def oper5(vertice):
    if vertice.cidade == "B":
        return ["E", 6]
    
def oper6(vertice):
    if vertice.cidade == "B":
        return ["F", 1]
    
def oper7(vertice):
    if vertice.cidade == "C":
        return ["F", 7]
    
def oper8(vertice):
    if vertice.cidade == "D":
        return ["F", 4]
    
def oper9(vertice):
    if vertice.cidade == "D":
        return ["G", 5]
    
def oper10(vertice):
    if vertice.cidade == "E":
        return ["H", 9]
    
def oper11(vertice):
    if vertice.cidade == "F":
        return ["H", 4]
    
def oper12(vertice):
    if vertice.cidade == "G":
        return ["H", 1]
    

def print_resultados(passo_a_passo, nos_abertos, nos_fechados, arvore_busca, custo):
    print("\nCusto total: {}".format(custo))

    print("\nPasso a passo: ")
    for vertice in passo_a_passo:
        print("  Cidade {}  Custo {}".format(vertice[0].cidade, vertice[1]))

    print("\nNós abertos:")
    for vertice in nos_abertos:
        print("  Cidade {}".format(vertice.cidade))

    print("\nNós fechados:")
    for vertice in nos_fechados:
        print("  Cidade {}".format(vertice.cidade))

    print("\nÁrvore de busca:")
    for vertice, adjacentes in arvore_busca.items():
        print("  Cidade {}".format(vertice.cidade))
        print("    Adjacentes:")
        for adjacente in adjacentes:
            print("      Cidade {}".format(adjacente.cidade))
        print()

    

# Definindo o estado inicial e final
estado_inicial = "A"
estado_final = "H"
resolucao = Resolucao(estado_inicial, estado_final)

# Executando a busca em largura e imprimindo o resultado
passo_a_passo, nos_abertos, nos_fechados, arvore_busca, custo = resolucao.busca_em_largura()

print("\n\n-----------------BUSCA EM LARGURA------------------\n\n")

print_resultados(passo_a_passo, nos_abertos, nos_fechados, arvore_busca, custo)


# Executando a busca em profundidade e imprimindo o resultado
passo_a_passo, nos_abertos, nos_fechados, arvore_busca, custo = resolucao.busca_em_profundidade()

print("\n\n-----------------BUSCA EM PROFUNDIDADE------------------\n\n")

print_resultados(passo_a_passo, nos_abertos, nos_fechados, arvore_busca, custo)

# Executando a busca gulosa e imprimindo o resultado
passo_a_passo, nos_abertos, nos_fechados, arvore_busca, custo = resolucao.busca_gulosa()

print("\n\n-----------------BUSCA GULOSA------------------\n\n")

print_resultados(passo_a_passo, nos_abertos, nos_fechados, arvore_busca, custo)
