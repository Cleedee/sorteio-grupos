from flask import Blueprint, render_template

import sorteio_sula2022 as sorteio
import base

bp = Blueprint('sula', __name__, url_prefix='/sula')


@bp.get('/')
def index():
    classificaveis = sorteio.preclassificados.copy()
    fase_de_grupo = sorteio.classificados + sorteio.preclassificados[0:16]
    fase_de_grupo.sort(key=base.pegar_ranking)
    perdedores = [
        base.Time("Perdedor do G1", "preliberta.jpg", "999", True),
        base.Time("Perdedor do G2", "preliberta.jpg", "999", True),
        base.Time("Perdedor do G3", "preliberta.jpg", "999", True),
        base.Time("Perdedor do G4", "preliberta.jpg", "999", True),
    ]
    pote1 = fase_de_grupo[0:8]
    pote2 = fase_de_grupo[8:16]
    pote3 = fase_de_grupo[16:24]
    pote4 = perdedores + fase_de_grupo[24:]
    return render_template(
        'sula/index.html',
        titulo='Copa Sul-Americana 2022',
        pote1=pote1,
        pote2=pote2,
        pote3=pote3,
        pote4=pote4
    )
