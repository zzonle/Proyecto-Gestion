import mysql.connector
from models.registrotiempo import RegistroTiempo
from config.database import db_config

class RegistroTiempoController:
    def __init__(self):
        self.db_config = db_config
        
    def conectar(self):
        return mysql.connector.connect(**self.db_config)
    
    
