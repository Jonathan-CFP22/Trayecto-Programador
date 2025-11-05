from tkinter import *
from tkinter import ttk
#programamos la funcion que luego se accionará cuando se presiona el boton que la ejecuta
def Saludar():
    hola = Label(ventana, text="Bienvenido a Mauro 2.1")
    hola.pack()
ventana = Tk()
#Modificar los ajustes de la ventana
ventana.geometry("400x400")
#Estamos estableciendo el minimo indispensable del tamaño de nuestro programa que ocupa en la pantalla
texto = Label(ventana, text="Texto hermoso en nuestra apliacion")
#Se tiene incorporar en algun lugar de nuestra para eso utilizamos el metodo pack()
texto.pack()
#Incorporamos boton
boton = Button(ventana, text="Bienvenido") #No tiene ninguna accion programada
boton.pack()
#vamos a programar alguna accion cuando se presiona el boton
bienvenido = Button(ventana, text="Haz clic para saludar", command=Saludar)
#Falta que aparezca el boton para accionar la bienvenida
bienvenido.pack()
ventana.mainloop()