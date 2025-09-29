"""Diccionarios en Python"""

"""
Los nombres de los Key(llaves) van a ir escritos siempre en minúsculas (por buenas prácticas)
"""

estudiante = {'nombre': "Gustavo", 'edad': 27, 'promedio': 18}

estudiante['distrito'] = "Miraflores"

del estudiante['edad']
del estudiante['promedio']

#Si no existe el key, el programa se cae o se crashea
#del estudiante['hobbie']

print("Diccionario actualizado: {}".format(estudiante))