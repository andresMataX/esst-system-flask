import functools
from logging import error
from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)
from werkzeug.security import check_password_hash, generate_password_hash
# Interactuamos con la base de datos
from app.db import get_db
