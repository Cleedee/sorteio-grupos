from flask import Blueprint, render_template

import base
from paises import brasil

pote_a = [
    brasil.fla, brasil.palmeiras, brasil.atletico, brasil.atlpr, brasil.santos,
    brasil.fluminense, brasil.corinthians, brasil.fortaleza, brasil.bahia,
    brasil.ammg, brasil.botafogo, brasil.bragantino    
]

bp = Blueprint('cdb', __name__, url_prefix='/cdb')

@bp.get('/')
def index():
    return render_template('cdb/index.html', pote_a=pote_a)