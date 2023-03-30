from tkinter import Tk, Frame
from registro import RegistroEmpleado
ventana = Tk()
ventana.geometry('600x600')
ventana.title('empleados')
ventana.resizable(False, False)

frameRegistro = RegistroEmpleado(master=ventana)
frameRegistro.place(x=0, y=0, width=600, height=600)

ventana.mainloop()