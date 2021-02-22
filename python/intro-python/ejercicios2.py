# #Multiplicar 2 numero sin usar el simbolo de la multiplicacion

# a = 4
# b = 8
# resultado = 0

# for x in range(a):
#     resultado += b

# print (resultado)

# #Ingresar un nombre y un apellido e imprimirlo al rever

# nombre = 'Antonio'
# apellido = 'Linares'

# concatenar = nombre + ' ' + apellido

# print(concatenar[::-1])

# #escribir un funcion que encuentre el elemento menor de una lista

# lista = [10, 20, 66, 5, 100]

# menor = 'init'

# for x in lista:
#     if menor == 'init':
#         menor = x
#     else:
#         menor = x if x < menor else menor

# print ('El elemento menor es: ', menor)

# #escribir una funcion que devuelva el volumen de una esfera por un radio 
# #4/3 * pi * r ** 3
# def calcularVolumen(r):
#     return 4 / 3 * 3.14 * r ** 3

# resultado = calcularVolumen(6)
# print (resultado)
    
# #escribir un funcion que indique si el usuario es mayor de edad

# def esMayor(usuario):
#     return usuario.edad > 17

# class Usuario:
#     def __init__(self, edad):
#         self.edad = edad

# usuario = Usuario(15)
# usuario2 = Usuario(21)

# resultado1 = esMayor(usuario)
# resultado2 = esMayor(usuario2)

# print (resultado1,resultado2)

# #Escribir una funcion que indique que numero es par o impar

# def esPar(n):
#     return n % 2 == 0

# resultado = esPar(11)
# print (resultado)

# #escribir una funcion que indique cuantas vocales tiene una palabra

# palabra = 'ChAnchitoFeliz'

# vocales = 0

# for x in palabra:
#     y = x.lower()
#     vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

# print (vocales)


# #escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta luego devuelva la suma de los numeros ingresado

# lista = []
# print ('Ingrese numero y para salir diga basta')
# while True:
#     valor = input('Ingrese un numero: ')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print ('Dato invalido')
#             exit()

# resultado = 0

# for x in lista:
#     resultado += x

# print (resultado)


#escribir un funcion que reciba nombre y apellido y los vaya agrengando a un archivo  

def agregaNombreAArchivo(nombre, apellido):
    c = open('Agregar.txt', 'a')
    c.write (nombre + " " + apellido+ "\n")
    
    c.close

    agregaNombreAArchivo('Antonio', 'Linares')