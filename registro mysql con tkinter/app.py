from tkinter import Tk, Frame, Button
from registro import RegistroEmpleado
from datos import InfoEmpleado

def _infoEmpleado():
    frameDatos.place(x=0, y=0, width=900, height=600)
    frameRegistro.place_forget()
    btn_inicio.config(state='normal')
    btn_info.config(state='disabled')

def _registroEmpleado():
    frameRegistro.place(x=0, y=0, width=900, height=600)
    frameDatos.place_forget()
    btn_inicio.config(state='disable')
    btn_info.config(state='normal')

        

ventana = Tk()
ventana.geometry('900x600')
ventana.title('empleados')
ventana.resizable(False, False)

frameDatos = InfoEmpleado(master=ventana)

frameRegistro = RegistroEmpleado(master=ventana)
frameRegistro.place(x=0, y=0, width=900, height=600)

# nos lleva al formulario de registro de empleado
btn_inicio = Button(ventana, text='Registro', state='disabled', command=_registroEmpleado)
btn_inicio.place(x=780, y=5, width=100, height=25)

# nos lleva a la tabla de empleados
btn_info = Button(ventana, text='Ver empleados >>', command=_infoEmpleado)
btn_info.place(x=650, y=5, width=120, height=25)



ventana.mainloop()