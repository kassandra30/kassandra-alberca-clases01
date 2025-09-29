"""Uso de cond. if"""
"""
Uso de if ternarios
Requisitos:
- Ingresar por teclado el sueldo del empleado
- Si el sueldo es mayor que 4000, imprimir "Su sueldo no tiene bonificación"
- Caso contrario indicar: "Su sueldo tiene bonificación este año y será de :
sueldo_final", sueldo_final = sueldo + 20% * sueldo
"""

sueldo = float(input("Ingrese el sueldo del empleado: "))

print(
    f"Su sueldo no tiene bonificación"
    if sueldo > 4000
    else f"Su sueldo tiene bonificación este año y será de: {sueldo * 1.20:.2f}"
)