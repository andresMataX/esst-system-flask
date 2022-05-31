from flask import (
    Blueprint, request, url_for, session, redirect
)
from werkzeug.security import check_password_hash, generate_password_hash
# Interactuamos con la base de datos
from app.db import get_db

# Creamos el blueprint de autenticación
bp = Blueprint('auth', __name__, url_prefix='/auth')


# Ruta de registro de usuario
@bp.route('/register', methods=['GET', 'POST'])
# Función que registra usuarios a la base de datos
def register():
    if request.method == 'POST':
        # Recuperamos el usuario enviado en el formulario
        username = request.json['user']
        # Recuperamos la contraseña enviada en el json
        password = request.json['pass']
        # Instancia de la base de datos
        db, c = get_db()
        # Variable que almacena los errores provocados por el usuario
        error = None
        # Validamos que el usuario no exista

        # Validamos que se haya ingresado un usuario
        if not username:
            error = 'Se requiere de un nombre de usuario para registrarse.'
        else:
            c.execute(
                # Buscamos el ID del usuario que ha sido ingresado
                'SELECT id FROM Usuario WHERE user = %s', (username,)
            )

        # Validamos que se haya ingresado una contraseña
        if not password:
            error = 'Se requiere de una contraseña para registrarse.'
        elif c.fetchone() is not None:
            # Se coloca el usuario {} con format
            error = 'El usuario {} ya se encuentra registrado'.format(username)

        # Validamos que no hayamos tenido mensajes de error
        if error is None:
            # Registramos al usuario con su contraseña
            c.execute(
                'INSERT INTO Usuario(user, pass) VALUES (%s, %s)',
                # Encriptamos la contraseña
                (username, generate_password_hash(password))
            )
            # Comprometemos la base de datos
            db.commit()
            return {
                "estatus": "ok",
                "retro": "El usuario se ha registrado correctamente"
            }
        return {
            "error": error
        }
    return {
        "ruta": "Register"
    }


@bp.route('/login', methods=['GET', 'POST'])
# Ruta para que un usuario se inicie sesión
def login():
    # Verificamos el método enviado
    if request.method == 'POST':
        # Recuperamos el usuario enviado desde el formulario
        username = request.json['user']
        # Recuperamos la contraseña enviada desde el formulario
        password = request.json['pass']
        # Instancia de base de datos
        db, c = get_db()
        # Variable que guarda los mensajes de error
        error = None
        # Buscamos al usuario y contraseña
        c.execute(
            'SELECT * FROM Usuario WHERE user = %s', (username,)
        )
        # Obtenemos el primer y único resultado obtenido
        user = c.fetchone()

        # Verificamos que el usuario exista
        if user is None:
            # Mensaje de error que no determina cuál campo es el incorrecto
            error = 'Usuario y/o Contraseña inválida'
        # Verificamos que la contraseña sea la correcta
        elif not check_password_hash(user['pass'], password):
            # Mensaje de error que no determina cuál campo es el incorrecto
            error = 'Usuario y/o Contraseña inválida'

        # Verificamos que no hayamos tenido algún error
        if error is None:
            # Limpiamos una sesión, le asignamos un ID a la sesión y lo redirigimos a la página principal
            session.clear()
            return {
                "estatus": "ok",
                "retro": "Has iniciado sesión correctamente"
            }
        return {
            "error": error
        }
    return {
        "ruta": "Login"
    }


@bp.route('/logout')
# Función de cierre de sesión de un usuario
def logout():
    # Limpiamos la sesión del usuario
    session.clear()
    # Redirigimos al usuario a la pantalla de inicio de sesión
    return redirect(url_for('auth.login'))
