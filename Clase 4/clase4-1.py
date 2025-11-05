#Realizar un objeto que permita crear 10 mesas, se pide mostrar el material, la cantidad de patas, el precio y el tiempo de producción
#Se pide mostrar al final el total gastado
class Mesa:
    operacion=0
    acumostrar=""
    def __init__(self):
        material = input("Ingrese el tipo de material: ")
        cpatas = int(input("Ingrese la cantidad de patas:"))
        precio = float(input("Ingrese el precio x hora: "))
        tprod = int((input("Ingrese el tiempo total de producción: ")))
        self.operacion+=precio*tprod
        self.acumostrar += f"La mesa ha sido creada con el material: {material} y la cantidad de patas: {cpatas} el precio de este producto es: {precio*tprod}\n"

total=0
mostrar=""
for I in range(1,6):
    nuevamesa = Mesa()
    total+=nuevamesa.operacion
    mostrar+=nuevamesa.acumostrar

print(mostrar)
print(total)