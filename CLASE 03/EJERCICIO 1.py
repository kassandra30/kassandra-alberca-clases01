"""Listas en python"""

"""
Listas,
len(): Obtener el tamaño de la lista en Python
append(): Agrega elementos en la lista
"""

paises = [] #inicio una lista vacía
print("Mi lista de países, contiene los valores: {}".format(paises))
print("Tamaño de la lista: {}".format(len(paises)))

"""Agregar datos a la lista"""
paises.append("Perú")
paises.append("España")
paises.append("Argentina")

print("Mi lista de países: {}".format(paises))

paises.append("Colombia")
print("Mi lista de países: {}".format(paises))

pais = paises[0]
print("El primer valor, elemento(0), de mi lista es: {}". format(pais))