import tkinter as tk
def imprimir_nombre(evento=None):
    print("Pablo")
class Menu:
    def __init__(self):
        ventana = tk.Tk()
        ventana.title("Menú en tkinter")
        menu = tk.Menu()
        menu_archivo = tk.Menu(menu, tearoff=False)#el tearofff sirve para desactivar o activar una opción o un elemento del menu. es decir que si yo lo establezco como false( lo que hago es deshabilitiar que se separa el menu), es decir que flote en cualquier lado de la ventana. Quede en un lugar fijo.
        menu_editar =tk.Menu(menu, tearoff=False)
        menu_archivo.add_command(
            label="Nuevo Archivo",
            accelerator="CTRL+N",
            command=imprimir_nombre
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Guardar",
            accelerator="CTRL+S",
            command=imprimir_nombre
        )
        menu_editar.add_command(
            label="Guardar",
            accelerator="CTRL+S",
            command=imprimir_nombre
        )
        ventana.bind_all("<Control-n>", imprimir_nombre)
        ventana.bind_all("<Control-s>", imprimir_nombre)
        menu.add_cascade(menu=menu_archivo, label="File")
        menu.add_cascade(menu=menu_editar, label="Editar")
        tk.Label(ventana, text="Vamos a bailar").pack()
        ventana.config(menu=menu)#Aca establezco el menu para la ventana
        ventana.mainloop()

nuevo = Menu()