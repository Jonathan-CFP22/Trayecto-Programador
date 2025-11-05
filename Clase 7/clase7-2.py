from tkinter import *
from tkinter import ttk
ventana = Tk()
ventana.title("Pablo 2.0 ✌")#Titulo a la ventana
ventana.geometry("400x400")#Defino el tamaño de la ventana
bienvenida = ttk.Label(ventana, text="Hola vale vengo a flotar 😊")
bienvenida.pack()
bienvenida.config(font=("Arial", 25))#propiedad font, widget config establecemos tipografia y tamaño
ventana.mainloop()