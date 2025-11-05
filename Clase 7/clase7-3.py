from tkinter import *
from tkinter import ttk
packman = Tk()
boton = ttk.Button(packman, text="Haz clic")
boton.pack(expand=False)
registrar = Button(packman, text="Registrate!", background="blue", fg="white")
registrar.pack(side=LEFT)
contacto = Button(packman, text="Contactate", background="black", fg="gray")
contacto.pack(side=RIGHT)
arriba = Label(packman, text="Comienza la caceria")
arriba.pack(side=TOP)
abajo = Label(packman, text="Desarrollado por Marina")
abajo.pack(side=BOTTOM)
packman.mainloop()