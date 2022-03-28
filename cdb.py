from random import shuffle
from collections import namedtuple

from flask import Blueprint, render_template

import base
from paises import brasil

pote_a = [
    brasil.fla, brasil.palmeiras, brasil.atletico, brasil.atlpr, brasil.santos,
    brasil.saopaulo, brasil.fluminense, brasil.corinthians, brasil.fortaleza,
    brasil.bahia, brasil.ceara, brasil.cruzeiro, brasil.ammg, brasil.atlego,
    brasil.botafogo, brasil.bragantino,
]

pote_b = [
    brasil.cuiaba_mt,  brasil.goias, brasil.juventude, brasil.vitoria,
    brasil.coritiba, brasil.csa, brasil.vilanova, brasil.remo,
    brasil.tombense_mg, brasil.juazeirense_ba, brasil.brasiliense,
    brasil.altos_pi, brasil.portuguesa_rj, brasil.tocantinopolis,
    brasil.ceilandia_df, brasil.azuriz_pr

]

bp = Blueprint('cdb', __name__, url_prefix='/cdb')

@bp.get('/')
def index():
    return render_template('cdb/index.html', pote_a=pote_a, pote_b=pote_b)

@bp.get('/sorteio')
def sorteio():
    shuffle(pote_a)
    shuffle(pote_b)
    Partida = namedtuple('Partida','mandante visitante')
    partidas = []
    for indice in range(16):
        partidas.append(Partida(pote_a[indice], pote_b[indice]))
    coluna1 = partidas[:8]
    coluna2 = partidas[8:]
    return render_template('cdb/sorteio.html', coluna1=coluna1, coluna2=coluna2)
