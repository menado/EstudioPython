# Condicionales 
# if 5 > 3: 
#     print('5 es mayor que 3') 

# if 3 > 5: 
#     print('Esto no se va a cumplir') 

x = 5
y = 'Chanchito Feliz'

# print(x, y)

email = 'chanchito@feliz.com'

# print(email)

miVar = 'Chanchito'
mi_var = 'Chanchito2'
_mi_var = 'Chanchito3'
MIVAR = 'Chanchito4'

a, b, c = 'Lala', 'Lele', 'Lili'
# print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'
# print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'Mundo'

# print(f'{inicio} {final}')
# print(inicio + ' ' + final)

palabra = 'Hola Mundo' # string
oracion = "Hola Mundo con Comillas Dobles" # string
entero = 20 # integer
conDecimal = 20.2 # float
complejo = 1j # complex

# print(palabra, oracion, entero, conDecimal, complejo)

lista = [1, 2, 3]
lista2 = lista.copy()
# lista.append(4) # Añade un elemento nuevo.
# lista.clear() # Limpia los datos de la lista. 

# print(lista, lista2.count(4)) # "count" nos indica la cantidad de elementos iguales dentro de la lista.
# print(len(lista), len(lista2)) # "len" cuenta los elementos dentro de la lista.

largoLista = len(lista)
largoLista2 = len(lista2)
# print(largoLista, largoLista2)

# print(lista[0])

lista.pop() # "pop" elimina el último elemento de la lista.
lista.remove(1) # Array.remove(elementoQueDeseamosEliminar) elimina el elemento según su valor. 
lista.reverse() # Ordena la lista inversamente. 
lista.sort() # Ordena de mayor a menor, si son del mismo tipo de dato. 
# print(lista)

tupla = ('Hola', 'Mundo', 'Somos', 'Tupla') # La tupla a diferencia de la lista, no puede ser modificada.
listaDeTupla = list(tupla)
# print(tupla.index('Mundo')) # Indica en que indice se encuentra el elemento. 

listaDeTupla.append('Chanchito')
# print(listaDeTupla)

rango = range(6)
# print(rango)

diccionario = {
    "nombre": "Chanchito Feliz",
    "raza": "Persa",
    "edad": 5
}

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])

# print(diccionario.get('nombre'))
# print(diccionario.get('raza'))
# print(diccionario.get('edad'))

diccionario['nombre'] = 'Fluffy'
# print(diccionario)
# print(len(diccionario))

diccionario['ronronea'] = 'si'
# print(diccionario)

# diccionario.popitem() # Elimina el último valor del diccionario.
# diccionario.pop('ronronea') # Elimina un valor del diccionario.
del diccionario['ronronea'] # Elimina un valor del diccionario.

# copiaDiccionario = diccionario.copy() # Crea una copia del diccionario.
copiaDiccionario = dict(diccionario)
# print(diccionario, copiaDiccionario)

diccionario.clear()
# print(diccionario, copiaDiccionario)

fluffy = {
    "nombre": "Fluffy",
    "edad": 4 
}

manba = {
    "nombre": "Black Manba",
    "edad": 12
}
gatitos = {
    "Fluffy": fluffy,
    "Manba": manba
}

# print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6)
# print(perritos)

verdadero = True
falso = False

print(verdadero, falso)