from flask import Flask
from flask.templating import render_template

import sorteio

app = Flask(__name__)

@app.get('/')
def index():
    sorteios = []
    while True:
        s = sorteio.sortear()
        if sorteio.eh_valido(s):
            sorteios.append(s)
        if len(sorteios) == 3:
            break
    return render_template('index.html', sorteios=sorteios)