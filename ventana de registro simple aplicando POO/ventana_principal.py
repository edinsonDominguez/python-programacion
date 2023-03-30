from tkinter import Frame, Tk
from registro import FrameRegistro    
root = Tk()
root.geometry('500x600')
root.resizable(False, False)

framePrincipal = Frame(root, bg='#1f497d')
framePrincipal.place(x=0, y=0, width=500, height=600)

frameRegistro = FrameRegistro(master=framePrincipal)
frameRegistro.place(x=10, y=10, width=480, height=580)

root.mainloop()

