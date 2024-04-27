from collections import deque

class Vertice:
    def __init__(self, estado):
        self.estado = estado
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

    # cria vertices para o quebra-cabeca de 8 pecas
    def cria_vertices(self):
        for i in range(3):
            for j in range(3):
                vertice = Vertice([i, j])
                self.adiciona_vertice(vertice)
        

    def cria_arestas(self, vertice):
        estados_possiveis = gera_estados_possiveis(vertice.estado)
        for estado in estados_possiveis:
            novo_vertice = self.procura_estado(estado)
            if novo_vertice:
                vertice.adiciona_adjacente(novo_vertice, 1)

    def adiciona_vertice(self, vertice):
        self.vertices.append(vertice)

    def procura_estado(self, estado):
        for vertice in self.vertices:
            if vertice.estado == estado:
                return vertice
            
        novo_vertice = Vertice(estado)
        self.adiciona_vertice(novo_vertice)
        return novo_vertice


class Resolucao:

    def __init__(self, estado_inicial, estado_final):
        self.grafo = Grafo()
        vertice_inicial = Vertice(estado_inicial)
        vertice_final = Vertice(estado_final)

        self.grafo.adiciona_vertice(vertice_inicial)
        self.grafo.adiciona_vertice(vertice_final)

        self.estado_inicial = vertice_inicial
        self.estado_final = vertice_final

    
    def heuristica(self, vertice):
        custo = 0
        for i in range(3):
            for j in range(3):
                if vertice.estado[i][j] != self.estado_final.estado[i][j]:
                    numero = vertice.estado[i][j]
                    i_final, j_final = None, None
                    for k in range(3):
                        for l in range(3):
                            if self.estado_final.estado[k][l] == numero:
                                i_final, j_final = k, l
                                break

                    custo += abs(i - i_final) + abs(j - j_final)
                    
        return custo

    
    def busca_gulosa(self):
        fila = [(self.estado_inicial, [], 0)]  # Fila de prioridade ordenada pela heurística
        nos_abertos = set()
        nos_fechados = set()
        arvore_busca = {self.estado_inicial: []}

        while fila:
            fila.sort(key=lambda x: x[2])
            vertice_atual, passo_a_passo_atual, custo_total = fila.pop(0)
            vertice_atual.visitado = True
            
            if vertice_atual in nos_abertos:
                nos_abertos.remove(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, arvore_busca, custo_total
            
            self.grafo.cria_arestas(vertice_atual)

            for adjacente in vertice_atual.adjacentes:
                if not adjacente[0].visitado:
                    
                    custo_adjacente = adjacente[1]
                    
                    if adjacente[0] not in nos_abertos:
                        nos_abertos.add(adjacente[0])
                        fila.append((adjacente[0], passo_a_passo_atual + [(adjacente[0], custo_adjacente)], custo_total + custo_adjacente))
                        
                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente[0])
                else:
                    nos_fechados.add(adjacente[0])

            print()
            print("Nós abertos:")
            for vertice in nos_abertos:
                print(vertice.estado[0])
                print(vertice.estado[1])
                print(vertice.estado[2])
                print()

            print("Nó atual:")
            print(vertice_atual.estado[0])
            print(vertice_atual.estado[1])
            print(vertice_atual.estado[2])
            print()

            print("Nós fechados:")
            for vertice in nos_fechados:
                print(vertice.estado[0])
                print(vertice.estado[1])
                print(vertice.estado[2])        
                print()
            print()

            nos_fechados.add(vertice_atual)


        self.grafo.reset_visitas()
        return passo_a_passo_atual, arvore_busca, custo_total
    
    def busca_gulosa_heuristica(self):
        fila = [(self.estado_inicial, [], 0)]  # Fila de prioridade ordenada pela heurística
        nos_abertos = set()
        nos_fechados = set()
        arvore_busca = {self.estado_inicial: []}

        while fila:
            fila.sort(key=lambda x: self.heuristica(x[0]))
            vertice_atual, passo_a_passo_atual, custo_total = fila.pop(0)
            vertice_atual.visitado = True
            
            if vertice_atual in nos_abertos:
                nos_abertos.remove(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, arvore_busca, custo_total
            
            self.grafo.cria_arestas(vertice_atual)

            for adjacente in vertice_atual.adjacentes:
                if not adjacente[0].visitado:
                    
                    custo_adjacente = adjacente[1]
                    
                    if adjacente[0] not in nos_abertos:
                        nos_abertos.add(adjacente[0])
                        fila.append((adjacente[0], passo_a_passo_atual + [(adjacente[0], custo_adjacente)], custo_total + custo_adjacente))
                        
                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente[0])
                else:
                    nos_fechados.add(adjacente[0])

            print()
            print("Nós abertos:")
            for vertice in nos_abertos:
                print(vertice.estado[0])
                print(vertice.estado[1])
                print(vertice.estado[2])
                print()

            print("Nó atual:")
            print(vertice_atual.estado[0])
            print(vertice_atual.estado[1])
            print(vertice_atual.estado[2])
            print()

            print("Nós fechados:")
            for vertice in nos_fechados:
                print(vertice.estado[0])
                print(vertice.estado[1])
                print(vertice.estado[2])        
                print()
            print()

            nos_fechados.add(vertice_atual)

        self.grafo.reset_visitas()
        return passo_a_passo_atual, arvore_busca, custo_total
    

    def busca_a_estrela(self):
        fila = [(self.estado_inicial, [], 0)]  # Fila de prioridade ordenada pela heurística
        nos_abertos = set()
        nos_fechados = set()
        arvore_busca = {self.estado_inicial: []}

        while fila:
            fila.sort(key=lambda x: x[2] + self.heuristica(x[0]))  # Ordena pela soma do custo total ate o momento e da heurística
            vertice_atual, passo_a_passo_atual, custo_total = fila.pop(0)
            vertice_atual.visitado = True
            
            if vertice_atual in nos_abertos:
                nos_abertos.remove(vertice_atual)

            if vertice_atual == self.estado_final:
                self.grafo.reset_visitas()
                return passo_a_passo_atual, arvore_busca, custo_total
            
            self.grafo.cria_arestas(vertice_atual)

            for adjacente in vertice_atual.adjacentes:
                if not adjacente[0].visitado:
                    custo_adjacente = adjacente[1]

                    if adjacente[0] not in nos_abertos:
                        nos_abertos.add(adjacente[0])
                        fila.append((adjacente[0], passo_a_passo_atual + [(adjacente[0], custo_adjacente)], custo_total + custo_adjacente))

                    arvore_busca.setdefault(vertice_atual, [])
                    arvore_busca[vertice_atual].append(adjacente[0])
                else:
                    nos_fechados.add(adjacente[0])

            print()
            print("Nós abertos:")
            for vertice in nos_abertos:
                print(vertice.estado[0])
                print(vertice.estado[1])
                print(vertice.estado[2])
                print()

            print("Nó atual:")
            print(vertice_atual.estado[0])
            print(vertice_atual.estado[1])
            print(vertice_atual.estado[2])
            print()

            print("Nós fechados:")
            for vertice in nos_fechados:
                print(vertice.estado[0])
                print(vertice.estado[1])
                print(vertice.estado[2])        
                print()
            print()

            nos_fechados.add(vertice_atual)

        self.grafo.reset_visitas()
        return passo_a_passo_atual, arvore_busca, custo_total


