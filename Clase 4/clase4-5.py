import random
frutas = ["banana","kiwi","melon"]
fruta_aleatoria = random.choice(frutas)

intento = 2
usuario = input("Ingrese la posible fruta elegida por la maquina: ").lower()
if(usuario==fruta_aleatoria):
    print(f"Has acertado la fruta era: {fruta_aleatoria}")
else:
    intento=intento-1