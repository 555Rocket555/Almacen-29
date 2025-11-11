from flask import Blueprint

bp = Blueprint('mesero', __name__) 

from app.mesero import routes