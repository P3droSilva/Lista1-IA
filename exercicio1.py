from collections import deque

class Vertice:
    def __init__(self, missionarios, canibais, barco):
        self.missionarios = missionarios
        self.canibais = canibais
        self.barco = barco
        self.adjacentes = []
        self.visitado = False

    def adiciona_adjacente(self, vertice):
        if vertice not in self.adjacentes:
            self.adjacentes.append(vertice)


class Grafo:
    def __init__(self, maxMissionarios, maxCanibais):
        self.vertices = []
        self.maxMissionarios = maxMissionarios
        self.maxCanibais = maxCanibais

    def adiciona_vertice(self, vertice):
        self.vertices.append(vertice)

    def adiciona_aresta(self, vertice_origem, vertice_destino):
        vertice_origem.adiciona_adjacente(vertice_destino)

    def cria_vertices(self):
        for missionarios in range(self.maxMissionarios + 1):
            for canibais in range(self.maxCanibais + 1):
                for barco in ["esq", "dir"]:
                    vertice = Vertice(missionarios, canibais, barco)
                    self.adiciona_vertice(vertice)

    def cria_arestas(self):
        for vertice in self.vertices:
            for acao in [levar1M, levar2M, levar1C, levar2C, levar1M1C, voltar1M, voltar2M, voltar1C, voltar2C, voltar1M1C]:
                novo_estado = acao(vertice, self.maxMissionarios, self.maxCanibais)
                if novo_estado:
                    novo_vertice = self.procura_estado(novo_estado)
                    if novo_vertice and estado_valido(novo_vertice, self.maxMissionarios, self.maxCanibais):
                        self.adiciona_aresta(vertice, novo_vertice)

    def procura_estado(self, estado):
        for vertice in self.vertices:
            if vertice.missionarios == estado[0] and vertice.canibais == estado[1] and vertice.barco == estado[2]:
                return vertice
        return None

    def print_grafo(self):
        for vertice in self.vertices:
            print("Missionarios {} Canibais {} Barco {}".format(vertice.missionarios, vertice.canibais, vertice.barco))
            print("  Adjacentes:")
            for adjacente in vertice.adjacentes:
                print("    Missionarios {} Canibais {} Barco {}".format(adjacente.missionarios, adjacente.canibais, adjacente.barco))
            print()

class Resolucao:

    def __init__(self, N):
        self.grafo = Grafo(N, N)
        self.grafo.cria_vertices()
        self.grafo.cria_arestas()
        self.estado_inicial = None
        self.estado_final = None

        for vertice in self.grafo.vertices:
            if vertice.missionarios == N and vertice.canibais == N and vertice.barco == "esq":
                self.estado_inicial = vertice

            if vertice.missionarios == 0 and vertice.canibais == 0 and vertice.barco == "dir":
                self.estado_final = vertice

        #self.grafo.print_grafo()


    def busca_em_largura(self):
        fila = deque([(self.estado_inicial, [])])
        nos_abertos = []
        nos_fechados = []
        arvore_busca = {self.estado_inicial: []}

        while fila:
            vertice_atual, passo_a_passo_atual = fila.popleft()
            nos_abertos.append(vertice_atual)
            vertice_atual.visitado = True

            if vertice_atual == self.estado_final:
                return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca
            
            for adjacente in vertice_atual.adjacentes:
                if not adjacente.visitado:
                    fila.append((adjacente, passo_a_passo_atual + [adjacente]))
                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente)
                else:
                    nos_fechados.append(adjacente)

        return passo_a_passo_atual ,nos_abertos, nos_fechados, arvore_busca

    def busca_em_profundidade(self):
        pilha = [(self.estado_inicial, [])]
        nos_abertos = []
        nos_fechados = []
        arvore_busca = {self.estado_inicial: []}

        while pilha:
            vertice_atual, passo_a_passo_atual = pilha.pop()
            nos_abertos.append(vertice_atual)
            vertice_atual.visitado = True

            if vertice_atual == self.estado_final:
                return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca

            for adjacente in vertice_atual.adjacentes:
                if not adjacente.visitado:
                    pilha.append((adjacente, passo_a_passo_atual + [adjacente]))
                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente)
                else:
                    nos_fechados.append(adjacente)

        return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca
    

