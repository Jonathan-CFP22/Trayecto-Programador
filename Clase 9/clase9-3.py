from tkinter import *

total = ""
class Calculadora:
    boton7=0
    def __init__(self):
        ventana = Tk()
        self.display_value = StringVar()
        self.display_value.set("0")
        self.visor = Entry(ventana,textvariable=self.display_value ,state="readonly")
        self.visor.grid(row=0,column=0)
        boton7 = Button(ventana, text="7", command=lambda: self.boton("7")).grid(row=1,column=0)
        boton8 = Button(ventana, text="8", command=lambda: self.boton("8")).grid(row=1,column=1)
        boton9 = Button(ventana, text="9", command=lambda: self.boton("9")).grid(row=1,column=2)
        boton4 = Button(ventana, text="4", command=lambda: self.boton("4")).grid(row=2,column=0)
        boton5 = Button(ventana, text="5", command=lambda: self.boton("5")).grid(row=2,column=1)
        boton6 = Button(ventana, text="6", command=lambda: self.boton("6")).grid(row=2,column=2)
        boton1 = Button(ventana, text="1", command=lambda: self.boton("1")).grid(row=3,column=0)
        boton2 = Button(ventana, text="2", command=lambda: self.boton("2")).grid(row=3,column=1)
        boton3 = Button(ventana, text="3", command=lambda: self.boton("3")).grid(row=3,column=2)
        ventana.mainloop()
    def boton(self, valor):
        global total #estoy accediendo a la variable total que ya esta declarada de manera inicial antes de la clase
        total += valor
        print(valor)
        print(total)
        self.display_value.set(total)

nueva = Calculadora()