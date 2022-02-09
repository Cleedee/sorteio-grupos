from flask import Blueprint, render_template

import sorteio_sula2022 as sorteio

bp = Blueprint('sula', __name__, url_prefix='/sula')


@bp.get('/')
def index():
    return render_template(
        'sula/index.html',
        titulo='Sul-americana 2022',
        pote1=sorteio.pote1,
        pote2=sorteio.pote2,
        pote3=sorteio.pote3,
        pote4=sorteio.pote4
    )
