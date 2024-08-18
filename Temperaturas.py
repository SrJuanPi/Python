# Conversor de grados Celsius a Fahrenheit (y viceversa)

def temperatura():
    while True:
        try: grados = float(input("Ingrese Temperatura: "))
        except: print("Ingrese un número válido")
        else: break
    convertir = input("Convertir grados a Fahrenheit (F) o Celsius (C): ")

    if convertir.lower() == "f":
        celsius = grados
        fahrenheit = ((celsius * 9/5) + 32)
        print(f"{celsius}°C equivalen a {round(fahrenheit, 2)}°F")
    elif convertir.lower() == "c":
        fahrenheit = grados
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F equivalen a {round(celsius, 2)}°C")
    else:
        print("Valor no válido")

temperatura()
# LISTO COMPLETADO GG! Costó pero se logró