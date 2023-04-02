import mysql.connector
from mysql.connector import Error
from vo.empleado import Empleado 

class EmpleadoDAO():
    
    # conexion Con la base de datos
    conn = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='', db='empresa')

    # registro de empleados en la base de datos
    def _registrarEmpleado(self, empleado_vo: Empleado):
        
        control = ''
        try:
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
            control = 'ok'
                    
        except Error as ex:
            print(ex)
            control = 'error'

        return control

    # obtiene los datos de los empleados de la base de datos
    def _listaEmpleado(self):

        cur = self.conn.cursor()
        mensaje = 'SELECT * FROM empleado'
        
        cur.execute(mensaje)
        lista = cur.fetchall()
        
        cur.close()

        return lista
    
    def _eliminarEmpleado(self, codigo: str):
        control = ''
        try:
            mensaje = "DELETE FROM empleado WHERE id_empleado = '{}' ".format(
                codigo
            )

            cur = self.conn.cursor()
            cur.execute(mensaje)
            self.conn.commit()
        
            cur.close()
            control = 'ok'
        
        except Error as ex:
            print(ex)
            control = 'error'

        return control
