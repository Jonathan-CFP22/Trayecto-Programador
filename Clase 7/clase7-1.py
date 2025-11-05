from tkinter import *
from tkinter import ttk
def Saludar():
    mostrarsaludo = ttk.Label(programa, text="Bienvenido lautaro")
    mostrarsaludo.pack()
#import tkFont
programa = Tk()
espacio = ttk.Label(programa, text="Bienvenido a python")#Salida de texto
#fuentes = tkFont.Font(family="Arial", size=22)#Utilizando el modulo Tkfont que a veces viene integrado y a veces se instala
boton = ttk.Button(programa, text="Realizar suma", command=Saludar)
espacio.pack()#Pack
boton.pack()
#espacio.grid()#Grid
programa.mainloop()