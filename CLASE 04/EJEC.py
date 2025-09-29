
"""Diccionarios en Python"""

"""
Participación:

- Crear diccionario de contactos, el cual tendrá como key: Nombre, value: teléfono (9 dígitos)
- Verificar si existe el número de contacto de una persona, para esto estos valores serán 
verificados con variables, entre 2 que existan y dos que no existan
- Indicar mediante un mensaje si está o no agregados a la agenda de contactos
- En caso que no exista agregarlo al diccionario de contactos
- Mostrar finalmente el diccionario actualizado.
"""
contactos = {"Kass": "980456441", "Santi": "929434891", "María": "973343210"}

# Personas a verificar (2 existen, 2 no)
personas = ["Kass", "Santi", "Pedro", "Carla"]

for persona in personas:
    if persona in contactos:
        print(persona, "ya está en la agenda con el número", contactos[persona])
    else:
        print(persona, "no está en la agenda, se agregará.")
        contactos[persona] = "900000000"

print("Agenda actualizada:", contactos)

