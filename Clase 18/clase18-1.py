import os
#Operative Sistem
with open("C:/Users/JONATHAN/Documents/Poo - Python/Clase18/texto.txt", "a") as archivo:
    #Codigo para leer o escribir el archivo
    contenido = "\nPablo Hernan Juan Carrai"
    archivo.write(contenido)

with open("C:/Users/JONATHAN/Documents/Poo - Python/Clase18/texto.txt", "r") as archivo:
    print(archivo.read())
#Abrir, leer o escribir un archivo

#Crear un archivo

open("marina.db", "x")

