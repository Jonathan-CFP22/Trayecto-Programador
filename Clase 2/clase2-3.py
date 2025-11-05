class Equipo:
    nombrejg="pablo"
    posicion="defensa"
    altura="1.80"
    peso="49"
    pelo="rubio"
    def Mostrar():
        print("Hola pablo")
    @staticmethod
    def prueba():
        print(f"Hola mauro {self.peso}")


Equipo.prueba()
Equipo.Mostrar()