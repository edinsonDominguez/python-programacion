from tkinter import Frame, Label, Button, ttk, messagebox
from dao.DAO import EmpleadoDAO

# esta clase visualiza los usuarios registrados en la base de datos 
class InfoEmpleado(Frame):

    daoEmpleado = EmpleadoDAO()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.config(bg='#A2CAFB')
        self._crearFrame()

    def _crearFrame(self):

        lbl = Label(self, text='INFORMACION DE EMPLEADOS')
        lbl.place(x=20, y=10, width=200, height=30)

        # creamos la tabla
        self.tabla_empleado = ttk.Treeview(self)
        self.tabla_empleado['columns'] = ('nombre', 'profesion', 'sueldo', 'direccion', 'telefono')

        # creamos las columnas
        self.tabla_empleado.column('#0', width=100)
        self.tabla_empleado.column('nombre')
        self.tabla_empleado.column('profesion', width=100)
        self.tabla_empleado.column('sueldo', width=100)
        self.tabla_empleado.column('direccion')
        self.tabla_empleado.column('telefono', width=100)

        #creamos los titulos de la tabla de empleados
        self.tabla_empleado.heading('#0', text='ID Empleado')
        self.tabla_empleado.heading('nombre', text='Nombre')
        self.tabla_empleado.heading('profesion', text='Profesion')
        self.tabla_empleado.heading('sueldo', text='Sueldo')
        self.tabla_empleado.heading('direccion', text='Domicilio')
        self.tabla_empleado.heading('telefono', text='Telefono')

        self.tabla_empleado.place(x=10, y=50, width=880, height=530)
        
        # llenamos la tabla        
        listaEmpleado = self.daoEmpleado._listaEmpleado()

        for i in listaEmpleado:
            self.tabla_empleado.insert('', 'end', text = i[0], values=(i[1], i[2], i[3], i[4], i[5]))


        #elimina el empleado de la lista
        btn_eliminar = Button(self, text='Eliminar', command=self._eliminarEmpleado)
        btn_eliminar.place(x=400, y=10, width=120, height=30)

    def _eliminarLista(self):
        for i in self.tabla_empleado.get_children():
            self.tabla_empleado.delete(i)

    def _eliminarEmpleado(self):

        # obtenemos el codigo del empleado
        codigoEmpleado = self.tabla_empleado.item(self.tabla_empleado.focus(), 'text')
        
        control = self.daoEmpleado._eliminarEmpleado(codigoEmpleado)

        if(control == 'ok'):
            messagebox.showinfo('Empleado eliminado!!', ' Se elimino el empleado correctamente !!')

        if(control == 'error'):
            messagebox.showinfo('ERROR !!', 'Error al eliminar el empleado!!')

        # actualizamos la tabla de empleados
        self._eliminarLista()
        listaEmpleado = self.daoEmpleado._listaEmpleado()

        for i in listaEmpleado:
            self.tabla_empleado.insert('', 'end', text = i[0], values=(i[1], i[2], i[3], i[4]))        

