from dataclasses import dataclass
import string
import random
from copy import copy

@dataclass
class Time:
    nome: str
    pais: str

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
    Time("Vencedor do G1", "XXX"),
    Time("Vencedor do G2", "XXX"),
    Time("Vencedor do G3", "XXX"),
    Time("Vencedor do G4", "XXX")
]

participantes = set(pote1 + pote2 + pote3 + pote4)

letras = string.ascii_uppercase[:8]

def sortear():
    grupos = {}

    for i in range(len(letras)):
        grupos[letras[i]] = []

    pote1_misturado = pote1[:]
    random.shuffle(pote1_misturado)

    for letra in letras:
        time = pote1_misturado.pop()
        grupos[letra].append(time)
        #print('Grupo', letra, ': ', time.nome)

    sorteados = pote1[:]

    # pote 2
    pote2_misturado = pote2[:]
    random.shuffle(pote2_misturado)
    for letra in letras:
        for time in pote2_misturado:
            if not mesma_nacionalidade(time.pais, grupos[letra]) and not foi_sorteado(time, sorteados):
                grupos[letra].append(time)
                sorteados.append(time)
                break

    # pote 3
    pote3_misturado = pote3[:]
    random.shuffle(pote3_misturado)
    for letra in letras:
        for time in pote3_misturado:
            if not mesma_nacionalidade(time.pais, grupos[letra]) and not foi_sorteado(time, sorteados):
                grupos[letra].append(time)
                sorteados.append(time)
                break

    # pote 4
    pote4_misturado = pote4[:]
    random.shuffle(pote4_misturado)
    for letra in letras:
        for time in pote4_misturado:
            if not mesma_nacionalidade(time.pais, grupos[letra]) and not foi_sorteado(time, sorteados):
                grupos[letra].append(time)
                sorteados.append(time)
                break

    # grupo incompleto
    sobra = participantes - set(sorteados)
    print(sobra)
    if sobra:
        sobras = list(sobra)
        for letra in letras:
            while len(grupos[letra]) < 4:
                grupos[letra].append(sobras.pop())

    return grupos

def mostrar_grupos(grupos):
    for letra in letras:
        print('Grupo', letra)
        for time in grupos[letra]:
            print(time.nome, time.pais)
