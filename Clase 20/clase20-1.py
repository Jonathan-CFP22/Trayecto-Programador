from tkinter import *
nombres = ["Juan","Pedro","Abril","Josefina","Martina","Viviana","Marta","Nohelia","Nahiara","Alejandra"]
ventana = Tk()
ventana.geometry("800x200")
Label(ventana,text="Bienvenidos a Pablo 2.1").grid(row=1,column=1)
#Recuadro para que aparezcan los items o elementos que queres visualizar
barra_deslizante = Listbox()
barra_deslizante.insert(END, *(f"Item N° {i}" for i in nombres))
barra_deslizante.place(x=50,y=0,height=100)

#Barra desplazadora
barra = Scrollbar(orient=VERTICAL, command=barra_deslizante.yview)
barra.set(0.1,0.5)
barra.place(x=170,y=0,height=100)
ventana.mainloop()