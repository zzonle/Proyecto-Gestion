class proyecto:
    def __init__(self, proyecto_id = None , nombre_proyecto = "", descripcion = "", fecha_inicio = None, empleados = []):
        self.proyecto_id = proyecto_id
        self.nombre_proyecto = nombre_proyecto
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self._empleados = empleados
        
        
    #getters
    
    def get_id(self):
        return self._id
    
    def get_nombre(self):
        return self._nombre
    
    def get_description(self):
        return self._descripcion
    
    def get_fecha_inicio(self):
        return self._fecha_inicio
    
    def get_empleados(self):
        return self._empleados    
    #setters
    
    def set_id(self, id):
        self._id = id
        
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
    
    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio
        
    def set_empleados(self, empleados):
        self._empleados = empleados
        
