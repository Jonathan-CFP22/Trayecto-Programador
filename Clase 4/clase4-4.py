import random
class jugador:
    nombre=""
    forma=""
    cant=4

jugador1 = jugador()
jugador1.nombre=input("Ingrese un nombre: ")
jugador1.forma="X"
jugador2 = jugador()
jugador2.nombre=input("Ingrese otro nombre para el segundo jugador: ")
jugador2.forma="O"

#ronda1

#random.randint - Es un numero aleatorio de tipo entero y en el parentesis se establece entre que numeros va a generar el numero aleatorio
jugador1.cant=jugador1.cant-random.randint(0,4)
print("**** Ronda 1 ****")
print(f"La cantidad de X que tiene el jugador1 es: {jugador1.cant}")
#Jugador2
jugador2.cant=jugador2.cant-random.randint(0,4)
print(f"La cantidad de O que tiene el jugador2 es: {jugador2.cant}")