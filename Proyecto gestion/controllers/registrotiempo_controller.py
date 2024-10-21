import mysql.connector
from models.registrotiempo import RegistroTiempo
from config.database import db_config

class RegistroTiempoController:
    def __init__(self):
        self.db_config = db_config
        
    def conectar(self):
        return mysql.connector.connect(**self.db_config)
    
    def crear_registro(self, registro):
        connection = self.conectar()
        cursor = connection.cursor()
        query = ("INSERT INTO registro_tiempo (fecha, horas, descripcion, empleado_id, proyecto_id) VALUES (%s,%s,%s,%s,%s);")
        cursor.execute(query, (registro.get_fecha_inicio(), registro.get_horas_trabajadas(), registro.get_descripcion(), registro.get_empleado_id(), registro.get_proyecto_id()))
        connection.commit()
        cursor.close()
        connection.close()
    
    def listar_registro(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "select * from registro_tiempo;"
        cursor.execute(query)
        registro_tiempos = cursor.fetchall()
        cursor.close()
        connection.close()
        return registro_tiempos
    
    def buscar_registro(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM registro_tiempo WHERE id = %s"
        cursor.execute(query, (id,))
        registro = cursor.fetchone()
        cursor.close()
        connection.close()
        return registro
    
    def modificar_registro(self, registro):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE registro_tiempo set fecha = %s, hora = %s, descripcion = %s, empleado_id = %s, proyecto_id = %s where id = %s;"
        cursor.execute(query(registro.get_fecha_inicio(),registro.get_horas_trabajadas(), registro.get_descripcion(), registro.get_proyecto_id(), registro.get_empleado_id(), registro.get_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_registro(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM registro_tiempo WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        
    