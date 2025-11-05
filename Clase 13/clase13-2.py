import mariadb

#Configurar la conexión a una base de datos que utilice SQL
hostname = mariadb.connect(
    host="localhost", #Nombre del servidor de la base de datos o ip
    user="root", #Usuario del servidor de la base de datos
    password="", #Contraseña del usuario
    database="python" #Base de daos que queremos conectar
)
secuencia = hostname.cursor()#Asignamos un cursor a una variable que nos va a servir de intermediario para realizar cualquier consulta sql
secuencia.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), mail Varchar(255), passwd Varchar(255));")
#hostname.commit()#Esto es para guardar
nombre = input("Ingrese un nombre: ")
mail = input("Ingrese el mail: ")
pwd = input("Ingrese una contraseña: ")
#Insertar un dato en la tabla
secuencia.execute(f"INSERT INTO usuarios(nombre, mail, passwd)VALUES('{nombre}','{mail}','{pwd}')")
hostname.commit()
secuencia.execute("SELECT * FROM usuarios")
mostrar = secuencia.fetchall()
for z in mostrar:
    print(z)
secuencia.close()#Esto es para cerrar el cursor
hostname.close()# Cerramos la conexión