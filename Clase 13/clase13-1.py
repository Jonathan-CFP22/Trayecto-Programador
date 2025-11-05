import mysql.connector
import socket

#Configurar la conexión a una base de datos que utilice SQL
hostname = mysql.connector.connect(
    host=socket.getaddrinfo('sql.infinityfree.com', 3306), #Nombre del servidor de la base de datos o ip
    user="if0_40115888", #Usuario del servidor de la base de datos
    password="qweASD36741506", #Contraseña del usuario
    database="if0_40115888_python" #Base de daos que queremos conectar
)
secuencia = hostname.cursor()#Asignamos un cursor a una variable que nos va a servir de intermediario para realizar cualquier consulta sql
secuencia.execute("CREATE TABLE users(id INTEGER AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), mail Varchar(255), passwd Varchar(255));")
hostname.commit()#Esto es para guardar
secuencia.close()#Esto es para cerrar el cursor
hostname.close()# Cerramos la conexión