# Aca va un comentario
#if 3 > 5:
    #print ('Esto no se va a imprimir')


#if 5 > 3: # Aca va otro comentario
    #print ('5 es mayor q 3')


x = 5
y = 'chanchito feliz'

#print (x, y)

email = 'chanchito@feliz.com'

#print (email)

mi_var = 'chanchito'
miVar ='chanchito'

a,b,c = 'lala', 'lele', 'lili'

#print (a, b, c)

valor1 = valor2 = valor3 = 'chanchito Feliz'

#print (valor1, valor2, valor3)

inicio = 'Hola '
final = 'mundo'

#print (inicio + final)

palabra = 'Hola mundo' #String
oracion = "Hola mundo, comilla dobles" #String

entero = 20 #Integer
condecimales = 20.2 #Float
complejo = 1j

#print (palabra, oracion, entero, condecimales, complejo)


lista = ['Hola', 'Mundo', 'Chanchito Feliz']
lista2 = lista.copy()
lista.append ('Chanchito Triste')
#lista.clear ()

#print (lista, lista2.count(3))
#print (len(lista), len(lista2))

largoLista= len(lista)
largoLista2= len(lista2)

#print (largoLista, largoLista2)

#print (lista[2])

#lista.pop() #Este elimina el ultimo elemento de lista
#lista.remove('Hola') #Este elimina un elemento por su valor

lista.reverse()
lista.sort()

tupla = ('Hola', 'Mundo', 'somos', 'tupla')
listaDetupla = list(tupla)
listaDetupla.append('Chanchito')
#print (listaDetupla)

rango = range(6)
#print (rango)

diccionario = {
    'nombre':'chanchito feliz', 
    'raza':'persa',
    'edad': 5
}

#print (diccionario)
#print (diccionario['nombre'])
#print (diccionario['raza'])
#print (diccionario.get('nombre'))
diccionario['nombre'] = 'Fluffy'

#print (len(diccionario))

diccionario['ronronea'] = 'si'

#print (diccionario)

#diccionario.pop('ronronea')
#diccionario.popitem()
#copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)
#del diccionario['ronronea']
diccionario.clear()
#print (diccionario, copiaGatito)

fluffy = {
    'nombre':'Fluffy',
    'edad':4,
}

mamba = {
    'nombre': 'Black Mamba',
    'edad':12
}

gatitos = {
    'Fluffy': fluffy,
    'Mamba': mamba
}

#print (gatitos)

#perritos = dict(nombre='Chanchito Feliz',edad=6)

#print (perritos)

verdadero = True
falso = False

print (verdadero, falso)