import tkinter as tk
import mariadb

hostname = mariadb.connect(host="localhost", user="root", password="",database="python")
cursor = hostname.cursor()
cursor.execute("SELECT id FROM usuarios")
id = cursor.fetchall()
cursor.execute("SELECT nombre FROM usuarios")
nombre = cursor.fetchall()
cursor.execute("SELECT mail FROM usuarios")
mail = cursor.fetchall()
#print(seleccion)
class Mostrar:
    def __init__(self):
        self.ventana=tk.Tk()
        self.marco=tk.Frame(self.ventana, width=200,height=200)
        self.marco.pack()
        
        for i in id:
            tk.Label(self.marco, text=i).pack()
        for i in mail:
            tk.Label(self.marco, text=i).pack()
        for i in nombre:
            tk.Label(self.marco, text=i).pack()
        self.ventana.mainloop()
nuevo = Mostrar()