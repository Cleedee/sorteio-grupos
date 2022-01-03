from dataclasses import dataclass
import string
import random
from copy import copy
from itertools import cycle, dropwhile
from operator import attrgetter

@dataclass
class Time:
    nome: str
    pais: str
    preliminar: bool = False

    def __eq__(self, __o: object) -> bool:
        return self.nome == __o.nome

    def __hash__(self) -> int:
        return hash(self.nome)

def mesma_nacionalidade(pais, grupo):
    for time in grupo:
        if time.pais == pais:
            return True
    return False

def foi_sorteado(time, sorteados):
    return True if time in sorteados else False

def sorteio_pote(grupos, pote, sorteados, quantidade):
    pote_misturado = pote[:]
    random.shuffle(pote_misturado)
    for letra in letras:
        time = pote_misturado.pop()
        print('Coloca', time.nome, 'no grupo',letra,'?')
        if foi_sorteado(time, sorteados):
            pote_misturado.insert(0, time)
        if not mesma_nacionalidade(time.pais, grupos[letra]) and len(grupos[letra]) < quantidade:
            print('Sim')
            grupos[letra].append(time)
            sorteados.append(time)
            continue
        elif mesma_nacionalidade(time.pais, grupos[letra]) and time.preliminar and len(grupos[letra]) < quantidade:
            print(time.nome,'será colocado em grupo de mesma nacionalidade por ter vindo de fases preliminares')
            grupos[letra].append(time)
            sorteados.append(time)
            continue
        else:
            print('Não')
            # jogar noutro grupo
            grupos_ciclados = cycle(letras)
            while next(grupos_ciclados) != letra:
                pass
            possiveis = []
            for nome_grupo in grupos_ciclados:
                if nome_grupo == letra:
                    break
                print('Olhando o grupo', nome_grupo)
                if not mesma_nacionalidade(time.pais, grupos[nome_grupo]) and len(grupos[nome_grupo]) < quantidade:
                    print('Colocando no grupo')
                    grupos[nome_grupo].append(time)
                    sorteados.append(time)
                    break

def eh_valido(grupos: dict):
    return not any([len(x) != 4 for x in grupos.values() ])

pote1 = [
    Time("Palmeiras", "BRA"),
    Time("River Plate", "ARG"),
    Time("Boca Jrs", "ARG"),
    Time("Flamengo", "BRA"),
    Time("Nacional", "URU"),
    Time("Peñarol", "URU"),
    Time("Athlético", "BRA"),
    Time("Atlético-MG", "BRA")
]

pote2 = [
    Time("Cerro Porteño", "PAR"),
    Time("Libertad", "PAR"),
    Time("Ind. Del Valle", "EQU"),
    Time("Univ. Católica", "CHI"),
    Time("Emelec", "EQU"),
    Time("Corinthians", "BRA"),
    Time("Colo-Colo", "CHI"),
    Time("Velez Sarsfield", "ARG")
]

pote3 = [
    Time("Sporting Cristal", "PER"),
    Time("RB Bragantino", "BRA"),
    Time("Tachira", "VEN"),
    Time("Alianza Lima", "PER"),
    Time("Tolima", "COL"),
    Time("Colon", "ARG"),
    Time("Caracas", "VEN"),
    Time("Dep. Cali", "COL")
]

pote4 = [
    Time("Always Ready", "BOL"),
    Time("Talleres", "ARG"),
    Time("Ind. Petrolero", "BOL"),
    Time("Fortaleza", "BRA"),
    Time("Vencedor do G1", "XXX", True),
    Time("Vencedor do G2", "XXX", True),
    Time("Vencedor do G3", "XXX", True),
    Time("Vencedor do G4", "XXX", True)
]

participantes = set(pote1 + pote2 + pote3 + pote4)

letras = string.ascii_uppercase[:8]

def sortear():
    grupos = {}

    for i in range(len(letras)):
        grupos[letras[i]] = []

    pote1_misturado = pote1[:]

    # coloca o campeão no grupo A
    grupos['A'].append(pote1_misturado[0])
    # retira o campeão do sorteio dos cabeças-de-chave
    pote1_misturado.pop(0)
    random.shuffle(pote1_misturado)
    for letra in letras[1:8]:
        time = pote1_misturado.pop()
        grupos[letra].append(time)
        #print('Grupo', letra, ': ', time.nome)

    sorteados = pote1[:]

    # pote 2
    print('POTE 2')
    sorteio_pote(grupos, pote2, sorteados, 2)

    # pote 3
    print('POTE 3')
    sorteio_pote(grupos, pote3, sorteados, 3)
    # pote 4
    print('POTE 4')
    sorteio_pote(grupos, pote4, sorteados, 4)

    print('Grupo A', len(grupos['A']))
    print('Grupo B', len(grupos['B']))
    print('Grupo C', len(grupos['C']))
    print('Grupo D', len(grupos['D']))
    print('Grupo E', len(grupos['E']))    
    print('Grupo F', len(grupos['F']))
    print('Grupo G', len(grupos['G']))
    print('Grupo H', len(grupos['H']))
    return grupos

def mostrar_grupos(grupos):
    for letra in letras:
        print('Grupo', letra)
        for time in grupos[letra]:
            print(time.nome, time.pais)
