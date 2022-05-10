from flask import (
    Blueprint, g, redirect, request, url_for
)
# Abortar acciones de un usuario que no le correspondan
from werkzeug.exceptions import abort
# Importamos la base de datos
from app.db import get_db

# Creamos el blueprint de inventory
bp = Blueprint('esst', __name__)


@bp.route('/create/venta', methods=['GET', 'POST'])
# El usuario debe haber iniciado sesión
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
            c.execute(
                'INSERT INTO Venta(name_cli, l_name_cli, id_cut_type) VALUES (%s, %s, %s);',
                (name_cli, l_name_cli, id_cut_type)
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
