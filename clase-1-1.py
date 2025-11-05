class Persona:
    #Atributo
    nombre = "pepe"
    pelo = "negro"

persona1 = Persona() #Instancio un objeto, el objeto cual es el que estamos instanciando: en este caso Persona
print(persona1.nombre)
persona2 = Persona()
print(persona2.pelo)
#ej:
persona2.pelo="marron"
print(persona2.pelo)
print("Persona1:"+persona1.pelo)
persona3 = Persona()
print(persona3.pelo)

