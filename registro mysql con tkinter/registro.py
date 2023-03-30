from tkinter import messagebox, Frame, Entry, Label, Button, END
from dao.registroDAO import EmpleadoDAO
from vo.empleado import Empleado

# en esta clase se crea el formulario de registro

class RegistroEmpleado(Frame):

    def __init__(self, master=None):
       super().__init__(master)
       self.master = master

       self.config(bg='#A2CAFB')
       self._crearFrame()

    def _registrar(self):
        emp = Empleado()
        emp._setIdEmpleado(self.txt_id.get())   
        emp._setNombre(self.txt_nombre.get().upper())
        emp._setProfesion(self.txt_profesion.get().upper())
        emp._setSueldo(int(self.txt_sueldo.get()))
        emp._setDireccion(self.txt_direccion.get().upper())
        emp._setTelefono(self.txt_telefono.get())
        
        daoEmpleado = EmpleadoDAO()

        validacion_bd = daoEmpleado.registrarEmpleado(emp)
        
        if  validacion_bd == 'ok':
            messagebox.showinfo('Registro exitoso !!', 'se registro el empleado correctamente !!')
            self._limpiar()
        else:
            messagebox.showinfo('ERROR !!', 'No se pudo registrar el usuario')

    def _limpiar(self):
        # limpia los campos 
        self.txt_id.delete('0', END)
        self.txt_nombre.delete('0', END)
        self.txt_profesion.delete('0', END)
        self.txt_sueldo.delete('0', END)
        self.txt_telefono.delete('0', END)
        self.txt_direccion.delete('0', END)

    def _crearFrame(self):

        lbl = Label(self, text='REGISTRO DE EMPLEADOS')
        lbl.place(x=150, y=10, width=200, height=30)

        lbl = Label(self, text='Id Empleado')
        lbl.place(x=40, y=70, width=100, height=30)

        self.txt_id = Entry(self)
        self.txt_id.place(x=160, y=70, width=150, height=30)

        lbl = Label(self, text='Nombre')
        lbl.place(x=40, y=110, width=100, height=30)

        self.txt_nombre = Entry(self)
        self.txt_nombre.place(x=160, y=110, width=150, height=30)
        
        lbl = Label(self, text='Profesion')
        lbl.place(x=40, y=150, width=100, height=30)

        self.txt_profesion = Entry(self)
        self.txt_profesion.place(x=160, y=150, width=150, height=30)
        
        lbl = Label(self, text='Sueldo')
        lbl.place(x=40, y=190, width=100, height=30)

        self.txt_sueldo = Entry(self)
        self.txt_sueldo.place(x=160, y=190, width=150, height=30)

        lbl = Label(self, text='Direccion')
        lbl.place(x=40, y=230, width=100, height=30)

        self.txt_direccion = Entry(self)
        self.txt_direccion.place(x=160, y=230, width=150, height=30)

        lbl = Label(self, text='Telefono')
        lbl.place(x=40, y=270, width=100, height=30)

        self.txt_telefono = Entry(self)
        self.txt_telefono.place(x=160, y=270, width=150, height=30)

        btn_registro = Button(self, text='Registrar', command=self._registrar)
        btn_registro.place(x=230, y=320, width=120, height=40)
        