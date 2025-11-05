from tkinter import *
from tkinter import ttk

botonera = Tk()
botonera.geometry("500x500")
boton1 = Button(botonera, text="Primer boton")
boton1.pack()
#Boton con color de fondo
boton2 = Button(botonera, text="Boton con fondo", background="#3de21a")
boton2.pack()
#boton con color de texto
boton3 = Button(botonera, text="Boton con texto de color", fg="#4ed1ac")
boton3.pack()
#Boton fusion
boton4 = Button(botonera, text="Boton fusionado", background="#44ac21", fg="#9f21ad")
boton4.pack()
botonera.mainloop()