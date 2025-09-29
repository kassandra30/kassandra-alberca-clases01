"""- Crear una función que multiplicará 4 valores (int y floats)
- La función tendrá un parámetro o que contendrá un valor
- Mostrar 2 casos donde ese ingresó los valores donde uno no afectará el valor del parámetro
que ya contiene un valor y otro donde si lo estará afectando"""

def multiplicar(a, b, c, d, o):
    resultado = a * b * c * d
    print("Multiplicación:", resultado)
    print("Parámetro o:", o)


# Caso 1: 'o' no es afectado
multiplicar(2, 3, 1.5, 2, 100)

# Caso 2: 'o' afectado (se multiplica con el resultado)
def multiplicar_afectando(a, b, c, d, o):
    resultado = a * b * c * d * o
    print("Multiplicación afectando o:", resultado)


multiplicar_afectando(2, 3, 1.5, 2, 100)