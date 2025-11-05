class Reloj:
    total = 0
    def __init__(self,material="",tamanio="",marca="",precio=0):    
        self.total += precio
        print(f"La marca del reloj es: {marca} El tamaño es: {tamanio} El material con el cual esta hecho el reloj es: {material} el precio es: {precio}")

Mauro = Reloj(input("Ingrese el materiall: "),input("Ingrese el tamaño: "),input("Ingrese la marca: "),int(input("Ingrese el precio: ")))

print(Mauro.total)