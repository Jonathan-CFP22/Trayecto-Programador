class FuncionesTeatro:
    fecha = ["30/08","11/09","21/09","14/10","25/12"]
    def __init__(self, teatro, butacas, sector, precio, nomfunc, i):
        print(f"Nombre del teatro: {teatro} | Funcion: {nomfunc} | Cant. Butacas: {butacas} | Sector: {sector} | Precio: {precio} | fecha {self.fecha[i]}")
Opera = FuncionesTeatro("Opera",12,"A",21212,"Arrepentidos",0)