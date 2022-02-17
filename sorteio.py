import random
from typing import List
from itertools import cycle

from base import Time, LETRAS_8_GRUPOS


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


pote1 = [
    Time("Palmeiras", "palmeiras.png", "BRA"),
    Time("River Plate", "riverc.png", "ARG"),
    Time("Boca Jrs", "bocc.png", "ARG"),
    Time("Flamengo", "fla.png", "BRA"),
    Time("Nacional", "naciouru.png", "URU"),
    Time("Peñarol", "penarol.png", "URU"),
    Time("Athlético", "atlpr.png", "BRA"),
    Time("Atlético-MG", "atletico.png", "BRA")
]

pote2 = [
    Time("Cerro Porteño", "cerropor.png", "PAR"),
    Time("Libertad", "libertad.png", "PAR"),
    Time("Ind. Del Valle", "indep_j_teran.jpg", "EQU"),
    Time("Univ. Católica", "unicatolica.png", "CHI"),
    Time("Emelec", "emelec.png", "EQU"),
    Time("Corinthians", "corinthians.png", "BRA"),
    Time("Colo-Colo", "colocolo.png", "CHI"),
    Time("Velez Sarsfield", "velez.png", "ARG")
]

pote3 = [
    Time("Sporting Cristal", "cristal.jpg", "PER"),
    Time("RB Bragantino", "bragantino.png", "BRA"),
    Time("Tachira", "tachira.png", "VEN"),
    Time("Alianza Lima", "alianza.jpg", "PER"),
    Time("Tolima", "dtolima_col.png", "COL"),
    Time("Colon", "colon.png", "ARG"),
    Time("Caracas", "caracas.png", "VEN"),
    Time("Dep. Cali", "dep_cali.png", "COL")
]

pote4 = [
    Time("Always Ready", "always_ready_bol.png", "BOL"),
    Time("Talleres", "talleres.png", "ARG"),
    Time("Ind. Petrolero", "indeppetrobol.png", "BOL"),
    Time("Fortaleza", "fortaleza.png", "BRA")
]

grupo1 = [
    Time("Milionarios", "millo.png", "COL", True),
    Time("Fluminense", "fluminense.png", "BRA", True),
    Time("Atlético Nacional", "medelin.png", "COL", True),
    Time("Universidade César Vallejo", "cesarvallejo.png", "PER", True),
    Time("Olímpia", "olimpia.png", "PAR", True)
]

grupo2 = [
    Time("Audax Italiano", "audax.gif", "CHI", True),
    Time("Estudiantes", "estudic.png", "ARG", True),
    Time("Everton", "everton_ch.gif", "CHI", True),
    Time("Monagas", "monagas_ven.png", "VEN", True)
]

grupo3 = [
    # Time("Deportivo Lara", "dep_lara_ven.gif", "VEN", True),
    # desclassificado pelo Bolivar
    Time("Bolivar", "bolivar.png", "BOL", True),
    Time("Universid Católica", "un_catolica_ecu.png", "EQU", True),
    Time("Plaza Colonia", "plazacolonia.png", "URU", True),
    Time("The Strongest", "strongest.png", "BOL", True)
]

grupo4 = [
    Time("América Mineiro", "ammg.gif", "BRA", True),
    Time("Guarani", "guarani_par.png", "URU", True),
    # Time("City Torque", "torque_uru.png", "URU", True), Perdeu para o Barcelona nos pênaltis
    Time("Universitário", "universitaria_peru.png", "PER", True),
    Time("Barcelona SC", "barcelonaeq.png", "EQU", True)
]


def sortear(classificados: List[Time]):
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
