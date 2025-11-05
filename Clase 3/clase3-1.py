#Realizar un objeto que permita ingresar 30 paises que participan del mundial, se pide mostrar nombre, bandera, puntos, grupo y posicion de cada uno

class Copa:
    mostrar=[]
    grupoa=[]
    def __init__(self,puntos=0,posicion=0):
        bandera = input("Ingrese la bandera del pais: ")
        nombre = input("Ingrese el nombre del pais: ")
        grupo = input(f"Ingrese el grupo al cual se encuentra asignado el pais {nombre}: ").upper()
        self.mostrar.append(f"El nombre del pais seleccionado es: {nombre} la bandera es la siguiente: {bandera}. El grupo asignado es: {grupo}. Su posición es: {posicion} y posee {puntos} puntos.")
        if(grupo=="A"):
            self.grupoa.append(f"El nombre del pais seleccionado es: {nombre} la bandera es la siguiente: {bandera}. El grupo asignado es: {grupo}. Su posición es: {posicion} y posee {puntos} puntos.")
        if(grupo=="B"):
            self.grupob.append(f"El nombre del pais seleccionado es: {nombre} la bandera es la siguiente: {bandera}. El grupo asignado es: {grupo}. Su posición es: {posicion} y posee {puntos} puntos.")
        if(grupo=="C"):
            self.grupoc.append(f"El nombre del pais seleccionado es: {nombre} la bandera es la siguiente: {bandera}. El grupo asignado es: {grupo}. Su posición es: {posicion} y posee {puntos} puntos.")

for i in range(1,11):
    crearpais = Copa()


for i in range(0,10):
    print(crearpais.grupoa[i])