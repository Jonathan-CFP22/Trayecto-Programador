class Persona:
    nombre=""
    apellido=""
    precios=[]
    total=0
    def Ingreso(self,nom="",ape="",pre=1):
        nom=input("Ingrese el nombre de la persona: ")
        self.nombre=nom
        ape=input("Ingrese el apellido de la persona: ")
        self.apellido=ape
        while(pre!=0):
            pre=int(input("Ingrese el precio o ingrese 0 para salir: "))
            self.total+=pre
            self.precios=pre
    def Mostrar(self):
        print(f"El nombre es: {self.nombre} el apellido es: {self.apellido}")
    def TotalAcumulado(self):
        print(f"El total acumulado es: {self.total}")

bandera = 0
while(bandera == 0):
    ingreso = Persona()
    ingreso.Ingreso()
    ingreso.Mostrar()
    bandera = int(input("Ingrese 0 para continuar o 1 para salir: "))

ingreso.TotalAcumulado()