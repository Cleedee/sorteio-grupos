from flask import Flask
from flask.templating import render_template

import sorteio

app = Flask(__name__)

@app.get('/')
def index():
    sorteios = [sorteio.sortear(), sorteio.sortear(), sorteio.sortear()]
    print(len(sorteios[1]['C']))
    return render_template('index.html', sorteios=sorteios)