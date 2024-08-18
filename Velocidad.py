# Calculadora (si otra más) de Velocidad

def velocidad():
    
    print("Calcular Velocidad") # Introducción
    
    while True: # Repetir hasta ingresar m o km
        
        distancia_unidad = input("Seleccione la unidad de medida de la distancia en Metros (m) o Kilómetros (km): ")
        
        if distancia_unidad.lower() == "km":
            while True: # Impedimos errores en los datos
                try: distancia = float(input("Ingrese la distancia recorrida en km: "))
                except: print("Ingrese un número válido")
                else: break
            while True:
                try: tiempo = float(input("Ingrese el tiempo total del recorrido en horas:"))
                except: print("Ingrese un número válido")
                else: break
            print()
            
            velocidad = distancia / tiempo
            print(f"La velocidad es de: {round(velocidad, 2)}km/h")     # Fórmula de velocidad en hr y s
            print(f"Lo que equivale a: {round((velocidad/3.6), 2)}m/s")
            break
        
        elif distancia_unidad.lower() == "m":
            while True:
                try: distancia = float(input("Ingrese la distancia recorrida en m: "))
                except: print("Ingrese un número válido")
                else: break
            while True:
                try: tiempo = float(input("Ingrese el tiempo total del recorrido en segundos:"))
                except: print("Ingrese un número válido")
                else: break
            print()
                                                                        # Lo mismo para la otra parte
            velocidad = distancia / tiempo
            print(f"La velocidad es de: {round(velocidad, 2)}m/s")
            print(f"Lo que equivale a: {round((velocidad*3.6), 2)}km/h")
            break
        else:
            print("Formato no válido, inténtelo de nuevo")
velocidad()
# COMPLETADO CON ÉXITO GG