from tkinter import *
from tkinter import ttk
def Cierre():
    ventana.destroy()

def Minimiza():
    ventana.iconify()#minimizar ventana
    #ventana.state('iconic')Otra forma

def restaura_maximiza():
    #comprobar el estado de la ventana
    if (ventana.state()== 'zoomed'):#Comprobamos si esta maximizado
        ventana.state('normal')#restaurarla a su forma normal
    else:
        ventana.state('zoomed')#Lo pasa a maximizar

ventana = Tk()
cerrar = Button(ventana, text="X", command=Cierre)
minimizar = Button(ventana, text="-", command=Minimiza)
restaurar = Button(ventana, text="✊", command=restaura_maximiza)
cerrar.pack()
minimizar.pack()
restaurar.pack()
ventana.mainloop()