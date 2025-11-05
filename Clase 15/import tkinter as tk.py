import tkinter as tk
class Login:
    def __init__(self):
        self.ventana = tk.Tk()
        self.menu = tk.Menu()
        self.menu_archivo = tk.Menu(self.menu, tearoff=False)
        self.frameusuario = tk.Frame(width=200,height=200)
        self.frameregistro = tk.Frame(width=200,height=400)
        self.menu_archivo.add_command(
            label="Nuevo",
            accelerator="Ctrl+N",
            command=self.nuevo_archivo
        )
        self.menu.add_cascade(menu=self.menu_archivo, label="Archivo")
        self.ventana.config(menu=self.menu)
        self.ventana.mainloop()
    def nuevo_archivo(self):
        print("hola")

nuevo = Login()