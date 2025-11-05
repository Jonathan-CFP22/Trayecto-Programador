"""Ejemplos"""
class Animal:
    reino="vegetal"
    def GetReino(self):
        print(self.reino)

class Gato(Animal):
    Animal.reino="carnivoro"#esto modifica al atributo original del cual hereda - Este tipo de modificacion no se utiliza en casi ningun caso
    patas = 4 #atributo que nace en 
    def GetPatas(self):#Creo un metodo para obtener el valor de los atributos tanto de la clase madre como del hijo
        print(f"Reino:{self.reino} {self.patas} patas")#imprimo o muestro los valores que tiene almacenado los atributos
    def SetDatos(self):#Creo un metodo para establecer o setear valores en los atributos.
        self.patas=5#aca se modifica el atributo patas que es creado dentro de la clase gato
        self.reino="carnivoro"#aca se modifica el atributo reino que es creado dentro de la clase madre (Animal)

class Perro(Animal):
    def GetCambios(self):#Se obtiene el valor del atributo de la clase animal del cual estamos heredando
        print(f"El reino {self.reino}")

nicaragua=Animal()
nicaragua.GetReino()

siberiano=Gato()
siberiano.SetDatos()
siberiano.GetPatas()

Aleman=Perro()
Aleman.GetCambios()