from collections import deque

class Vertice:
    def __init__(self, fazendeiro, lobo, ovelha, repolho):
        self.fazendeiro = fazendeiro
        self.lobo = lobo
        self.ovelha = ovelha
        self.repolho = repolho
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

    def cria_vertices(self):
        for fazendeiro in ["esq", "dir"]:
            for lobo in ["esq", "dir"]:
                for ovelha in ["esq", "dir"]:
                    for repolho in ["esq", "dir"]:
                        vertice = Vertice(fazendeiro, lobo, ovelha, repolho)
                        self.adiciona_vertice(vertice)

    def cria_arestas(self):
        for vertice in self.vertices:
            for acao in [vai, leva_lobo, leva_ovelha, leva_repolho, volta, traz_lobo, traz_ovelha, traz_repolho]:
                novo_estado = acao(vertice)
                if novo_estado:
                    novo_vertice = self.procura_estado(novo_estado)
                    if novo_vertice and estado_valido(novo_vertice):
                        self.adiciona_aresta(vertice, novo_vertice)

    def procura_estado(self, estado):
        for vertice in self.vertices:
            if vertice.fazendeiro == estado[0] and vertice.lobo == estado[1] and vertice.ovelha == estado[2] and vertice.repolho == estado[3]:
                return vertice
        return None

    def print_grafo(self):
        for vertice in self.vertices:
            print("Fazendeiro {} Lobo {} Ovelha {} Repolho {}".format(vertice.fazendeiro, vertice.lobo, vertice.ovelha, vertice.repolho))
            print("  Adjacentes:")
            for adjacente in vertice.adjacentes:
                print("    Fazendeiro {} Lobo {} Ovelha {} Repolho {}".format(adjacente.fazendeiro, adjacente.lobo, adjacente.ovelha, adjacente.repolho))
            print()

class Resolucao:

    def __init__(self, estado_inicial, estado_final):
        self.grafo = Grafo()
        self.grafo.cria_vertices()
        self.grafo.cria_arestas()
        self.estado_inicial = None
        self.estado_final = None

        for vertice in self.grafo.vertices:
            if vertice.fazendeiro == estado_inicial[0] and vertice.lobo == estado_inicial[1] and vertice.ovelha == estado_inicial[2] and vertice.repolho == estado_inicial[3]:
                self.estado_inicial = vertice
            if vertice.fazendeiro == estado_final[0] and vertice.lobo == estado_final[1] and vertice.ovelha == estado_final[2] and vertice.repolho == estado_final[3]:
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

        return passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca
    

def estado_valido(vertice):
    if vertice.ovelha == vertice.repolho and vertice.ovelha != vertice.fazendeiro:
        return False
    if vertice.lobo == vertice.ovelha and vertice.lobo != vertice.fazendeiro:
        return False
    return True

def vai(vertice):
    if(vertice.fazendeiro == "esq"):
        return ["dir" , vertice.lobo, vertice.ovelha, vertice.repolho]
    
def leva_lobo(vertice):
    if vertice.fazendeiro == "esq" and vertice.lobo == "esq":
        return ["dir", "dir", vertice.ovelha, vertice.repolho]

def leva_ovelha(vertice):
    if vertice.fazendeiro == "esq" and vertice.ovelha == "esq":
        return ["dir", vertice.lobo, "dir", vertice.repolho]

def leva_repolho(vertice):
    if vertice.fazendeiro == "esq" and vertice.repolho == "esq":
        return ["dir", vertice.lobo, vertice.ovelha, "dir"]

def volta(vertice):
    if(vertice.fazendeiro == "dir"):
        return ["esq" , vertice.lobo, vertice.ovelha, vertice.repolho]

def traz_lobo(vertice):
    if vertice.fazendeiro == "dir" and vertice.lobo == "dir":
        return ["esq", "esq", vertice.ovelha, vertice.repolho]

def traz_ovelha(vertice):
    if vertice.fazendeiro == "dir" and vertice.ovelha == "dir":
        return ["esq", vertice.lobo, "esq", vertice.repolho]

def traz_repolho(vertice):
    if vertice.fazendeiro == "dir" and vertice.repolho == "dir":
        return ["esq", vertice.lobo, vertice.ovelha, "esq"]


# Executando a busca em largura e imprimindo o resultado
estado_inicial = ["esq", "esq", "esq", "esq"]
estado_final = ["dir", "dir", "dir", "dir"]
resolucao = Resolucao(estado_inicial, estado_final)
passo_a_passo, nos_abertos, nos_fechados, arvore_busca = resolucao.busca_em_profundidade()

print("\nPasso a passo: ")
for vertice in passo_a_passo:
    print("  Fazendeiro {} Lobo {} Ovelha {} Repolho {}".format(vertice.fazendeiro, vertice.lobo, vertice.ovelha, vertice.repolho))

print("\nNós abertos:")
for vertice in nos_abertos:
    print("  Fazendeiro {} Lobo {} Ovelha {} Repolho {}".format(vertice.fazendeiro, vertice.lobo, vertice.ovelha, vertice.repolho))

print("\nNós fechados:")
for vertice in nos_fechados:
    print("  Fazendeiro {} Lobo {} Ovelha {} Repolho {}".format(vertice.fazendeiro, vertice.lobo, vertice.ovelha, vertice.repolho))

if arvore_busca:
    print("\nÁrvore de busca:")
    for vertice_pai, vertices_filhos in arvore_busca.items():
        print("  Vertice pai: Fazendeiro {} Lobo {} Ovelha {} Repolho {}".format(vertice_pai.fazendeiro, vertice_pai.lobo, vertice_pai.ovelha, vertice_pai.repolho))
        print("    Vertices filhos:")
        for vertice_filho in vertices_filhos:
            print("      Fazendeiro {} Lobo {} Ovelha {} Repolho {}".format(vertice_filho.fazendeiro, vertice_filho.lobo, vertice_filho.ovelha, vertice_filho.repolho))
else:
    print("Nenhum resultado encontrado.")
