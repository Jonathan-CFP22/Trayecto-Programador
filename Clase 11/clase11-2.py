import tkinter as tk
#La priemr linea define una nueva clase llamada login. Que va a heredar, es decir no es un objeto principal, si no que hereda los widgets o los distintos atributos y metodos definidos en la clase tk.Frame
class Login(tk.Frame):
    #Constructor que self, hace referencia a la clase que estamos utilizando. Por otro lado principal hara de intermediario entre nuestra clase y la que heredemos (tk.Frame)
    def __init__(self, principal):
        #Esta linea es crucial, ya que, lo que hacemos es primero llamar al constructor que existe en la clase tk.frame, adem{as le mandamos el parametro que utilizams de intermediario.}
        super().__init__(principal)
        #Acivamos la visualizacion del frame, es decir el contenido en nuestra ventana principal
        self.pack()
        texto_nombre = tk.Label(self, text="Ingrese nombre de usuario: ").grid(row=1,column=1)
        ingreso_nombre = tk.Entry(self, text="Ingrese nombre de usuario: ")
        ingreso_nombre.grid(row=1,column=2)
        texto_pwd = tk.Label(self, text="Ingrese nombre de usuario: ").grid(row=2,column=1)
        ingreso_pwd = tk.Entry(self, text="Ingrese nombre de usuario: ")
        ingreso_pwd.grid(row=2,column=2)
        login = tk.Button(self, text="Login").grid(row=3,column=1)


#Esta ultima parte preparar el funcionamiento de nuestra aplicacion
#la primer linea creamos la ventana principal de la aplicacion, donde iran todos los elementos
ventana = tk.Tk()
#la segunda linea se va a generar la instancia a la clase que armamos para el contenido que se debe mostrar en la venta.
main = Login(ventana)
#la tercera linea perimitira la ejecuccion e inicia el bucle principal de eventos.
main.mainloop()