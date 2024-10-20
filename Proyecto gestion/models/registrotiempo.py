class RegistroTiempo:
    def __init__(self, id = None, fecha_inicio = "", horas_trabajadas = "", descripcion = "", proyecto_id = None, empleado_id = None):
        self._id = id
        self._fecha_inicio = fecha_inicio
        self._horas_trabajadas = horas_trabajadas
        self._descripcion = descripcion
        self._proyecto_id = proyecto_id
        self._empleado_id = empleado_id
        
    # Getters
        
    def get_id(self):
        return self._id
        
    def get_fecha_inicio(self):
        return self._fecha_inicio
        
    def get_horas_trabajadas(self):
        return self._horas_trabajadas
        
    def get_descripcion(self):
        return self._descripcion
    
    def get_proyecto_id(self):
        return self._proyecto_id
    
    def get_empleado_id(self):
        return self._empleado_id
    # Setters
        
    def set_id(self, id):
        self._id = id
        
    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio
        
    def set_horas_trabajadas(self, horas_trabajadas):
        self._horas_trabajadas = horas_trabajadas
        
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
        
    def set_proyecto_id(self, proyecto_id):
        self._proyecto_id = proyecto_id
        
    def set_empleado_id(self, empleado_id):
        self._empleado_id = empleado_id