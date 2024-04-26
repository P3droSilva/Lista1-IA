from collections import deque

class Vertice:
    def __init__(self, cidade):
        self.cidade = cidade
        self.adjacentes = []
        self.visitado = False

    def adiciona_adjacente(self, vertice):
        if vertice not in self.adjacentes:
            self.adjacentes.append(vertice)


class Grafo:
    def __init__(self):
        self.vertices = []

    def adiciona_vertice(self, vertice):
        self.vertices.append(vertice)

    def adiciona_aresta(self, vertice_origem, vertice_destino):
        vertice_origem.adiciona_adjacente(vertice_destino)

    def reset_visitas(self):
        for vertice in self.vertices:
            vertice.visitado = False

    def cria_vertices(self):
        cidades = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        for cidade in cidades:
            vertice = Vertice(cidade)
            self.adiciona_vertice(vertice)

    def cria_arestas(self):
        for vertice in self.vertices:
            for acao in [oper1, oper3, oper4, oper5, oper6, oper7, oper8, oper9, oper10, oper11, oper12, oper13, oper14, oper15, oper16, oper17, oper18, oper19]:
                novo_estado = acao(vertice)
                if novo_estado:
                    novo_vertice = self.procura_estado(novo_estado)
                    if novo_vertice and estado_valido(novo_vertice):
                        self.adiciona_aresta(vertice, novo_vertice)

    def procura_estado(self, estado):
        for vertice in self.vertices:
            if vertice.cidade == estado:
                return vertice
        return None

    def print_grafo(self):
        for vertice in self.vertices:
            print("Cidade {}".format(vertice.cidade))
            print("  Adjacentes:")
            for adjacente in vertice.adjacentes:
                print("    Cidade {}".format(adjacente.cidade))
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

        #self.grafo.print_grafo()


    def busca_em_largura(self):
        fila = deque([(self.estado_inicial, [])])
        nos_abertos = []
        nos_fechados = []
        arvore_busca = {self.estado_inicial: []}

        while fila:
            vertice_atual, passo_a_passo_atual = fila.popleft()
            vertice_atual.visitado = True
            if vertice_atual not in nos_abertos:
                nos_abertos.append(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca
            
            for adjacente in vertice_atual.adjacentes:
                if not adjacente.visitado:
                    
                    if adjacente not in nos_abertos:
                        nos_abertos.append(adjacente)
                        fila.append((adjacente, passo_a_passo_atual + [adjacente]))

                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente)
                else:
                    nos_fechados.append(adjacente)
        
        self.grafo.reset_visitas()
        return passo_a_passo_atual ,nos_abertos, nos_fechados, arvore_busca

    def busca_em_profundidade(self):
        pilha = [(self.estado_inicial, [])]
        nos_abertos = []
        nos_fechados = []
        arvore_busca = {self.estado_inicial: []}

        while pilha:
            vertice_atual, passo_a_passo_atual = pilha.pop()
            vertice_atual.visitado = True
            if vertice_atual not in nos_abertos:
                nos_abertos.append(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca

            for adjacente in vertice_atual.adjacentes:
                if not adjacente.visitado:

                    if adjacente not in nos_abertos:
                        nos_abertos.append(adjacente)
                        pilha.append((adjacente, passo_a_passo_atual + [adjacente]))
                        
                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente)
                else:
                    nos_fechados.append(adjacente)

        self.grafo.reset_visitas()
        return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca
    

def estado_valido(vertice):
    if vertice.cidade in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]:
        return True

def oper1(vertice):
    if vertice.cidade == "A":
        return "B"
    
def oper3(vertice):
    if vertice.cidade == "A":
        return "D"

def oper4(vertice):
    if vertice.cidade == "B":
        return "E"
    
def oper5(vertice):
    if vertice.cidade == "B":
        return "F"
    
def oper6(vertice):
    if vertice.cidade == "C":
        return "G"
    
def oper7(vertice):
    if vertice.cidade == "C":
        return "H"
    
def oper8(vertice):
    if vertice.cidade == "C":
        return "I"
    
def oper9(vertice):
    if vertice.cidade == "D":
        return "J"
    
def oper10(vertice):
    if vertice.cidade == "E":
        return "K"
    
def oper11(vertice):
    if vertice.cidade == "E":
        return "L"
    
def oper12(vertice):
    if vertice.cidade == "G":
        return "M"
    
def oper13(vertice):
    if vertice.cidade == "J":
        return "N"
    
def oper14(vertice):
    if vertice.cidade == "J":
        return "O"
    
def oper15(vertice):
    if vertice.cidade == "K":
        return "F"
    
def oper16(vertice):
    if vertice.cidade == "L":
        return "H"
    
def oper17(vertice):
    if vertice.cidade == "M":
        return "D"

def oper18(vertice):
    if vertice.cidade == "O":
        return "A"
    
def oper19(vertice):
    if vertice.cidade == "N":
        return "B"

# Definindo o estado inicial e final
estado_inicial = "A"
estado_final = "J"
resolucao = Resolucao(estado_inicial, estado_final)

# Executando a busca em largura e imprimindo o resultado
passo_a_passo, nos_abertos, nos_fechados, arvore_busca = resolucao.busca_em_largura()

print("\n\n-----------------BUSCA EM LARGURA------------------\n\n")

print("\nPasso a passo: ")
for vertice in passo_a_passo:
    print("  Cidade {}".format(vertice.cidade))

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


# Executando a busca em profundidade e imprimindo o resultado
passo_a_passo, nos_abertos, nos_fechados, arvore_busca = resolucao.busca_em_profundidade()

print("\n\n-----------------BUSCA EM PROFUNDIDADE------------------\n\n")

print("\nPasso a passo: ")
for vertice in passo_a_passo:
    print("  Cidade {}".format(vertice.cidade))

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
