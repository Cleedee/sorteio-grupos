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
    brasil.cuiaba_mt, brasil.coritiba,
    brasil.csa, brasil.vilanova, brasil.remo, brasil.juazeirense_ba, brasil.tombense_mg , 
    brasil.brasiliense,
    brasil.altos_pi,  brasil.portuguesa_rj, brasil.ceilandia_df, brasil.tocantinopolis,
    brasil.azuriz_pr

]

bp = Blueprint('cdb', __name__, url_prefix='/cdb')

@bp.get('/')
def index():
    return render_template('cdb/index.html', pote_a=pote_a, pote_b=pote_b)