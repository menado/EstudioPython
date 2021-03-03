from modulos import saludo, mascotas
from camelcase import CamelCase

saludo(mascotas[0])

c = CamelCase()
s = 'esta oración necesita CamelCase'

print(c.hump(s))

