"""
Intervención

Requisitos:
- Dentro de una empresa se vaa solicitar pedir el nombre y apelldio del empleado (input)
- Distrito de residencia ingresado por teclado
- Sueldo y cálculo del bono final de año, que será el triple del sueldo mensual menos el 10% del sueldo
- Todos estos datos se van a ingresar a un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal (output) el mensaje de: "'Nombre' 'Apellido',
recibirá 'bono' soles de fin de año"
"""

# Pedir datos
nombre = input("Nombre: ")
apellido = input("Apellido: ")
distrito = input("Distrito: ")
sueldo = float(input("Sueldo: "))

# Calcular bono
bono = (3 * sueldo) - (0.10 * sueldo)

# Guardar en diccionario
empleado = {"nombre": nombre, "apellido": apellido, "distrito": distrito, "bono": bono}

# Asignar a variables
nom, ape, bon = empleado["nombre"], empleado["apellido"], empleado["bono"]

# Mostrar resultado
print(f"{nom} {ape}, recibirá {bon:.2f} soles de fin de año")