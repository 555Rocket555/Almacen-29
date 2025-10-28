from flask import Blueprint

# 'admin' es el nombre para url_for()
bp = Blueprint('admin', __name__) 

from app.admin import routes