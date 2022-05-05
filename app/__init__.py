# Acceder a las variables de entorno
import os
# Importación de Flask
from flask import Flask
# Solucionar problema de CORS al llamar al backend desde frontend de otro hosting
from flask_cors import CORS
# TODO: Agregar archivo de base de datos


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
