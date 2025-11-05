#Se pide programar un objeto que procese distintas materias en un cuatrimestre de una universidad. Debe procesarse el nombre de la materia, el docente a cargo, el nombre de la carrera, el turno y la cantidad de alumnos anotados. Por otro lado cada alumno debe poseer un nombre y apellido, dni, y las notas de cada materia. Se pide mostrar los alumnos que hayan aprobado las materias sabiendo que se aprueba con 4 o más. Mostrando un cartel diciendo "Aprobado" En cualquier otro caso "Recursa".
"""Universidad de Palermo"""
"""Carrera Arquitectura"""
class Materias:
    def __init__(self):
        self.nomateria=input("Ingrese el nombre de la materia: ")
        self.docente=input(f"Docente a cargo de la materia {self.nomateria} : ")
        self.turno=input(f"Ingrese el turno que tiene asignado el docente {self.docente}: ")
        self.calumnos=int(input(f"Ingrese la cantidad de alumnos anotados en  {self.nomateria}: "))      
        self.cantnotas=int(input(f"Ingrese la cantidad de notas de la materia {self.nomateria}: "))
        self.carrera="Arquitectura"

class Alumnos:
    def __init__(self):
        self.notas=[]
        self.promedio=0
        materia = Materias()
        i=0
        while(i<materia.calumnos):
            i+=1
            self.suma=0
            self.nomyapellido=input("Ingrese el nombre y apellido del alumno: ")
            self.dni=int(input(f"Ingrese el dni de {self.nomyapellido}: "))
            for I in range (0,materia.cantnotas):
                ingreso=int(input(f"Ingrese la nota de la materia: {materia.nomateria}"))
                self.notas.append(ingreso)
                self.suma+=ingreso
            self.promedio=self.suma/materia.cantnotas
            if(self.promedio>=4):
                print(f"El alumno {self.nomyapellido} Aprobo la materia {materia.nomateria}")
            else:
                print(f"El alumno {self.nomyapellido} Desaprobo la materia {materia.nomateria}")
    
Jose = Alumnos()
