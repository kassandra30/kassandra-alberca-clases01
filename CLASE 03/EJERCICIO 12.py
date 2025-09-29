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

Lista_1 = []
Lista_2 = []

Lista_1.append("KASSANDRA")
Lista_1.append("ALBERCA")
Lista_1.append(24)
Lista_1.append("INGENIERA")
Lista_2.append("NICOL")
Lista_2.append("CARMEN")
Lista_2.append(25)
Lista_2.append("QUIMICA")

suma_lista = Lista_1 + Lista_2
print(suma_lista)

suma_lista.reverse()
print("Lista :", suma_lista)

suma_lista.remove(24)
suma_lista.remove("CARMEN")

print("Lista :", suma_lista)

