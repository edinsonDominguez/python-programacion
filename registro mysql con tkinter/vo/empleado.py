# los datos de los empleados seran transportados por medio de esta clase
class Empleado():

    def __init__(self):
        self.id_empleado: int
        self.nombre: str
        self.profesion: str
        self.sueldo: int
        self.direccion: str
        self.telefono: str
    
    def _setIdEmpleado(self, id_empleado:int):
        self.id_empleado = id_empleado

    def _getIdEmpleado(self):
        return self.id_empleado
    
    def _setNombre(self, nombre:str):
        self.nombre = nombre

    def _getNombre(self):
        return self.nombre

    def _setProfesion(self, profesion:str):
        self.profesion = profesion

    def _getProfesion(self):
        return self.profesion

    def _setSueldo(self, sueldo:int):
        self.sueldo = sueldo

    def _getSueldo(self):
        return self.sueldo

    def _setDireccion(self, direccion:str):
        self.direccion = direccion

    def _getDireccion(self):
        return self.direccion
    
    def _setTelefono(self, telefono:str):
        self.telefono = telefono

    def _getTelefono(self):
        return self.telefono

