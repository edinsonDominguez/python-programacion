from tkinter import Tk, messagebox, Frame, Entry, Label, Button
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
        pass

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

        self.txt_Profesion = Entry(self)
        self.txt_Profesion.place(x=160, y=150, width=150, height=30)
        
        lbl = Label(self, text='Sueldo')
        lbl.place(x=40, y=190, width=100, height=30)

        self.txt_Sueldo = Entry(self)
        self.txt_Sueldo.place(x=160, y=190, width=150, height=30)

        lbl = Label(self, text='Direccion')
        lbl.place(x=40, y=230, width=100, height=30)

        self.txt_Direccion = Entry(self)
        self.txt_Direccion.place(x=160, y=230, width=150, height=30)

        lbl = Label(self, text='Telefono')
        lbl.place(x=40, y=270, width=100, height=30)

        self.txt_Telefono = Entry(self)
        self.txt_Telefono.place(x=160, y=270, width=150, height=30)

        btnRegistro = Button(self, text='Registrar', command=self._registrar)
        btnRegistro.place(x=230, y=320, width=120, height=40)
        