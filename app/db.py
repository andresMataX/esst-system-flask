import mysql.connector
# click es para poder usar un comando en consola
import click
# Variable g que es global
from flask import current_app, g
from flask.cli import with_appcontext
# Instrucciones para crear la base de datos
# TODO: crear achivo schema para las instrucciones de creación de base de datos


def get_db():  # Función que nos devuelve la base de datos
    # Revisamos si hay una conexión de BD en g
    if 'db' not in g:
        # Asignamos la base de datos a g
        g.db = mysql.connector.connect(
            # Uso de variables de entorno para la conexión a la base de datos
            database=current_app.config['DATABASE'],
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD']
        )
        # Obtención del cursor de la base de datos
        g.c = g.db.cursor(dictionary=True)
    # Retornamos la base de datos y su cursor
    return g.db, g.c
