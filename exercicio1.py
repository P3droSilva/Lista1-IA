class Estado:
    def __init__(self, missionarios, canibais, barco):
        self.missionarios = missionarios
        self.canibais = canibais
        self.barco = barco
        self.pai = None

    def __eq__(self, other):
        return self.missionarios == other.missionarios and \
               self.canibais == other.canibais and \
               self.barco == other.barco

    def __hash__(self):
        return hash((self.missionarios, self.canibais, self.barco))

    def __str__(self):
        return f'M: {self.missionarios}, C: {self.canibais}, B: {self.barco}'

    def __repr__(self):
        return str(self)


def validar_estado(estado):
    if estado.missionarios < 0 or estado.canibais < 0 or \
       estado.missionarios > N or estado.canibais > N or \
       (estado.missionarios != 0 and estado.missionarios < estado.canibais) or \
       (estado.missionarios != N and N - estado.missionarios < N - estado.canibais):
        return False
    return True


def gerar_filhos(estado):
    filhos = []
    for i in range(M + 1):
        for j in range(C + 1):
            if 1 <= i + j <= O and (i > 0 or j > 0):
                if estado.barco == 1:
                    novo_estado = Estado(estado.missionarios - i, estado.canibais - j, 0)
                else:
                    novo_estado = Estado(estado.missionarios + i, estado.canibais + j, 1)
                novo_estado.pai = estado
                if validar_estado(novo_estado):
                    filhos.append(novo_estado)
    return filhos


def busca_largura():
    inicial = Estado(N, N, 1)
    if not validar_estado(inicial):
        return None

    visitados = set()
    fila = [inicial]

    while fila:
        estado_atual = fila.pop(0)
        visitados.add(estado_atual)

        if estado_atual.missionarios == 0 and estado_atual.canibais == 0 and estado_atual.barco == 0:
            return estado_atual

        filhos = gerar_filhos(estado_atual)
        for filho in filhos:
            if filho not in visitados and filho not in fila:
                fila.append(filho)

    return None


N = 3  # Número de missionários e canibais
M = C = N  # Número máximo de missionários e canibais em cada lado
O = 2  # Número máximo de pessoas no barco

solucao = busca_largura()
if solucao:
    caminho = []
    while solucao:
        caminho.append(solucao)
        solucao = solucao.pai
    caminho.reverse()
    for estado in caminho:
        print(estado)
else:
    print("Não há solução possível.")
