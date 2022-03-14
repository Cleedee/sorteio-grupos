from flask import Blueprint, render_template

import sorteio_sula2022 as sorteio
import base

bp = Blueprint('sula', __name__, url_prefix='/sula')


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

