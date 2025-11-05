import tkinter as tk
from tkinter import font

def ventanabase(titulo="Ejemplo",dimensiones="800x800",color="blue"):
    ventana = tk.Tk()
    ventana.title(titulo)
    ventana.geometry(dimensiones)
    ventana.configure(background=color)
    tipografia=font.Font(family="Times New Roman", size=14, weight="normal")
    abrir_ventana = tk.Button(ventana,text="Abrir otra ventana", command=ventanasecundaria).pack()
    ventana.mainloop()

def ventanasecundaria():
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana emergente")

ventanabase("Login")