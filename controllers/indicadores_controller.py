import mysql.connector
from models.indicador import indicadores
from config.database import db_config 
import requests

api = "https://mindicador.cl/api/"

class IndicadorController():
    
    def __init__(self):
        self.db_config = db_config
    
    def conectar(self):
        return mysql.connector.connect(**self.db_config)
    
    def crear_indicador(self, indicadores):
        connection = self.conectar()
        cursor = connection.cursor()
        query = '''INSERT INTO registros (Nombre, fecha_registro, fecha_consulta, valor, usuario, sitio) VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (indicadores.get_nombre(), indicadores.get_fecha_registro(), indicadores.get_fecha_consulta(), indicadores.get_valor(), indicadores.get_usuario(), indicadores.get_sitio()))
        connection.commit()
        cursor.close()
        connection.close()        
        
    def info(self, indicadores: str):
        data: dict = requests.get(api + indicadores).json()
        print("\n")
        print("-"*30)
        print(f"Nombre: {data['nombre']}")
        print(f"Unidad de Medida: {data['unidad_medida']}")
        print(f"Fecha: {data['serie'][0]['fecha'][:10]}")
        print(f"Valor: {data['serie'][0]['valor']}")
        print("-"*30, "\n")