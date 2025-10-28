from flask import Blueprint

# 'mesero' es el nombre para url_for()
bp = Blueprint('mesero', __name__) 

from app.mesero import routes