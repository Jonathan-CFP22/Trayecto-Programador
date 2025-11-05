from tkinter import *
usuarios = []
usuarios.append(["marina"])
usuarios.append(["321"])
global nueva_ventana
def login():
    nom = ingresa_nombre.get()
    for i in usuarios:
        for j in i:
            print(j)
            if(nom==j):
                """texto_nombre.grid_remove
                ingresa_nombre.destroy()
                #destroy es un metodo que permite eliminar cualquier widget siempre y cuando no utilice o no tenga .place o .grid
                texto_pwd.grid_remove
                #Para widgets que utilizan .grid existe grid_remove()
                ingresa_pwd.pack_forget()
                #pack forget que sea invisible"""
                #Ahora rompemos la ventana actual
                ventana.destroy()
                #para esta situación es mas eficar destruir la ventana actual y generar otra
                texto_ok=Label(nueva_ventana, text="Has logeado").grid(row=1,column=1)
            else:
                ventana.destroy()
                
                nueva_ventana = Tk()
                texto_err=Label(nueva_ventana, text="El usuario no está registrado").grid(row=1,column=1)
                btn_reg = Button(nueva_ventana,text="Register", command=register).grid(row=1,column=2)

def register():
    
    nueva_ventana.destroy()
    ventana_reg = Tk()
    texto_nombre = Label(ventana_reg, text="Nombre de usuario: ").grid(row=1,column=1)
    ingresa_nombre = Entry(ventana_reg)
    ingresa_nombre.grid(row=1,column=2)
    texto_pwd = Label(ventana_reg, text="Ingresa contraseña: ").grid(row=2, column=1)
    ingresa_pwd = Entry(ventana_reg)
    ingresa_pwd.grid(row=2,column=2)
    btn_ing = Button(ventana_reg,text="Login", command=login).grid(row=3,column=2)
    btn_reg = Button(ventana_reg,text="Register", command=register).grid(row=3,column=1)

#Vamos a armar un login
ventana = Tk()
texto_nombre = Label(ventana, text="Nombre de usuario: ").grid(row=1,column=1)
ingresa_nombre = Entry(ventana)
ingresa_nombre.grid(row=1,column=2)
texto_pwd = Label(ventana, text="Ingresa contraseña: ").grid(row=2, column=1)
ingresa_pwd = Entry(ventana)
ingresa_pwd.grid(row=2,column=2)
btn_ing = Button(ventana,text="Login", command=login).grid(row=3,column=2)

ventana.mainloop()