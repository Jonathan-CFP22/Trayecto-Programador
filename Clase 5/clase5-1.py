#programa que permita calcular el total de una compra para 20 clientes. Sabiendo que los productos son: televisores y smartv. Se necesita saber el mínimo gastado y el promedio gastado
Productos = []
Productos.append([0,"Televisor JBL","JBL",2000])
Productos.append([1,"Televisor Samsung","Samsung",4000])
class Cliente:
    id_cliente = 0
    gastado=0
    id_cliente += 1
    def __init__(self,nomcliente="",direccion=""):
        nomcliente = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese el nombre del cliente: ")

class Carrito:
    id_carrito = 0
    id_carrito += 1
    subtotal=0
    id_producto=0
    def __init__(self,idproducto=0):
        idproducto=int(input("Ingrese el id del producto: "))
        self.id_producto=idproducto
    def GetProducto(self):
        if(self.id_producto==0):
            self.subtotal+=Productos[0][4]
        if(self.id_producto==1):
            self.subtotal+=Productos[1][4]
        if(self.id_producto==2):
            self.subtotal+=Productos[2][4]
        if(self.id_producto==3):
            self.subtotal+=Productos[3][4]

min_gastado=99999999999999
promedio=0
total=0
for I in range(0,10):
    Clien = Cliente()
    print("Este es el catalogo de nuestros productos: ")
    for y in range(0,len(Productos)):
        for z in range(0,4):
            print(Productos[y][z])
    cart = Carrito()
    while(True):
        cart = Carrito()
        Clien.gastado=cart.GetProducto()
        if(Clien.gastado<min_gastado):
            min_gastado=Clien.gastado
        if(input("Desea continuar?")):
            print("Sigue ingresando productos al carrito")
        else:
            break
        total+=Clien.gastado
    
promedio=total/10
print(f"Promedio {promedio}")