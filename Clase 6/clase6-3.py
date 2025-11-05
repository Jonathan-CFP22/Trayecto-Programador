#Realizar un programa que procese 10 clientes de un banco. Se pide mostrar el tipo de cuenta (sueldo - credito). Se debe permitir al usuario realizar transferencias y depósitos en su cuenta mediante un cbu o alias que es generado por el banco.
import random
alias=["client.bbva","client.santander","client.mp","client.cocacola"]
class Clientes:
    def __init__(self):
        self.dinero=0
        self.cbu=random.getrandbits(8)
        self.alias=random.choice(alias)
        while(True):
            self.cuenta=input("Ingrese tipo de cuenta: ").lower()
            if(self.cuenta=="sueldo" or self.cuenta=="credito"):
                break
        if(self.cuenta=="sueldo"):
            self.dinero=float(input("Ingrese su sueldo: "))
            self.Dinero()
        else:
            self.Dinero()
        print(f"Cuenta creada!\n su cbu es: {self.cbu}\n su alias es: {self.alias}")
        if(input("Oprima enter para modificar el alias ")==""):
            self.alias=input("Ingrese el alias que desea: ")
            print(f"Su nuevo alias es: {self.alias}")
        if(input("Oprima enter para realizar depósito en su cuenta ")==""):
            self.Deposito()
        if(input("Oprima enter para realizar transferencias ")==""):
            self.Transferencias()
        self.Consulta()
    def Consulta(self):
        if(input("Oprima Enter para ver el dinero que posee en su cuenta ")==""):
            if(self.verificar):
                self.Dinero()
    def Dinero(self):
        print(f"Usted posee ${self.dinero} en su cuenta! ")
    def verificar(self):
        while(True):
            print("Para verificar su usuario le vamos a pedir que ingrese su cbu o alias")
            if(input("Oprima enter si desea ingresar su cbu ")==""):
                if(int(input("Ingrese su cbu: "))==self.cbu):
                    print("Verificado")
                    return True
                    break
            elif(input("Oprima enter si desea ingresar su alias ")==""):
                if(input("Ingrese su alias: ")==self.alias):
                    print("Verificado")
                    return True
                    break
    def Deposito(self):
        if(self.verificar()):
            self.dinero+=float(input("Ingrese el dinero que desea ingresar en su cuenta: "))
            self.Dinero()
    def Transferencias(self):
        if(self.verificar()):
            self.dinero-=float(input("Ingrese la cantidad que desea transferir: "))
            self.Dinero()

Pedro = Clientes()