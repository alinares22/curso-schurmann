class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print ('Hola mi nombres es ', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print ('Hola, me llamo ',self.nombre, 'y soy Administrador')

# usuario = Usuario('Antonio', 'Linares')

# usuario.saludo()
# usuario.nombre = 'Pedro'
# usuario.saludo()
# # del usuario.nombre
# # del usuario
# # print (usuario)

# admin = Admin('Super', 'Feliz')
# admin.saludo()
# admin.superSaludo()

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print ('Hola soy un', self.tipo,'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo ='gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print ('Hola, soy un gato extendido!')

class Perro(Animal):
    tipo = 'perro'  
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print ('Instanciando un perro')

class Canario(Animal):
    tipo = 'Canario'  
gato = Gato('fluffy', 'maullido')
gato.saludo()
perro = Perro('Firulais', 'ladrido')
perro.saludo()
canario = Canario('Piolin', 'silvido')
canario.saludo()