# Calculadora (si otra más) de Velocidad

def velocidad():
    print("Calcular Velocidad")

    distancia_unidad = input("Seleccione la unidad de medida de la distancia en Metros (m) o Kilómetros (km): ")
    if distancia_unidad == "km":
        distancia = float(input("Ingrese la distancia recorrida en km: "))
        tiempo = float(input("Ingrese el tiempo total del recorrido en horas:"))
        print()
        
        velocidad = distancia / tiempo
        print(f"La velocidad es de: {round(velocidad, 2)}km/h")
        print(f"Lo que equivale a: {round((velocidad/3.6), 2)}m/s")

    elif distancia_unidad == "m":
        distancia = float(input("Ingrese la distancia recorrida en m: "))
        tiempo = float(input("Ingrese el tiempo total del recorrido en segundos:"))
        print()

        velocidad = distancia / tiempo
        print(f"La velocidad es de: {round(velocidad, 2)}m/s")
        print(f"Lo que equivale a: {round((velocidad*3.6), 2)}km/h")
    else:
        print("Formato no válido")

# COMPLETADO CON ÉXITO GG