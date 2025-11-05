from tkinter import *
from tkinter import ttk
Relleno = Tk()
texto1 = Label(Relleno, text="Mira que lindo que se acerca la primavera")
texto1.pack(fill=BOTH)
boton1 = Button(Relleno, text="Vamos a jugar")
boton1.pack(fill=BOTH)
boton2 = Button(Relleno, text="Horizontal")
boton3 = Button(Relleno, text="Horizontal")
boton3.pack()
boton2.pack(pady=10, padx=5)#separacion entre elementos
boton4 = Button(Relleno, text="Relleno interno",background="yellow")
boton4.pack(ipadx=50)
boton5 = Button(Relleno, text="Relleno interno", background="red")
boton5.pack(ipady=50)
boton6 = Button(Relleno, text="Boton gigante", background="black", fg="white")
boton6.pack(ipadx=50,ipady=50)
#Relleno en texto
texto2 = Label(Relleno,text="Este texto esta dentro de una caja mayor", bg="yellow", font=("Arial",25))
#texto2.config(font=("Arial",25))
texto2.pack(ipadx=50, ipady=50, pady=10)
Relleno.mainloop()