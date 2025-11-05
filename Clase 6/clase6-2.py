#Realizar un programa para una heladeria que necesita generar 10 sabores de helados. Se pide mostrar los distintos sabores con el precio.
class Heladeria:
    def __init__(self):
        self.mostrar=""
        self.total=0
        for i in range(0,9):
            self.sabor=input("Ingrese el sabor de helado: ")
            self.precio=int(input(f"Ingrese el precio de {self.sabor}: "))
            self.total+=self.precio
            self.mostrar+=f"El sabor {self.sabor} sale ${self.precio}\n"
        print(self.mostrar)
        print(f"El total gastado es: ${self.total}")

Grido = Heladeria()