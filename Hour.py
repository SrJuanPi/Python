# Crear un programa que transforme horas en minutos, y viceversa (si puedo)
import re

while True:
    tiempo = input("Ingrese el tiempo en horas o minutos: ")
    formato_hora = r"\d{1,}:\d{1,2}"
    formato_minuto = r"\d{1,}"
    verificar_hora = re.match(formato_hora,tiempo)
    verificar_minuto = re.match(formato_minuto,tiempo)
    
    if verificar_hora:
        tiempos = tiempo.split(":")
        if len(tiempos) > 2:
            print("Formato de hora inválido. El formato permitido es 'horas:minutos'.")
            continue
            
        hora = int(tiempos[0])
        minutos = int(tiempos[1])
        
        if minutos > 59:
            print("Formato de hora inválido. Los minutos no pueden ser mayores a 59.")
            continue
        
        minutos_finales = hora*60 + minutos
        print(f"{hora}hrs con {minutos}min son {minutos_finales} minutos.")
        break
    
    elif verificar_minuto:
        try: minutos = int(tiempo)
        except:
            print("Formato de hora no válido. Si va a usar horas, asegúrese de colocar los minutos.")
            continue
        hora = minutos/60
        decimal = hora - int(hora)
        nuevos_minutos = int(decimal*60)
        if nuevos_minutos < 10:
            nuevos_minutos = f"0{str(nuevos_minutos)}"
        print(f"{minutos}min son {round(hora,2)}hrs o {int(hora)}:{nuevos_minutos}.")
        break
    
    else:
        print("Formato no válido. Use 'horas:minutos' o simplemente minutos.")
        continue