#Realizar un objeto que permita crear 10 mesas, se pide mostrar el material, la cantidad de patas, el precio y el tiempo de producción
#Se pide mostrar al final el total gastado

class Mesas:
    def __init__(self,n=1):
        total=0
        mostrar=""
        while(n!=0):
            material=input("Ingrese el tipo material: ")
            precio=int(input("Ingrese el precio: "))
            produccion=int(input("Tiempo produccion: "))
            patas=int(input("Ingrese cant paas: "))
            mostrar+=f"El material elaborado es {material} el tiempo de produccion es de {produccion} minutos. Cantidad de patas {patas} y el precio es: {produccion*precio}\n"
            n=int(input("Ingrese 0 para salir o cualquier numero para continuar: "))
            total+=produccion*precio
        print(f"El toal es: {total}")
        print(f"{mostrar}")

objeto = Mesas()