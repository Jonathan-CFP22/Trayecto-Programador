from tkinter import *
import mariadb

conexion = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
cursor = conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
cod_prod INT PRIMARY KEY NOT NULL,
nombre VARCHAR(255),
descripcion VARCHAR(255),
categoria VARCHAR(255),
precio DECIMAL
);""")

def ObtenerDatos():
    precio = ing_precio.get()
    precio_int = int(precio)
    cod = ing_cod_prod.get()
    nombre = ing_nombre.get()
    desc = ing_descripcion.get()
    categoria = ing_categoria.get()
    cursor.execute(f"INSERT INTO productos(cod_prod, nombre, descripcion, categoria, precio)VALUES('{cod}','{nombre}','{desc}','{categoria}','{precio_int}')")
    ventana.destroy()

ventana = Tk()
label_cod_prod = Label(ventana, text="Cod. Producto: ").grid(row=1, column=1)
ing_cod_prod = Entry(ventana)
ing_cod_prod.grid(row=1,column=2)
label_nombre = Label(ventana, text="Nombre: ").grid(row=2,column=1) 
ing_nombre = Entry(ventana)
ing_nombre.grid(row=2,column=2)
label_descripcion = Label(ventana, text="Descripción: ").grid(row=3,column=1)
ing_descripcion = Entry(ventana)
ing_descripcion.grid(row=3,column=2)
label_categoria = Label(ventana, text="Categoria: ").grid(row=4,column=1) 
ing_categoria = Entry(ventana)
ing_categoria.grid(row=4,column=2)
label_precio = Label(ventana, text="Precio: ").grid(row=5,column=1) 
ing_precio = Entry(ventana)
ing_precio.grid(row=5,column=2)
submit = Button(ventana, text="Agregar Producto", command=ObtenerDatos).grid(row=6,column=1)


ventana.mainloop()
conexion.commit()
cursor.close()
conexion.close()