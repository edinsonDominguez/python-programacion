from tkinter import Label, Entry, Button, messagebox, Frame

class FrameRegistro(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.config(bg='#fff')
        self._crearFrame_()
    
    def registrar(self):
        nombre = self.txtNombre.get()
        valor = self.txtValor.get()
        cantidad = self.txtCantidad.get()
        total = int(valor) * int(cantidad)
        
        mensaje = 'se registraron ' + cantidad + ' unidades de ' + nombre + ' con un costo de $ '+ valor + ' el valor total fue de ' + str(total)
        return messagebox.showinfo('Registro exitoso !!', mensaje)


    def _crearFrame_(self):
        
        lblTitulo = Label(self, text = 'REGISTRO DE PRODUCTOS')
        lblTitulo.place(x=20, y=10, width=400, height=30)

        lbl = Label(self, text= 'Nombre')
        lbl.place(x=30, y=60, width=100, height=30)

        self.txtNombre = Entry(self)
        self.txtNombre.place(x=140, y=60, width=100, height=30)

        lbl = Label(self, text='Valor')
        lbl.place(x=30, y=100, width=100, height=30)

        self.txtValor = Entry(self)
        self.txtValor.place(x=140, y=100, width=100, height=30)

        lbl = Label(self, text='Cantidad')
        lbl.place(x=30, y=140, width=100, height=30)

        self.txtCantidad = Entry(self)
        self.txtCantidad.place(x=140, y=140, width=100, height=30)

        btnRegistro = Button(self, text='Registrar', command= self.registrar)
        btnRegistro.place(x=260, y=190, width=100, height=30)
