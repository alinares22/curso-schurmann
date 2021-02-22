import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='antonio',
    password='alinares22',
    database='prueba'
)

cursor = midb.cursor()

# Lista de datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

cursor.execute('select * from Usuario limit 2')
resultado = cursor.fetchall()
print(resultado)

# ver definiciones de las tablas
# cursor.execute ('show create table Usuario')

#Insertar Datos
# sql = 'insert into Usuario(email, username, edad) values (%s, %s, %s)'
# values = ('micorreo@correo.com', 'nombreusuario', 45)

#Acutalizar datos
# sql = 'update Usuario set email = %s where id = %s'
# values = ('antonio@correo.com', 4)
# cursor.execute (sql, values)


# midb.commit()

# print (cursor.rowcount)

#eliminar Datos
# sql = 'delete from Usuario where id = %s'
# values =  (4,)
# cursor.execute(sql, values)
# midb.commit()   