from tkinter import *
def Saludar():
    print(f"Hola {nombre} Gigante")

nombre = "Pablo"
def Despedida():
    print(f"Chau {nombre} Gigante")

class Celular:
    def __init__(self):
        self.nombre=input("Ingresa el nombre del celular: ")
        self.precio=float(input("Ingrese el precio del celular: "))
        print(f"Se ha creado el celular {self.nombre} con el precio ${self.precio}\n")