def gera_estados_possiveis(estado):
    estados_possiveis = []
    vazio_i, vazio_j = None, None

    # Encontra a posição do espaço vazio (representado por " ")
    for i in range(3):
        for j in range(3):
            if estado[i][j] == " ":
                vazio_i, vazio_j = i, j
                break

    # Movimentos possíveis: cima, baixo, esquerda, direita
    movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Gera os novos estados possíveis após um único movimento
    for movimento in movimentos:
        novo_i, novo_j = vazio_i + movimento[0], vazio_j + movimento[1]

        # Verifica se o novo movimento está dentro dos limites do tabuleiro
        if 0 <= novo_i < 3 and 0 <= novo_j < 3:
            novo_estado = [list(row) for row in estado]  # Cria uma cópia do estado atual

            # Realiza a troca entre a peça vazia e a peça adjacente
            novo_estado[vazio_i][vazio_j], novo_estado[novo_i][novo_j] = novo_estado[novo_i][novo_j], novo_estado[vazio_i][vazio_j]

            estados_possiveis.append(novo_estado)

    return estados_possiveis
    

def print_resultados(passo_a_passo, arvore_busca, custo, arvore):
    print("Passo a passo:")
    print("Custo total:", custo)
    print()
    for passo in passo_a_passo:
        print(passo[0].estado[0])
        print(passo[0].estado[1])
        print(passo[0].estado[2])
        print("Custo:", passo[1])
        print()

    if arvore == False:
        return

    print("\nÁrvore de busca:")
    for no in arvore_busca:
        print(no.estado[0])
        print(no.estado[1])
        print(no.estado[2])
        print()
        for adjacente in arvore_busca[no]:
            print("  ->", adjacente.estado[0])
            print("  ->", adjacente.estado[1])
            print("  ->", adjacente.estado[2])
            print()

    

# Definindo o estado inicial e final
estado_inicial = [["1", "3", "4"], 
                  ["8", "2", "5"], 
                  ["7", "6", " "]]

estado_final = [["1", "2", "3"], 
                ["8", " ", "4"], 
                ["7", "6", "5"]]


# Executando a busca em largura e imprimindo o resultado

print("\n\n-----------------BUSCA GULOSA------------------\n\n")

resolucao = Resolucao(estado_inicial, estado_final)
passo_a_passo, arvore_busca, custo = resolucao.busca_gulosa()
print_resultados(passo_a_passo, arvore_busca, custo, True)

# Executando a busca gulosa com heuristica e imprimindo o resultado


print("\n\n-----------------BUSCA GULOSA COM HEURISTICA------------------\n\n")

resolucao = Resolucao(estado_inicial, estado_final)
passo_a_passo, arvore_busca, custo = resolucao.busca_gulosa_heuristica()
print_resultados(passo_a_passo, arvore_busca, custo, True)

#Executando a busca A Estrela e imprimindo o resultado


print("\n\n-----------------BUSCA A ESTRELA------------------\n\n")

passo_a_passo, arvore_busca, custo = resolucao.busca_a_estrela()
print_resultados(passo_a_passo, arvore_busca, custo, False)


# Executando a busca A Estrela com nova entrada e imprimindo o resultado

print("\n\n-----------------BUSCA A ESTRELA - NOVA ENTRADA ------------------\n\n")

estado_inicial = [["1", "2", "3"], 
                  [" ", "6", "4"], 
                  ["8", "7", "5"]]

resolucao = Resolucao(estado_inicial, estado_final)

passo_a_passo, arvore_busca, custo = resolucao.busca_a_estrela()
print_resultados(passo_a_passo, arvore_busca, custo, True)