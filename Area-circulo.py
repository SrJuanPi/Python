# Calculando el area de un circulo

from math import pi

while True:
    try: radio = float(input("Ingrese el radio de la circunferencia en cm: "))
    except: print("Ingrese un número válido")
    else: break

area = pi*(radio**2)
print(f"El área de la circunferencia es: {round(area, 3)}cm²")