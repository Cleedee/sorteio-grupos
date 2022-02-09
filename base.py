from dataclasses import dataclass
import random
import string

LETRAS_8_GRUPOS = string.ascii_uppercase[:8]


@dataclass
class Time:
    nome: str
    imagem: str
    pais: str
    preliminar: bool = False

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
