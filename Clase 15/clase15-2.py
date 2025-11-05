import tkinter as tk
import mariadb

hostname = mariadb.connect(host="localhost", user="root", password="",database="python")
cursor = hostname.cursor()
cursor.execute("SELECT * FROM USUARIOS")
#cursor.execute("SELECT * FROM usuarios") Obteniendo los datos como si fuesen tuplas, es decir datos fijos. Que solo puedo acceder por indice numerico y no por nombre de columna. Entonces ahora vamos a utilizar otro metodo que es el Row. Que devolvera los valores como objetos.
#hostname.row_factory = mariadb.Row Este metodo sirve siempre y cuando utilizamos  sqlite 
#utilizamos el atributo description
#print(cursor.description)
columna = cursor.description


#print(seleccion)
class Mostrar:
    def __init__(self):
        self.ventana=tk.Tk()
        self.columna = [columna[0] for columna in cursor.description]
        self.marco=tk.Frame(self.ventana, width=200,height=200)
        self.marco.pack()
        self.nombre_columna()
        self.ventana.mainloop()
    def nombre_columna(self):
        for fila in cursor.fetchall():
            for i in self.columna:
                if(i=='nombre'):
                    tk.Label(self.marco, text=fila[0]).pack()
    
nuevo = Mostrar()