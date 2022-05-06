import functools
from logging import error
from flask import (
    Blueprint, g, request, url_for, session, redirect
)
from werkzeug.security import check_password_hash, generate_password_hash
# Interactuamos con la base de datos
from app.db import get_db

# Creamos el blueprint de autenticación
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
# Ruta para que un usuario se inicie sesión
def login():
    # Verificamos el método enviado
    if request.method == 'POST':
        # Recuperamos el usuario enviado desde el formulario
        username = request.form['user']
        # Recuperamos la contraseña enviada desde el formulario
        password = request.form['pass']
        # Instancia de base de datos
        db, c = get_db()
        # Variable que guarda los mensajes de error
        error = None
        # Buscamos al usuario y contraseña
        c.execute(
            'SELECT * FROM usuario WHERE user = %s', (username,)
        )
        # Obtenemos el primer y único resultado obtenido
        user = c.fetchone()

        # Verificamos que el usuario exista
        if user is None:
            # Mensaje de error que no determina cuál campo es el incorrecto
            error = 'Usuario y/o Contraseña inválida'
        # Verificamos que la contraseña sea la correcta
        # TODO: Crear la función que registre por URL
        # elif not check_password_hash(user['pass'], password):
        #     # Mensaje de error que no determina cuál campo es el incorrecto
        #     error = 'Usuario y/o Contraseña inválida'

        # Verificamos que no hayamos tenido algún error
        if error is None:
            # Limpiamos una sesión, le asignamos un ID a la sesión y lo redirigimos a la página principal
            session.clear()
            # Creamos una variable en la sesión con el ID que tiene el usuario en la base de datos
            session['user_id'] = user['id']
            return {
                "error": "false"
            }
        else:
            return {
                "error": error
            }
    return {
        "pepe": "uwu"
    }


# Función decoradora para asignar la sesión del usuario ya loggeado a g
@bp.before_app_request
def load_logged_in_user():
    # Obtenemos el user_id que guardamos al iniciar la sesión del usuario
    user_id = session.get('user_id')
    if user_id is None:
        # Debemos asignarle None, ya que no tenemos un usuario que haya iniciado sesión
        g.user = None
    else:
        # Buscamos el usuario por su ID en la base de datos y se lo asignamos a g.user
        db, c = get_db()
        c.execute(
            'SELECT * FROM usuario WHERE id = %s', (user_id,)
        )
        # Retornamos el primer y único elemento encontrado
        g.user = c.fetchone()


def login_required(view):
    # Función que protege las rutas recibiendo un inicio de sesión que ya está siendo decorada con esta función decoradora
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        # Verificamos que el usuario haya iniciado sesión
        if g.user is None:
            return redirect(url_for('auth.login'))
        # Devolvemos la vista envuelta
        return view(**kwargs)
    return wrapped_view


@bp.route('/logout')
# Función de cierre de sesión de un usuario
def logout():
    # Limpiamos la sesión del usuario
    session.clear()
    # Redirigimos al usuario a la pantalla de inicio de sesión
    return redirect(url_for('auth.login'))
