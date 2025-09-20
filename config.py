import os

class Config: 
  SECRET_KEY = 'dev'  # ¡Cambiar en production!
    SQLALCHEMY_DATABASE_URI = "postgresql://tester:12345@localhost:5432/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
