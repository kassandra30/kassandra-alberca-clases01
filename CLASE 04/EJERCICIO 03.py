"""Diccionarios en Python"""

"""
Sorted: obtener los nombres de los keys de un diccionario
"""



base_datos= {"nombre": "Mysql", "tipo": "80 relacional", "gestor_bd": "norkbench"}

keys = sorted(base_datos)
print(base_datos)

print(keys)

base_datos_keys = list(base_datos.keys())
print("keys: {}" .format(base_datos_keys))

