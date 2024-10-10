import mysql.connector
from models.proyecto import proyecto
from config.database import db_config  

class proyecto_controller:
    def __init__(self):
        self.db_config = db_config
    
    def conectar(self):
        return mysql.connector.connect(**self.db_config)
    
    def crear_proyecto(self, proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO Proyecto (nombre_proyecto, descripcion_proyecto, fecha_inicio_proyecto) VALUES (%s, %s, %s)"
        cursor.execute(query, (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha_inicio()))
        connection.commit()
        cursor.close()
        connection.close()
    
    def buscar_proyecto_por_id(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Proyecto WHERE proyecto_id = %s"
        cursor.execute(query, (id,))
        proyecto = cursor.fetchone()
        cursor.close()
        connection.close()
        return proyecto
    
    def edicion_proyecto(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Proyecto SET nombre_proyecto = %s, descripcion_proyecto = %s, fecha_inicio_proyecto = %s WHERE proyecto_id = %s"
        cursor.execute(query, (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha_inicio(), proyecto.get_id()))
        connection.commit()
        cursor.close()
        connection.close()
    
    def eliminar_proyecto(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM Proyecto WHERE proyecto_id = %s"
        cursor.execute(query, (id))
        connection.commit()
        cursor.close()
        connection.close()