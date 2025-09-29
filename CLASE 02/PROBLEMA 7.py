#PROBLEMA 07
#De 3 números asignados mayores a 30 (entre positivos y negativos tú los propones) a 3 variables,
# se pide hallar la suma de los valores de los módulos
# con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la suma.
numero_1 = 56
numero_2 = 39
numero_3 = -98
suma_modulos = (numero_1 % 3) + (numero_2 % 5) + (numero_3 % 7)
print("La suma de los valores de los módulos es:", suma_modulos)