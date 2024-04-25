from collections import deque

class Estado:
    def __init__(self, jarro1, jarro2):
        self.jarro1 = jarro1
        self.jarro2 = jarro2

def estado_final(estado):
    return estado.jarro2 == 2

def enche1(estado):
    return Estado(3, estado.jarro2)

def enche2(estado):
    return Estado(estado.jarro1, 4)

def esvazia1(estado):
    return Estado(0, estado.jarro2)

def esvazia2(estado):
    return Estado(estado.jarro1, 0)

def despeja1em2(estado):
    total = estado.jarro1 + estado.jarro2
    if total <= 4:
        return Estado(0, total)
    else:
        return Estado(total - 4, 4)

def despeja2em1(estado):
    total = estado.jarro1 + estado.jarro2
    if total <= 3:
        return Estado(total, 0)
    else:
        return Estado(3, total - 3)

def busca_em_largura():
    estado_inicial = Estado(0, 0)
    fila = deque([(estado_inicial, [])])  # Tuple (estado, passo_a_passo)
    visitados = set()
    nos_abertos = []
    nos_fechados = []
    arvore_busca = {estado_inicial: []}

    while fila:
        estado_atual, passo_a_passo_atual = fila.popleft()
        nos_abertos.append(estado_atual)
        visitados.add(estado_atual)

        if estado_final(estado_atual):
            return estado_atual, passo_a_passo_atual, nos_abertos, nos_fechados, arvore_busca

        acoes = [enche1, enche2, esvazia1, esvazia2, despeja1em2, despeja2em1]
        for acao in acoes:
            novo_estado = acao(estado_atual)
            if novo_estado not in visitados:
                fila.append((novo_estado, passo_a_passo_atual + [novo_estado]))
                arvore_busca.setdefault(novo_estado, [])
                arvore_busca[estado_atual].append(novo_estado)
            else:
                nos_fechados.append(novo_estado)

    return None, None, nos_abertos, nos_fechados, arvore_busca

# Executando a busca em largura e imprimindo o caminho encontrado
estado_meta, passo_a_passo, nos_abertos, nos_fechados, arvore_busca = busca_em_largura()
if estado_meta:
    print("Caminho encontrado:")
    print("Passo a passo:")
    for passo in passo_a_passo:
        print("Jarro 1: {}, Jarro 2: {}".format(passo.jarro1, passo.jarro2))
else:
    print("Não foi possível encontrar uma solução.")

print("\nNós Abertos:")
for no in nos_abertos:
    print("Jarro 1: {}, Jarro 2: {}".format(no.jarro1, no.jarro2))

print("\nNós Fechados:")
for no in nos_fechados:
    print("Jarro 1: {}, Jarro 2: {}".format(no.jarro1, no.jarro2))


print("\nÁrvore de Busca:")
for no, filhos in arvore_busca.items():
    print("Pai: Jarro 1: {}, Jarro 2: {}".format(no.jarro1, no.jarro2))
    print("Filhos:")
    for filho in filhos:
        print("Jarro 1: {}, Jarro 2: {}".format(filho.jarro1, filho.jarro2))
    print("\n")

