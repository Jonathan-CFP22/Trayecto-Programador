#Realizar un objeto que permita crear 10 mesas, se pide mostrar el material, la cantidad de patas, el precio y el tiempo de producción
#Se pide mostrar al final el total gastado
class Produccion:
    mostrar=""
    total=0
    def __init__(self):
        cpatas = int(input("Ingrese la cantidad de patas: "))
        material = input("Ingrese el tipo material: ")
        precio = float(input("Ingrese el precio: "))
        tiempop= int(input("Ingrese el tiempo de produccion: "))
        self.mostrar+=f"El material de la mesa creada con patas {cpatas} es de {material} y llevo un tiempo de produccion de {tiempop} minutos y su precio es de ${precio*tiempop}\n"
        self.total+=precio*tiempop
    def MostrarMesa(self):
        print(self.mostrar)
    def MostrarTotal(self):
        print(self.total)

for I in range(1,6):
    mesa = Produccion()

mesa.MostrarMesa()
mesa.MostrarTotal()