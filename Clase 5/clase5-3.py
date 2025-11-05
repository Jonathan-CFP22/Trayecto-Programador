class Peliculas:
    def __init__(self,nombre="",anio=0,genero="",suscripcion=""):
        nombre=input("Ingrese el nombre de la pelicula: ")
        anio=int(input("Ingrese el año de la pelicula: "))
        genero=input("Ingrese el genero de la pelicula: ")
        suscripcion=input("Ingrese el tipo de suscripcion que debe teenr el usuario para visualizar esta pelicula: ")
        self.nombre=nombre
        self.anio=anio
        self.genero=genero
        self.suscripcion=suscripcion
        print(f"El nombre de la pelicula ingresada es: {self.nombre} el año es: {self.anio}. El genero: {self.genero}. El tipo de suscripcion que debe tener el usuario es: {self.suscripcion}")

class Usuarios:
    def __init__(self,id_usuario=0,nombre="",mail="",suscripcion=""):
        id_usuario+=1
        nombre=input("Ingrese un nombre de usuario: ")
        mail=input("Ingrese el mail para registrar este usuario: ")
        suscripcion=input("Ingrese la suscripcion que desea contratar: ")
        self.nombre=nombre#reconvierto el parametro nombre en un atributo de la clase usuarios
        self.mail=mail#reconvierto el parametro mail en un atributo de la clase usuarios
        self.suscripcion=suscripcion#cambiando el tipo de valor al elemento, es decir, lo pasamos de un parametro a atributo
        print(f"El usuario {self.nombre} con el mail {self.mail} ha sido registrado con la suscripcion {self.suscripcion}")

class Alquiler:
    def __init__(self):
        pelicula = Peliculas()
        usuario = Usuarios()
        if(pelicula.suscripcion==usuario.suscripcion):
            print("Felicitaciones podes ver la pelicula")
        else:
            print("No podes ver la pelicula")

blockbuster = Alquiler()
netflix = Alquiler()
napster = Alquiler()
spotify = Alquiler()