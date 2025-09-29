"""
Lista de python - Participacion
"""
"""
Requisitos:
-Crear dos listas vacias
- Agregar los datos de nombre, apellido paterno y profesion para ambas listas
-Obtener y mosotrar la suma de las edades de ambas listas
-Sumar las listas y mostrar el resultado en la terminal
-Mostrar de forma inversa la suma de ambas listas
-Actualizar la nueva lista eliminando la edad de la primera y el apellido del segundo
(actualizar cualquiera de los metodos de eliminación)
-Actualizar la profesion del segundo usuario
"""

lista1 = []
lista2 = []

# Datos lista1
lista1.append("Kassandra")
lista1.append("Alberca")
lista1.append(24)
lista1.append("Ingeniera")

# Datos lista2
lista2.append("Nicol")
lista2.append("Carmen")
lista2.append(25)
lista2.append("Abogada")

# Sumar listas
suma_lista = lista1 + lista2
print(suma_lista)

# Mostrar lista inversa
suma_lista.reverse()
print(suma_lista)

# Eliminar la edad de lista1 y el apellido de lista2
suma_lista.remove(24)
suma_lista.remove("Carmen")
print(suma_lista)

# Actualizar profesión del segundo usuario
suma_lista[0] = "Doctora"
print(suma_lista)