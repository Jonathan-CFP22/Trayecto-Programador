#Realizar un login que permita ingresar el nombre, el mail y la contraseña para cada usuario. Luego mostrar los datos ingresados por pantalla
from tkinter import *
ventana = Tk()
etiqueta_nombre = Label(ventana, text="Nombre:").grid(row=0,column=0)
nombre = Entry(ventana)
nombre.grid(row=0,column=1)
etiqueta_mail = Label(ventana, text="Mail").grid(row=1,column=0)
mail = Entry(ventana)
mail.grid(row=1,column=1)
etiqueta_pw = Label(ventana, text="Contraseña").grid(row=2,column=0)
pw = Entry(ventana, show="#")
pw.grid(row=2,column=1)
#Inico de la función para obtener y mostrar los datos ingresados por el usuario
def ObtenerDatos():
    nom = nombre.get()
    email = mail.get()
    pwd = pw.get()
    texto = Label(ventana, text=f"El nombre del usuario es: {nom}\nEl mail del usuario ingresado es: {email}\nLa contraseña del usuario es: {pwd}").grid(row=4,column=1)
#Fin de la función para obtener y mostrar los datos del usuario
"""Esto es la incorporación del boton para registrar y accionar la función que va a obtener los datos ingresados y luego mostrarlos por interfaz"""
registrar = Button(ventana, text="Registrar", command=ObtenerDatos)
registrar.grid(row=3,column=2)
ventana.mainloop()