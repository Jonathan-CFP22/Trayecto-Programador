class persona:
    def __init__(self,nombre,edad,nacionalidad,sexo):
        print(f"El nombre de la persona es: {nombre} la edad: {edad}, cuya nacionalidad es: {nacionalidad} de sexo: {sexo}")

salida = ""
for I in range(10):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    nacionalidad = input("Ingrese su nacionalidad: ")
    sexo = input("ingrese su sexo: ")
    mostrar = persona(nombre,edad,nacionalidad,sexo)        
