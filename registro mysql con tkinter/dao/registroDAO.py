import mysql.connector
from vo.empleado import Empleado 

class EmpleadoDAO():
    
    # conexion Con la base de datos
    conn = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='', db='empresa')

    # registro de empleados en la base de datos
    def registrarEmpleado(self, empleado_vo: Empleado):
        
        cur = self.conn.cursor()
        mensaje = "INSERT INTO empleado(id_empleado, nombre, profesion, sueldo, direccion, telefono) \
            values ('{}','{}','{}', '{}', '{}', '{}' )".format(
                empleado_vo._getIdEmpleado(),
                empleado_vo._getNombre(),
                empleado_vo._getProfesion(),
                empleado_vo._getSueldo(),
                empleado_vo._getDireccion(),
                empleado_vo._getTelefono(),
            )
        cur.execute(mensaje)
        self.conn.commit()
        cur.close()
        
        return 'ok'

    def listaEmpleado(self):
        pass