from flask import (
    Blueprint, g, redirect, request, url_for
)
# Abortar acciones de un usuario que no le correspondan
from werkzeug.exceptions import abort
# Importamos la base de datos
from app.db import get_db
from datetime import datetime

# Creamos el blueprint de inventory
bp = Blueprint('esst', __name__)


@bp.route('/create/venta', methods=['GET', 'POST'])
def create_cliente():
    # Revisar si usamos el método de POST
    if request.method == 'POST':
        # Sacamos la descripción desde el formulario
        name_cli = request.json['name_cli']
        l_name_cli = request.json['l_name_cli']
        id_cut_type = request.json['id_cut_type']
        error = None
        # Preguntaremos si no existe una descripción
        if not name_cli:
            error = 'El nombre del cliente es requerido.'
        if not l_name_cli:
            error = 'El apellido del cliente es requerido.'
        if not id_cut_type:
            error = 'El tipo de corte es requerido.'
        # Preguntamos si tenemos un mensaje de erro
        if error is not None:
            return {
                "error": error
            }
        else:
            # Podemos crear nuestro ToDo
            db, c = get_db()
            price = get_price_corte(id_cut_type)
            c.execute(
                'INSERT INTO Transaccion(tran_price, tran_type) VALUES (%s, %s);',
                (price['cut_price'], 0)
            )
            db.commit()
            c.execute(
                'INSERT INTO Venta(name_cli, l_name_cli, id_cut_type, id_tran) VALUES (%s, %s, %s, %s);',
                (name_cli, l_name_cli, id_cut_type, get_transaction())
            )
            # Comprometemos la base de datos
            db.commit()
            # Redirigimos al usuario al listado de ToDos
            return {
                "estatus": "ok",
                "retro": "El cliente ha sido registrado exitosamente"
            }
    return {
        "ruta": "/create/venta"
    }


@bp.route('/read/clientes')
def read_clientes():
    db, c = get_db()
    c.execute(
        'SELECT v.id, v.name_cli, v.l_name_cli, v.id_cut_type, v.id_tran, v.date, c.cut_name FROM Venta v '
        'JOIN Corte c ON v.id_cut_type = c.id ORDER BY v.date'
    )
    clientes = c.fetchall()
    # print(clientes[0]['date'].strftime('%d-%m-%Y %I:%M%p'))
    # "id": fetch[0]['id'],
    # "name_cli": fetch[0]['name_cli'],
    # "l_name_cli": fetch[0]['l_name_cli'],
    # "cut_name": fetch[0]['cut_name'],
    # "id_tran": fetch[0]['id_tran'],
    # "date": fetch[0]['date'].strftime('%I:%M%p %d-%m-%Y')
    # "year": clientes[0]['date'].strftime('%Y'),
    # "month": clientes[0]['date'].strftime('%m'),
    # "day": clientes[0]['date'].strftime('%d'),
    # "hour": clientes[0]['date'].strftime('%I%p'),
    # "minute": clientes[0]['date'].strftime('%M')
    return {
        "clientes": clientes
    }


def get_price_corte(id):
    db, c = get_db()
    c.execute(
        'SELECT cut_price FROM Corte WHERE id = %s',
        (id,)
    )
    price = c.fetchone()
    return price


def get_transaction():
    db, c = get_db()
    c.execute(
        'SELECT MAX(id) AS id FROM transaccion;'
    )
    ids = c.fetchone()
    return ids['id']
