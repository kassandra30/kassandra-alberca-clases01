"""Listas en Python"""

"""
Lista: Recorrido de las listas en un bucle for
"""

notas = [12, 18, 16, 20, 11, 14, 13]

i = 0
for nota in notas:
    print(notas[i])
    notas[i] = nota / 2
    print("Nota actualizada: {}".format(notas[i]))
    i = i + 1

 print(notas)
 notas = notas + [max(notas)+2, max(notas)+4]
 print(notas)