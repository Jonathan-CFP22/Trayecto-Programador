import tkinter as tk
ventana = tk.Tk()
ventana.title("Ejemplo de Marcos")
ventana.geometry("600x600")

def Mostrar():
    Frame2.pack()
    Frame1.pack_forget()
#Creamos el Marco principal donde voy a armar la primer parte del programa
Frame1 = tk.Frame(ventana,bg="green",width=450,height=450)
Frame1.pack()
tk.Button(Frame1,text="Haz Clic", command=Mostrar).pack()

#Creamos el segundo marco
Frame2 = tk.Frame(ventana,bg="red",width=250,height=250)
Frame2.pack()
Frame2.pack_forget()
#Armar un texto que aparezca uno en el primer marco y el otro en el segundo
#tk.Label(Frame1, text="Este es el primer marco").pack()
#tk.Label(Frame2, text="Este es el segundo marco").pack()

ventana.mainloop()