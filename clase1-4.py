#Constructor como tal es como un método pero que permite darle valor a el atributo que posee el objeto
"""class cubierto:
    #atributos
    forma = "cuchara"
    marca = "tramontina"
    color = "negro"
    material = "aluminio"""
class cubierto:
    def __init__(self, forma, marca, color, material):
        print(f"Se creo correctamente el cubierto con forma de {forma} de la marca {marca} y de color {color} con el material {material}")

#Objeto - Constructor - Obligatorio:
#Necesito si o si enviarle cuando lo instancio los valores que va a tener cada uno de los atributos

Cuchara = cubierto("cuchara ","Tramontina","azul","plastico")

Cuchillo = cubierto()
#Esto es un error, porque si o si, le tengo que dar los valores que tiene el objeto en los atributos