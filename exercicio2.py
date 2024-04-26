from collections import deque

class Vertice:
    def __init__(self, jaarro1, jarro2):
        self.jarro1 = jaarro1
        self.jarro2 = jarro2
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
        for jarro1 in range(3 + 1):
            for jarro2 in range(4 + 1):
                vertice = Vertice(jarro1, jarro2)
                self.adiciona_vertice(vertice)

    def cria_arestas(self):
        for vertice in self.vertices:
            for acao in [enche1, enche2, esvazia1, esvazia2, despeja1em2, despeja2em1]:
                novo_estado = acao(vertice)
                if novo_estado:
                    novo_vertice = self.procura_estado(novo_estado)
                    if novo_vertice and estado_valido(novo_vertice):
                        self.adiciona_aresta(vertice, novo_vertice)

    def procura_estado(self, estado):
        for vertice in self.vertices:
            if vertice.jarro1 == estado[0] and vertice.jarro2 == estado[1]:
                return vertice
        return None

    def print_grafo(self):
        for vertice in self.vertices:
            print("Jarro1 {} Jarro2 {}".format(vertice.jarro1, vertice.jarro2))
            print("  Adjacentes:")
            for adjacente in vertice.adjacentes:
                print("    Jarro1 {} Jarro2 {}".format(adjacente.jarro1, adjacente.jarro2))
            print()

class Resolucao:

    def __init__(self, estado_inicial, estado_final):
        self.grafo = Grafo()
        self.grafo.cria_vertices()
        self.grafo.cria_arestas()
        self.estado_inicial = None
        self.estados_finais = []

        for vertice in self.grafo.vertices:
            if vertice.jarro1 == estado_inicial[0] and vertice.jarro2 == estado_inicial[1]:
                self.estado_inicial = vertice

            if (vertice.jarro1 == estado_final[0] or estado_final[0] == "X") and (vertice.jarro2 == estado_final[1] or estado_final[1] == "X"):
                self.estados_finais.append(vertice)

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

            if vertice_atual in self.estados_finais:
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

            if vertice_atual in self.estados_finais:
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
    if vertice.jarro1 < 0 or vertice.jarro1 > 3:
        return False
    if vertice.jarro2 < 0 or vertice.jarro2 > 4:
        return False
    return True

def enche1(vertice):
    return [3, vertice.jarro2]

def enche2(vertice):
    return [vertice.jarro1, 4]

def esvazia1(vertice):
    return [0, vertice.jarro2]

def esvazia2(vertice):
    return [vertice.jarro1, 0]

def despeja1em2(vertice):
    total = vertice.jarro1 + vertice.jarro2
    if total <= 4:
        return [0, total]
    else:
        return [total - 4, 4]

def despeja2em1(vertice):
    total = vertice.jarro1 + vertice.jarro2
    if total <= 3:
        return [total, 0]
    else:
        return [3, total - 3]


# Executando a busca em largura e imprimindo o resultado
estado_inicial = [0, 0]
estado_final = ["X", 2]
resolucao = Resolucao(estado_inicial, estado_final)
passo_a_passo, nos_abertos, nos_fechados, arvore_busca = resolucao.busca_em_largura()

print("\nPasso a passo: ")
for vertice in passo_a_passo:
    print("  Jarro1 {} Jarro2 {}".format(vertice.jarro1, vertice.jarro2))

print("\nNós abertos:")
for vertice in nos_abertos:
    print("  Jarro1 {} Jarro2 {}".format(vertice.jarro1, vertice.jarro2))

print("\nNós fechados:")
for vertice in nos_fechados:
    print("  Jarro1 {} Jarro2 {}".format(vertice.jarro1, vertice.jarro2))

print("\nÁrvore de busca:")
for vertice, adjacentes in arvore_busca.items():
    print("  Jarro1 {} Jarro2 {}".format(vertice.jarro1, vertice.jarro2))
    print("    Adjacentes:")
    for adjacente in adjacentes:
        print("      Jarro1 {} Jarro2 {}".format(adjacente.jarro1, adjacente.jarro2))
    print()
