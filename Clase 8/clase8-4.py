#Para que esto funcione, que importamos tkinter como tk
import tkinter as tk
ventana = tk.Tk()
texto1 = tk.Label(ventana, text="Texto en nuestra aplicacion")
texto1.pack()
#Esto lo que venimos utilizando
#Se puede usar todo junto
texto2 = tk.Label(ventana, text="Otro texto en pantalla").pack()

#Vamos ver como integrar o colocar una imagen
imagen = tk.PhotoImage(file=r'C:\Users\JONATHAN\Documents\Poo - Python\Clase8\messi.gif')
#r'C:\Users\JONATHAN\Documents\Poo - Python\Clase8\messi.gif'
tk.Label(ventana, image=imagen).pack()
ventana.mainloop()