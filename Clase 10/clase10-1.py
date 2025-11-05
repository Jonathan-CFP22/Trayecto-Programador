from tkinter import *
#Calculadora 1.0
ventana = Tk()

"""Configuro el peso de los grid"""
#Esta parte para las filas
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)

#Esto parte es para las columnas
for i in range(6):
    ventana.grid_columnconfigure(i, weight=1)

#Variable donde voy a guardar el primer numero ingresado por el usuario en el visor
numero1 = 0
#Variable donde almacenar la operacion a realizar por el usuario
op = ""
#Vamos a pertir en esta variable display value el ingreso de cadena de caracteres
display_value = StringVar()
#Arrancamos el display en 0
display_value.set("")

#visor de la calculadora
visor = Entry(ventana, textvariable=display_value ,state="readonly")
visor.grid(column=0,row=0, columnspan=4)

#Funcion para agregar los botones presionados por el usuario al visor
def presionado(valor_ingresado):
    display_value.set(display_value.get()+valor_ingresado)

#Función para las distintas operaciones
def operacion(operacion_ingresada):
    #guardar lo que el usuario ingreso por display en la variable numero1
    global numero1
    numero1 = int(display_value.get())
    global op
    op = operacion_ingresada
    display_value.set(display_value.get()+operacion_ingresada)
    #limpio la pantalla, es decir la vuelvo a poner en 0
    display_value.set("")

#Funcion para calcular resultado
def resultado():
    if (op=="+"):
        resultado=numero1+int(display_value.get())
        display_value.set("")
        display_value.set(resultado)
    elif (op=="-"):
        resultado=numero1-int(display_value.get())
        display_value.set("")
        display_value.set(resultado)
    elif (op=="*"):
        resultado=numero1*int(display_value.get())
        display_value.set("")
        display_value.set(resultado)
    elif (op=="/"):
        if(int(display_value.get==0)):
            display_value.set("ERROR")
        else:
            resultado=numero1-int(display_value.get())
            display_value.set("")
            display_value.set(resultado)
        


#Botones de los números

boton1 = Button(ventana, text="1", command=lambda: presionado("1")).grid(row=3,column=0)
boton2 = Button(ventana, text="2", command=lambda: presionado("2")).grid(row=3,column=1)
boton3 = Button(ventana, text="3", command=lambda: presionado("3")).grid(row=3,column=2)
boton4 = Button(ventana, text="4", command=lambda: presionado("4")).grid(row=2,column=0)
boton5 = Button(ventana, text="5", command=lambda: presionado("5")).grid(row=2,column=1)
boton6 = Button(ventana, text="6", command=lambda: presionado("6")).grid(row=2,column=2)
boton7 = Button(ventana, text="7", command=lambda: presionado("7")).grid(row=1,column=0)
boton8 = Button(ventana, text="8", command=lambda: presionado("8")).grid(row=1,column=1)
boton9 = Button(ventana, text="9", command=lambda: presionado("9")).grid(row=1,column=2)

#Botones de opreaciones
boton_suma = Button(ventana, text="+", command=lambda: operacion("+")).grid(row=1,column=3)
boton_resta = Button(ventana, text="-", command=lambda: operacion("-")).grid(row=2,column=3)
boton_multiplicacion = Button(ventana, text="*", command=lambda: operacion("*")).grid(row=3,column=3)
boton_division = Button(ventana, text="/", command=lambda: operacion("/")).grid(row=4,column=3)

#Boton igual
boton_igual = Button(ventana, text="=", command=resultado).grid(row=4,column=2)
ventana.mainloop()