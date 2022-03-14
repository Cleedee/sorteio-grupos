from dataclasses import dataclass
import random
import string
from typing import List
from itertools import cycle

LETRAS_8_GRUPOS = string.ascii_uppercase[:8]


@dataclass
class Time:
    nome: str
    imagem: str
    pais: str
    preliminar: bool = False
    ranking: int = 99999

    def __eq__(self, __o: object) -> bool:
        return self.nome == __o.nome

    def __hash__(self) -> int:
        return hash(self.nome)


def procurar_time(chave: str, times: list[Time]):
    for time in times:
        if time.imagem == chave:
            return time
    return None


def trazer_escolha(chave, times, padrao):
    if chave == 'aleatorio':
        return random.choice(times)
    elif chave == 'indeterminado':
        return padrao
    else:
        return procurar_time(chave, times)

def pegar_ranking(time):
    return time.ranking

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
    for letra in LETRAS_8_GRUPOS:
        time = pote_misturado.pop()
        if foi_sorteado(time, sorteados):
            pote_misturado.insert(0, time)
        if not mesma_nacionalidade(time.pais, grupos[letra]) and \
                len(grupos[letra]) < quantidade:
            grupos[letra].append(time)
            sorteados.append(time)
            continue
        elif mesma_nacionalidade(time.pais, grupos[letra]) and \
                time.preliminar and len(grupos[letra]) < quantidade:
            grupos[letra].append(time)
            sorteados.append(time)
            continue
        else:
            # jogar noutro grupo
            grupos_ciclados = cycle(LETRAS_8_GRUPOS)
            while next(grupos_ciclados) != letra:
                pass
            for nome_grupo in grupos_ciclados:
                if nome_grupo == letra:
                    break
                if not mesma_nacionalidade(time.pais, grupos[nome_grupo]) and \
                        len(grupos[nome_grupo]) < quantidade:
                    grupos[nome_grupo].append(time)
                    sorteados.append(time)
                    break


def eh_valido(grupos: dict):
    return not any([len(x) != 4 for x in grupos.values()])

def sortear(classificados: List[Time], pote1, pote2, pote3, pote4):
    grupos = {}

    for i in range(len(LETRAS_8_GRUPOS)):
        grupos[LETRAS_8_GRUPOS[i]] = []

    pote1_misturado = pote1[:]

    # coloca o campeão no grupo A
    grupos['A'].append(pote1_misturado[0])
    # retira o campeão do sorteio dos cabeças-de-chave
    pote1_misturado.pop(0)
    random.shuffle(pote1_misturado)
    for letra in LETRAS_8_GRUPOS[1:8]:
        time = pote1_misturado.pop()
        grupos[letra].append(time)

    sorteados = pote1[:]

    # pote 2
    sorteio_pote(grupos, pote2, sorteados, 2)
    # pote 3
    sorteio_pote(grupos, pote3, sorteados, 3)
    # pote 4
    sorteio_pote(grupos, pote4 + classificados, sorteados, 4)

    return grupos


def mostrar_grupos(grupos):
    for letra in LETRAS_8_GRUPOS:
        print('Grupo', letra)
        for time in grupos[letra]:
            print(time.nome, time.pais)
