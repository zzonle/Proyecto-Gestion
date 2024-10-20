#proyecto_controller.py
import mysql.connector
from models.proyecto import Proyecto
from config.database import db_config  

class ProyectoController:
    def __init__(self):
        self.db_config = db_config
    
    def conectar(self):
        return mysql.connector.connect(**self.db_config)
    
    def crear_proyecto(self, Proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO proyecto (nombre_proyecto, descripcion_proyecto, fecha_inicio_proyecto) values (%s, %s, %s)"
        cursor.execute(query, (Proyecto.get_nombre(), Proyecto.get_descripcion(), Proyecto.get_fecha_inicio()))
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
    
    def modificar_proyecto(self, Proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Proyecto SET nombre_proyecto = %s, descripcion_proyecto = %s fecha_inicio_proyecto = %s, WHERE proyecto_id = %s"
        cursor.execute(query, (Proyecto.get_nombre(), Proyecto.get_descripcion(), Proyecto.get_fecha_inicio() , Proyecto.get_id()))
        connection.commit()
        cursor.close()
        connection.close()
    
    def eliminar_proyecto(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM Proyecto WHERE proyecto_id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()    
    
    def agregar_empleado_proyecto(self, proyecto_id, empleado_id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO empleados_proyecto (proyecto_id, empleado_id) VALUES (%s, %s)"
        cursor.execute(query, (proyecto_id, empleado_id))
        connection.commit()
        cursor.close()
        connection.close()
        
    def eliminar_empleado_proyecto(self, proyecto_id, empleado_id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM empleados_proyecto WHERE proyecto_id = %s AND empleado_id = %s"
        cursor.execute(query, (proyecto_id, empleado_id))
        connection.commit()
        cursor.close()
        connection.close()
        
    def listar_empleados_proyecto(self, proyecto_id):
        
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT E.nombre, P.nombre_proyecto, P.proyecto_id FROM empleado E INNER JOIN empleados_proyecto PxE ON E.id = PxE.empleado_id INNER JOIN proyecto P ON PxE.proyecto_id = P.proyecto_id WHERE P.proyecto_id = %s;"
        cursor.execute(query, (proyecto_id))
        empleados = cursor.fetchall()
        cursor.close()
        connection.close()
        return empleados