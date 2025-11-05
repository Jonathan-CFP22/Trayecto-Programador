import os

ruta = (os.path.abspath("clase18-2.py"))

print(f"La ruta es {ruta}")

#Otra forma de obtener o de devolver la ruta es
print(os.path.basename("c:/ProgramFiles/Poo"))

print(os.path.basename("c:\\ProgramFiles\\Poo"))

base = "/ProgramFiles/Poo/"
print(os.path.basename(base))

#Otra forma de obtener o devolver rutas

dir = "c:/Users\JONATHAN\Documents\Poo - Python\Clase18\marina.db"
print(os.path.dirname(dir))

#El ultimo para obtener o devolver rutas
print(os.path.realpath("clase18-2.py"))
print(os.path.realpath("marina"))

