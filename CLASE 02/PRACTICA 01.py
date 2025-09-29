# 1. Crea 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string
entero1 = 42
entero2 = 6

flotante1 = 2.5
flotante2 = 1.1

string1 = "Kassandra"
string2 = "Alberca"

string_num = "9"   # string con valor numérico
booleano = True

# 2. Suma de una variable entera con la variable string numérica
# Necesitamos convertir string_num a entero
suma1 = entero1 + int(string_num)
print("Suma de entero1 + string_num:", suma1)

# 3. Suma de las 2 variables enteras + string numérica + una variable flotante
suma2 = entero1 + entero2 + int(string_num) + flotante1
print("Suma de enteros + string_num + flotante1:", suma2)

# 4. Módulo de las variables enteras
modulo = entero1 % entero2
print("Módulo (entero1 % entero2):", modulo)

# 5. Parte entera de la división de las variables enteras
division_entera = entero1 // entero2
print("División entera (entero1 // entero2):", division_entera)

# 6. Potencia usando una variable flotante y la variable entera como exponente
potencia = flotante1 ** entero2
print("Potencia (flotante1 ** entero2):", potencia)

# Mostrar strings y boolean para comprobar que existen
print("string1:", string1)
print("string2:", string2)
print("Booleano:",booleano)
