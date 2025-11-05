import tkinter as tk

class Login:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Logeo")
        self.txtnom=tk.Label(self.ventana,text="Nombre:")
        self.txtnom.grid(row=1, column=1)
        self.ingnom=tk.Entry(self.ventana)
        self.ingnom.grid(row=1,column=2)
        self.txtpass=tk.Label(self.ventana,text="Contraseña:")
        self.txtpass.grid(row=2, column=1)
        self.ingpass=tk.Entry(self.ventana)
        self.ingpass.grid(row=2,column=2)
        self.btning=tk.Button(self.ventana,text="Ingresar",command=self.Ingreso)
        self.btning.grid(row=3,column=1)
        self.ventana.mainloop()
    def Ingreso(self):
        self.nomusuario=self.ingnom.get()
        self.txtnom.grid_remove()
        self.ingnom.grid_remove()
        self.btning.grid_remove()
        self.txtpass.grid_remove()
        self.ingpass.grid_remove()
        self.MuestraUsuario()
    def MuestraUsuario(self):
        self.usuario=tk.Label(self.ventana,text=self.nomusuario)
        self.usuario.grid(row=1,column=1)
app = Login()