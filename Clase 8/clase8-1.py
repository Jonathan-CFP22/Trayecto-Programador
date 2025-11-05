from tkinter import *
from tkinter import ttk

Main = Tk()
Main.geometry("600x600")
#Texto con color de fondo
texto_bg = Label(Main, text="Texto con color de fondo", bg="pink")
texto_bg.pack()
#Texto con color solo al texto
texto_color = Label(Main, text="Texto colorido", fg="blue")
texto_color.pack()
#Texto fusionado
texto_fusion = Label(Main, text="Texto divertido", bg="#c3ad21", fg="#fff")
texto_fusion.pack()
#Tamaño de la fuente y la fuente
texto_grande = Label(Main, text="Texto grande", font=('Arial',40))
texto_grande.pack()
Main.mainloop()