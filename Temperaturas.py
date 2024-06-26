# Conversor de grados Celsius a Fahrenheit (y viceversa)

def temperatura():
    grados = float(input("Ingrese Temperatura: "))
    convertir = input("Convertir grados a Fahrenheit (F) o Celsius (C): ")

    if convertir.lower() == "f":
        celsius = grados
        fahrenheit = ((celsius * 9/5) + 32)
        print(f"{celsius}°C equivalen a {fahrenheit}°F")
    elif convertir.lower() == "c":
        fahrenheit = grados
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F equivalen a {celsius}°C")
    else:
        print("Valor no válido")

temperatura()
# LISTO COMPLETADO GG! Costó pero se logró