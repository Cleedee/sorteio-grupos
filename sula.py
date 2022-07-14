from random import shuffle
from collections import namedtuple

from flask import Blueprint, render_template

import sorteio_sula2022 as sorteio
import base
from paises import brasil, argentina, venezuela
from paises import uruguai, equador, peru

bp = Blueprint('sula', __name__, url_prefix='/sula')

quartas = [
    brasil.saopaulo, brasil.ceara, brasil.inter, brasil.atlego,
    venezuela.tachira, uruguai.naciouru, equador.delvalle,
    peru.melgar
]

@bp.get('/')
def index():
    pote1, pote2, pote3, pote4 = sorteio.traga_potes()
    return render_template(
        'sula/index.html',
        titulo='Copa Sul-Americana 2022',
        pote1=pote1,
        pote2=pote2,
        pote3=pote3,
        pote4=pote4
    )

@bp.get('/sorteio')
def sortear():
    pote1, pote2, pote3, pote4 = sorteio.traga_potes()
    sorteios = []
    while True:
        s = base.sortear([], pote1, pote2, 
            pote3, pote4, campeao_no_a=False, ver_nacionalidade_preliminares=True)
        if base.eh_valido(s):
            sorteios.append(s)
            print('Válido')
        else:
            print('Inválido')
        if len(sorteios) == 3:
            break
    return render_template('sula/sorteio.html', sorteios=sorteios,
                           titulo='Copa Sul-Americana 2022')

@bp.get('/sorteio-quartas')
def sorteio_quartas():
    shuffle(quartas)
    mandantes = quartas[:4]
    visitantes = quartas[4:]

    Partida = namedtuple('Partida','mandante visitante')
    partidas = []
    for indice in range(4):
        partidas.append(Partida(mandantes[indice], visitantes[indice]))
    coluna1 = partidas[:2]
    coluna2 = partidas[2:]
    return render_template('sula/sorteio-mata-mata.html', coluna1=coluna1, coluna2=coluna2,
        partidas_coluna=2)
