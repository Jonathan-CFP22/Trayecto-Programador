#Generar la conexión a una base de datos mediante el gestor sql
#importar libreria para conectar la base de datos
import sqlite3
#conectar a la base de datos, para eso voy a generar una variable donde generamos la conexión
conectar = sqlite3.connect('python.db')
#Utilizamos un cursor que va a ser de intermediario para la conexi{on y las consultas sql que necesitamos elbarorar en nuestro archivo python}
referencia = conectar.cursor()
#de esta manera lo que tenemos es un cursor denominado referencia que servira de intermediario para cualquier consulta que necesitamos en nuestro archivo python
if(conectar==True):
    print("Conexión exitosa")
else:
    print("Intente volver a configurar para conectar")

#vamos a crear una tabla en la base de datos
referencia.execute('''
                CREATE TABLE IF NOT EXISTS usuarios(
                   id_usuario INT PRIMARY KEY,
                   nombre VARCHAR(255),
                   mail VARCHAR(255)
                   )''')
#para que se guarde necesitamos utilizar una función .commit() que va a guardar esta consulta que estamos generando 
#conectar.commit()

#Insertar dato
referencia.execute("INSERT INTO usuarios (nombre, mail) VALUES ('Juan','juan.perez@gmail.com')")
#tambien necesitamos guardar la accion
conectar.commit()

#execute seria la consulta sql a executar
consulta = referencia.execute("SELECT * FROM usuarios")
#No alcanza con hacer la consulta, necesitamos mostrarlo, para eso lo que vamos a hacer es recorrer todo los datos reciviso en esta consulta.
#Para esto, vamos a utilizar una funcion llamada fetchone(). Que lo que va a hacer es recorrer en bucle todos los datos almacenados en esa tabla, y mostrarlos por pantalla.
print(consulta.fetchone())
#para mostrar todos los datos almacenados en la tabla lo hacemos con la función llamada fetchall()
#print(consulta.fetchall())
#aca cerramos la conexi{on}
#si yo quiero que este resultado aparezca por cada linea lo recorremos con un for.
valores = consulta.fetchall()
for i in valores:
    print(f"{i}")
conectar.close()