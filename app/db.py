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


def close_db(e=None):  # Función que cierra la conexión de base de datos con un evento None
    # Sacamos el atributo de la base de datos de g
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():  # Función que ejecuta todas las instrucciones del archivo schema.py
    # Obtenemos la base de datos
    db, c = get_db()
    # Iteramos las instrucciones
    # TODO: Habilitar ciclo For con instrucciones y execute
    # for i in instructions:
    # Ejecutamos las sentencias SQL
    # c.execute(i)
    # Comprometemos las instrucciones para que se ejecuten en la base de datos
    db.commit()


@click.command('init-db')
# Habilitamos que el script pueda usar las variables de entorno
@with_appcontext
def init_db_command():  # Función que inicializa la base de datos desde consola
    # Llamada a función de sentencias SQL
    init_db()
    # Mostramos un mensaje de funcionamiento
    click.echo("Base de datos inicializada")
