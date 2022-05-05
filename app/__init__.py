# Importación de Flask
from flask import Flask
from flask_cors import CORS


def create_app():
    # Instancia de Flask
    app = Flask(__name__)

    CORS(app)

    # Función de prueba
    @app.route('/hola')
    def hola():
        return {
            "Hola": 1452,
            "Pepe": "Cómo te va?"
        }

    # Retornamos la app
    return app
