#Entrada de datos
from tkinter import *

def ObtenerNombre():
    obteneringreso = int(nombre.get())
    print(f"El usuario ingreso: {obteneringreso}")
    print(f"El usuario ingreso: {nombre.get()}")
    print(5+obteneringreso)

ventana = Tk()
texto1 = Label(ventana, text="Nombre:").grid(column=0,row=0)
nombre = Entry(ventana)
nombre.grid(column=1,row=0)

enviar = Button(ventana, text="Enviar", command=ObtenerNombre).grid(column=0,row=1)
ventana.mainloop()