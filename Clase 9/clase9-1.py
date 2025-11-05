from tkinter import *

ventana = Tk()
texto1 = Label(ventana, text="Bienvenido a pablo 3.1 ").grid(column=0,row=1)
texto2 = Label(ventana, text="Mauro es el mejor, mejor que nadie mas").grid(column=1,row=1)
boton1 = Button(ventana, text="Enviar").grid(column=0,row=0)
boton2 = Button(ventana, text="Haz clic").grid(column=1,row=0)
ventana.mainloop()