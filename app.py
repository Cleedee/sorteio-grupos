from flask import Flask, render_template

import libertadores
import sula
import cdb


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'palavra_secreta'

    app.register_blueprint(libertadores.bp)
    app.register_blueprint(sula.bp)
    app.register_blueprint(cdb.bp)

    @app.get('/')
    def index():
        return render_template('index.html')

    return app


app = create_app()
