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


@bp.route('/create/coste', methods=['GET', 'POST'])
def create_coste():
    # Revisar si usamos el método de POST
    if request.method == 'POST':
        # Sacamos la descripción desde el formulario
        name_cost = request.json['name_cost']
        id_pro_type = request.json['id_pro_type']
        error = None
        # Preguntaremos si no existe una descripción
        if not name_cost:
            error = 'El nombre del producto es requerido.'
        if not id_pro_type:
            error = 'El tipo del producto es requerido.'
        # Preguntamos si tenemos un mensaje de erro
        if error is not None:
            return {
                "error": error
            }
        else:
            db, c = get_db()
            price = get_price_producto(id_pro_type)
            c.execute(
                'INSERT INTO Transaccion(tran_price, tran_type) VALUES (%s, %s);',
                (price['prod_price'], 1)
            )
            db.commit()
            c.execute(
                'INSERT INTO Coste(name_cost, id_pro_type, id_tran) VALUES (%s, %s, %s);',
                (name_cost, id_pro_type, get_transaction())
            )
            # Comprometemos la base de datos
            db.commit()
            # Redirigimos al usuario al listado de ToDos
            return {
                "estatus": "ok",
                "retro": "El producto ha sido registrado exitosamente"
            }
    return {
        "ruta": "/create/coste"
    }


@bp.route('/read/clientes', methods=['GET', 'POST'])
def read_clientes():
    if request.method == 'POST':
        date = request.json['date']
        day = request.json['day']
        month = request.json['month']
        year = request.json['year']
        db, c = get_db()
        if len(date) != 0:
            c.execute(
                'SELECT v.id, v.name_cli, v.l_name_cli, v.id_cut_type, v.date, c.cut_name FROM Venta v '
                'JOIN Corte c ON v.id_cut_type = c.id WHERE v.date LIKE %s ORDER BY v.date desc;',
                ("%"+date+"%",)
            )
            filtro_date = c.fetchall()
            return {
                "filtro": filtro_date
            }
        if len(day) != 0:
            c.execute(
                'SELECT v.id, v.name_cli, v.l_name_cli, v.id_cut_type, v.date, c.cut_name FROM Venta v JOIN Corte c ON v.id_cut_type = c.id WHERE v.date LIKE %s ORDER BY v.date desc;',
                ("%"+"-"+day+" "+"%",)
            )
            filtro_day = c.fetchall()
            return {
                "filtro": filtro_day
            }
        if len(month) != 0:
            c.execute(
                'SELECT v.id, v.name_cli, v.l_name_cli, v.id_cut_type, v.date, c.cut_name FROM Venta v '
                'JOIN Corte c ON v.id_cut_type = c.id WHERE v.date LIKE %s ORDER BY v.date desc;',
                ("%"+"-"+month+"-"+"%",)
            )
            filtro_month = c.fetchall()
            return {
                "filtro": filtro_month
            }
        if len(year) != 0:
            c.execute(
                'SELECT v.id, v.name_cli, v.l_name_cli, v.id_cut_type, v.date, c.cut_name FROM Venta v '
                'JOIN Corte c ON v.id_cut_type = c.id WHERE v.date LIKE %s ORDER BY v.date desc;',
                ("%"+year+"-"+"%",)
            )
            filtro_year = c.fetchall()
            return {
                "filtro": filtro_year
            }

    # Si el cliente no manda nada en el buscador
    db, c = get_db()
    c.execute(
        'SELECT v.id, v.name_cli, v.l_name_cli, v.id_cut_type, v.date, c.cut_name FROM Venta v '
        'JOIN Corte c ON v.id_cut_type = c.id ORDER BY v.date desc'
    )
    clientes = c.fetchall()
    '''
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
    '''
    return {
        "clientes": 'pepe'
    }


@bp.route('/read/costes')
def read_costes():
    db, c = get_db()
    c.execute(
        'SELECT c.id, c.name_cost, c.id_pro_type, c.date, p.prod_name FROM Coste c '
        'JOIN Producto p ON c.id_pro_type = p.id ORDER BY c.date desc'
    )
    costes = c.fetchall()
    return {
        "costes": costes
    }


@bp.route('/read/cortes')
def read_cortes():
    db, c = get_db()
    c.execute(
        'SELECT * FROM Corte;'
    )
    cortes = c.fetchall()
    return {
        "cortes": cortes
    }


@bp.route('/read/productos')
def read_productos():
    db, c = get_db()
    c.execute(
        'SELECT * FROM Producto;'
    )
    producto = c.fetchall()
    return {
        "producto": producto
    }


@bp.route('/read/transacciones')
def read_transacciones():
    db, c = get_db()
    c.execute(
        'SELECT * FROM Transaccion;'
    )
    transacciones = c.fetchall()
    return {
        "transacciones": transacciones
    }


def get_price_corte(id):
    db, c = get_db()
    c.execute(
        'SELECT cut_price FROM Corte WHERE id = %s',
        (id,)
    )
    price = c.fetchone()
    return price


def get_price_producto(id):
    db, c = get_db()
    c.execute(
        'SELECT prod_price FROM Producto WHERE id = %s',
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
