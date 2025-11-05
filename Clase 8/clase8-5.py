from tkinter import *

ventana = Tk()
"""Para que esto funcione se tiene que asignar a cada columna el peso, es decir el espacio que va a ocupar cada uno de los elementos que se encuentran en las columnas o filas dependiendo, en este caso las columnas"""
for i in range(0,6):
    ventana.columnconfigure(i, weight=1)

texto1 = Label(ventana, text="Primer texto", bg="blue")
texto1.grid(row=0, column=0)
texto2 = Label(ventana, text="Texto muy pero muy extenso", bg="yellow")
texto2.grid(row=1,column=0)
texto3 = Label(ventana, text="Tercer texto",bg="red")
texto3.grid(row=0, column=1)
boton = Button(ventana, text="",width=20).grid(row=0,column=2)
texto4 = Label(ventana, text="Texto").grid(row=0,column=3)
boton6 = Button(ventana, text="",width=20).grid(row=0,column=6)
texto5 = Label(ventana, text="Hola").grid(row=0,column=5)
#Tomar varias columnas al mismo tiempo
#texto6 = Button(ventana, text="Pablo 3.1", background="blue").grid(row=1,column=2,columnspan=3)
#Hacemos que el boton se expanda
texto6 = Button(ventana, text="Pablo 3.1", background="blue").grid(row=2,column=0,columnspan=3, sticky="ew")#sticky - Pegar o fijar (e - este) - W (oeste). de izquierda a derecha
ventana.mainloop()