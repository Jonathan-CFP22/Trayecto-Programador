import os
ruta_actual = os.path.abspath("clase18-3.py")
print(f"Estoy ubicado en {ruta_actual}")
#que seria el directorio
directorio = os.path.dirname(ruta_actual)
print(f"Este es el directorio {directorio}")

#open("lista_de_compras.txt", "x")


with open(os.path.realpath("lista_de_compras.txt"), "a") as archivo:
    archivo.write("\nArchivo creado")

with open(os.path.realpath("lista_de_compras.txt"), "r") as archivo:
    print(archivo.read())

archivo = os.path.abspath("texto.txt")
#print(archivo)
os.remove("C:/Users/JONATHAN/Documents/Poo - Python/Clase18/texto.txt")