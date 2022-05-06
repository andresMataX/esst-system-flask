from os import error
from flask import (
    Blueprint, g, redirect, request, url_for, abort, session
)
# Abortar acciones de un usuario que no le correspondan
from werkzeug.exceptions import abort
# Proteger los endpoints de usuarios que no hayan ingresado a la sesión
from app.auth import login_required
# Importamos la base de datos
from app.db import get_db
