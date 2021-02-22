import modulos as xs
from camelcase import CamelCase

print (xs.mascotas)
xs.saludo('Antonio')

c = CamelCase() 
s = 'Esta oracion necesita CamelCase'

camelcased = c.hump(s)
print (camelcased)