def estado_valido(vertice, maxMissionarios, maxCanibais):
    if vertice.missionarios < 0 or vertice.missionarios > maxMissionarios:
        return False
    
    if vertice.canibais < 0 or vertice.canibais > maxCanibais:
        return False
    
    if vertice.missionarios < vertice.canibais and vertice.missionarios > 0:
        return False
    
    if maxCanibais - vertice.canibais > maxMissionarios - vertice.missionarios and maxMissionarios - vertice.missionarios > 0:
        return False
    
    return True

def levar1M(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "esq" and vertice.missionarios >= 1:
        return [vertice.missionarios - 1, vertice.canibais, "dir"]
    
def levar2M(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "esq" and vertice.missionarios >= 2:
        return [vertice.missionarios - 2, vertice.canibais, "dir"]
    
def levar1C(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "esq" and vertice.canibais >= 1:
        return [vertice.missionarios, vertice.canibais - 1, "dir"]
    
def levar2C(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "esq" and vertice.canibais >= 2:
        return [vertice.missionarios, vertice.canibais - 2, "dir"]
    
def levar1M1C(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "esq" and vertice.missionarios >= 1 and vertice.canibais >= 1:
        return [vertice.missionarios - 1, vertice.canibais - 1, "dir"]
    
def voltar1M(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "dir" and maxMissionarios - vertice.missionarios >= 1:
        return [vertice.missionarios + 1, vertice.canibais, "esq"]
    
def voltar2M(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "dir" and maxMissionarios - vertice.missionarios >= 2:
        return [vertice.missionarios + 2, vertice.canibais, "esq"]
    
def voltar1C(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "dir" and maxCanibais - vertice.canibais >= 1:
        return [vertice.missionarios, vertice.canibais + 1, "esq"]
    
def voltar2C(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "dir" and maxCanibais - vertice.canibais >= 2:
        return [vertice.missionarios, vertice.canibais + 2, "esq"]
    
def voltar1M1C(vertice, maxMissionarios, maxCanibais):
    if vertice.barco == "dir" and maxMissionarios - vertice.missionarios >= 1 and maxCanibais - vertice.canibais >= 1:
        return [vertice.missionarios + 1, vertice.canibais + 1, "esq"]
    





# Executando a busca em largura e imprimindo o resultado
N = 3
resolucao = Resolucao(N)
passo_a_passo, nos_abertos, nos_fechados, arvore_busca = resolucao.busca_em_largura()

print("\nPasso a passo: ")
for vertice in passo_a_passo:
    print("  Esq: Missionarios {} Canibais {}\n  Barco {}\n  Dir: Missionarios {} Canibais {}\n".format(vertice.missionarios, vertice.canibais, vertice.barco, N - vertice.missionarios, N - vertice.canibais))

print("\nNós abertos:")
for vertice in nos_abertos:
    print("  Missionarios {} Canibais {} Barco {}".format(vertice.missionarios, vertice.canibais, vertice.barco))

print("\nNós fechados:")
for vertice in nos_fechados:
    print("  Missionarios {} Canibais {} Barco {}".format(vertice.missionarios, vertice.canibais, vertice.barco))

print("\nÁrvore de busca:")
for vertice, adjacentes in arvore_busca.items():
    print("  Missionarios {} Canibais {} Barco {}".format(vertice.missionarios, vertice.canibais, vertice.barco))
    print("    Adjacentes:")
    for adjacente in adjacentes:
        print("      Missionarios {} Canibais {} Barco {}".format(adjacente.missionarios, adjacente.canibais, adjacente.barco))
    print()
