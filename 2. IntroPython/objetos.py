# class Usuario:
#     nombre = "Felipe"
#     apellido = "Feliz"

# usuario = Usuario
# usuario = Usuario()

# print(usuario.nombre, usuario.apellido)

class Usuario: 
    def __init__ (self, nombre, apellido): # Constructor - Self va a ser la referencia del objeto instanciado.
        self.nombre = nombre
        self.apellido = apellido

    def imprimirNombre(self):
        print(self.nombre, self.apellido)

usuario = Usuario('Juan', 'Mena')
usuario2 = Usuario('Paula', 'Mena')

# usuario.imprimirNombre()
# usuario2.imprimirNombre()

usuario.nombre = 'Juan el Crack'

# usuario.imprimirNombre()

del usuario.nombre # Eliminamos el valor de una propiedad de la instancia.
# usuario.imprimirNombre()

del usuario
# print(usuario)

class Admin(Usuario):
    def superSaludo(self):
        print(f'Hola, me llamo: {self.nombre} y soy administrador')

admin = Admin('Super', 'Administrador')

# admin.superSaludo()


class Animal():
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print(f'Hola soy un {self.tipo} y mi sonido es el {self.onomatopeya}.')


class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola soy un gato extendido...')
    
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro...')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()

