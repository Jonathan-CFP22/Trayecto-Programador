class Reloj:
    material = ""
    tamanio = ""
    marca = ""
    precio = 0
    total = 0
    def Ingreso(self):
        self.material = input("Ingrese el tipo de material: ")
        self.tamanio = input("Ingrese el tamaño del reloj: ")
        self.marca = input("Ingrese la marca del reloj: ")
        self.precio = int(input("Ingrese el precio del reloj: "))
        self.total += self.precio
    def MostrarReloj(self):
        print(f"La marca del reloj es: {self.marca} El tamaño es: {self.tamanio} El material con el cual esta hecho el reloj es: {self.material} el precio es: {self.precio}")

Factura = Reloj()
Factura.Ingreso()
Factura.MostrarReloj()
Factura.total