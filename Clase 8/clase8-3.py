from tkinter import *

ventana = Tk()
ventana.geometry("400x400")
#Deshabilitir o prohibir que el usuario redimensione la ventana
#ventana.resizable(False, True)
#Asi solo no va a poder modificar el tamaño de la ventana a lo ancho. Pero! si a lo alto
#Se puede restringir para que el usuario no modifique ni el ancho ni el alto
ventana.resizable(False, False)

#Configurar que una ventana tenga transparencia
#ventana.attributes("-alpha", 0.7)

#Configurar el fondo de la ventana
ventana.configure(background="#333")
ventana.mainloop()