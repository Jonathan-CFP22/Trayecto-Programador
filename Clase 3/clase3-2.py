#Herencia - Es un proceso por el cual se puede establecer una clase que hereda los métodos y atributos de la clase principal. Es decir, como si fuese un legado familiar, donde la madre es la que da vida y da la genetica a su hijo/a y que el hijo/a puede sobreescribir o incluso definir nuevos métodos y/o atributos. Entonces se podría decir que podemos establecer mediante la herencia modificaciones o mutaciones a la clase original.
"""Ejemplos"""
class Animal:
    reino="vegetal"
    def GetReino(self):
        print(self.reino)

class Gato(Animal):
    patas = 4
    def GetPatas(self):
        print(f"Reino:{self.reino} {self.patas} patas")
    def SetDatos(self):
        self.patas=5
        self.reino="carnivoro"

Gerbasio = Animal()
Gerbasio.GetReino()

Persa = Gato()
Persa.SetDatos()
Persa.GetPatas()