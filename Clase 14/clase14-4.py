import tkinter as tk
class Login:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Login")
        self.MarcoPrincipal()
        self.ventana.mainloop()
    def MarcoPrincipal(self):
        self.marcologin=tk.Frame(self.ventana, width=300, height=300)
        self.marcologin.pack()
        tk.Label(self.marcologin, text="Ingrese nombre:").grid(row=1, column=1)
        self.ingnom=tk.Entry(self.marcologin)
        self.ingnom.grid(row=1,column=2)
        tk.Label(self.marcologin, text="Ingrese contraseña:").grid(row=2, column=1)
        self.ingpass=tk.Entry(self.marcologin)
        self.ingpass.grid(row=2,column=2)
        tk.Button(self.marcologin, text="Logear", command=self.MarcoSecundario).grid(row=3, column=1)
        tk.Button(self.marcologin, text="Registrarse", command=self.MarcoTerciario).grid(row=3, column=2)
    def MarcoSecundario(self):
        self.marcologin.pack_forget()
        self.marcologeado = tk.Frame(self.ventana, width=200, height=200)
        self.marcologeado.pack()
        tk.Label(self.marcologeado, text="Logeado correctamente").pack()
    def MarcoTerciario(self):
        self.marcologin.pack_forget()
        self.marcoregistrar = tk.Frame(self.ventana, width=200, height=200)
        self.marcoregistrar.pack()
        tk.Label(self.marcoregistrar, text="Logeado correctamente").pack()

nuevo = Login()