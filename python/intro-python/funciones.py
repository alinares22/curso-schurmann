def miFuncion():
    print ('Mi primera funcion!')

#miFuncion()

def imprimeDato(*nombre):
    print ('Mi nombre completo es:', nombre[0])

#imprimeDato('chanchito', 'feliz', 'Pedro', 'Pablo')

def nombreCompleto(apellido, nombre):
    print (nombre, apellido)

#nombreCompleto(nombre='Chanchito', apellido='Feliz')

def nombreCompleto2(**kwargs):
    print (kwargs['nombre'], kwargs['apellido'])

#nombreCompleto2(nombre='Pedro', apellido='feliz')

def miFuncion2(argunmento= 'chanchito'):
    print (argunmento)

# miFuncion2('Batman')
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

#miFuncionLista(['chanchito', 'feliz'])


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i    
        
# nombres = concatenaNombres(['chanchito', 'feliz'])
# print (nombres)

def recursion(i):
    if (i < 1):
        return i
    print (i)
    recursion(i - 1)

recursion(6)
