from tkinter import Tk, Frame, Button
from registro import RegistroEmpleado
from datos import InfoEmpleado


ventana = Tk()
ventana.geometry('900x600')
ventana.title('empleados')
ventana.resizable(False, False)


frameRegistro = RegistroEmpleado(master=ventana)
frameRegistro.place(x=0, y=0, width=900, height=600)


ventana.mainloop()