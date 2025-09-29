"""
    Programación Orientada a Objetos (POO)
    Participación
Requerimientos:
- Crear una clase Alumno
- Debe tener un atributo de nacionalidad con el valor de "Peruano"
- Crear un método que indicará el promedio del alumno
- Tendrá 3 notas para 3 cursos (Cálculo II, Matemática Discreta y Redes neuronales), la nota inicial de c/u será de 0
(puedes basarte en diccionarios)
- Crear un método donde indicará qué curso fue que tuvo la mayor nota
- Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio  (>= 13)
- Las notas serás pasadas por parámetro al momento de instanciar la clase
- Habrá un método adicional para obtener el nombre y distrito de residencia del alumno
-  Instanciar la clase para el caso de 2 alumnos por lo menos
"""

class Alumno:

    def __init__(self, nombre, nota_1=0, nota_2=0, nota_3=0):
        self.nombre = nombre
        self.nacionalidad = "Peruano"
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3

    def promedio(self):
        return (self.nota_1 + self.nota_2 + self.nota_3) / 3

    def aprobado(self):
        return self.promedio() >= 11  # Aprobado si el promedio es mayor o igual a 11


# Crear alumnos con los nombres solicitados
alumno_1 = Alumno("Kass", 13, 15, 11)
alumno_2 = Alumno("Nicol", 18, 17, 16)
alumno_3 = Alumno("Leandro", 10, 12, 9)
alumno_4 = Alumno("Gustavo", 14, 11, 13)

# Probar
for alumno in [alumno_1, alumno_2, alumno_3, alumno_4]:
    print(f"{alumno.nombre} ({alumno.nacionalidad}) - Promedio: {alumno.promedio():.2f} - {'Aprobado' if alumno.aprobado() else 'Desaprobado'}")