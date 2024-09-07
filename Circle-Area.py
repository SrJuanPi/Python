# Calculando el area de un circulo

from math import pi

while True:
    try: radio = float(input("Enter the radius of the circle: "))
    except: print("Please enter a valid number")
    else: break

area = pi*(radio**2)
print(f"The radius of the circunference is: {round(area, 3)}cm²")