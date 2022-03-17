from flask import Blueprint
from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from base import Time, trazer_escolha, eh_valido
import base
import sorteio

bp = Blueprint('liberta', __name__, url_prefix='/libertadores')

escolhas_padrao = [('aleatorio', 'Escolha por mim'),
                   ('indeterminado', 'Deixe indeterminado')]
times_g1 = [(time.imagem, time.nome)
            for time in sorteio.grupo1]
times_g2 = [(time.imagem, time.nome)
            for time in sorteio.grupo2]
times_g3 = escolhas_padrao + [(time.imagem, time.nome)
                              for time in sorteio.grupo3]
times_g4 = [(time.imagem, time.nome)
            for time in sorteio.grupo4]


class PreLibertaForm(FlaskForm):
    # TODO lista de times
    g1 = SelectField('Vencedor do G1', choices=times_g1)
    g2 = SelectField('Vencedor do G2', choices=times_g2)
    g3 = SelectField('Vencedor do G3', choices=times_g3)
    g4 = SelectField('Vencedor do G4', choices=times_g4)
    submit = SubmitField('Continuar', render_kw={'class': 'button is-success'})


@bp.get('/')
def index():
    form = PreLibertaForm()
    return render_template('liberta/index.html', form=form,
                           titulo='Copa Libertadores 2022')


@bp.post('/')
def sortear():
    form = PreLibertaForm()
    classificados = []
    classificados += [
        trazer_escolha(
            form.g1.data, sorteio.grupo1,
            Time("Vencedor do G1", "preliberta.jpg", "XXX", True))
        ]
    classificados += [
        trazer_escolha(
            form.g2.data, sorteio.grupo2,
            Time("Vencedor do G2", "preliberta.jpg", "XXX", True))
        ]
    classificados += [
        trazer_escolha(
            form.g3.data, sorteio.grupo3,
            Time("Vencedor do G3", "preliberta.jpg", "XXX", True))
        ]
    classificados += [
        trazer_escolha(
            form.g4.data, sorteio.grupo4,
            Time("Vencedor do G4", "preliberta.jpg", "XXX", True))
        ]
    sorteios = []
    while True:
        s = base.sortear(classificados, sorteio.pote1, sorteio.pote2, 
            sorteio.pote3, sorteio.pote4)
        if eh_valido(s):
            sorteios.append(s)
            print('Válido')
        else:
            print('Inválido')
        if len(sorteios) == 3:
            break
    return render_template('liberta/sorteio.html', sorteios=sorteios,
                           titulo='Copa Libertadores 2022')
