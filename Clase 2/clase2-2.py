"""Realizar un objeto con un constructor que permita comprar entradas de una funcion de teatro. Debe permitir ingresar la cantidad de butacas, sector, precio y fecha. Debe mostrar las 5 funciones. Las fechas son: 30/08 - 11/09 - 21/09 - 14/10 y 25/12"""
class FuncionesTeatro:
    def __init__(self, teatro, butacas, sector, precio, fecha, nomfunc):
        print(f"Nombre del teatro: {teatro} | Funcion: {nomfunc} | Cant. Butacas: {butacas} | Sector: {sector} | Precio: {precio} | Fecha: {fecha}")

GranRex = FuncionesTeatro("Gran Rex", 17, "A",123045,"30/08","El zorro")
LunaPark = FuncionesTeatro("Luna Park", 45, "B",223045,"11/09","Disney On ice")
Opera = FuncionesTeatro("Opera", 71, "J",323045,"21/09","Power Rangers")
Movistar = FuncionesTeatro("Movistar Arena", 25, ">",23045,"14/10","El zorro")
Devoto = FuncionesTeatro("Teatro Devoto", 16, "B",205045,"25/12","El zorro")
        