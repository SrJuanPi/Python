import re
# for birthday in range(1, 367):
#     if birthday == 163:                   idea original
#         print("Happy Birthday!")

def es_bisiesto(año):  #  Mejora con chat-gpt4
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
def dias_por_mes(mes, bisiesto):
    dias_en_mes = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(dias_en_mes[:mes-1])

while True:
    fecha = input("Ingrese fecha (dd-mm-aa): ")
    patron = r"\d{1,2}-\d{1,2}-\d{1,}"  #   Formato de fecha
    verificar = re.match(patron,fecha)
    
    if verificar:
        fechas = fecha.split("-")
        if len(fechas) > 3:
            print("\nFormato de fecha no válido, intente nuevamente.\n")
            continue
        dia = int(fechas[0])
        mes = int(fechas[1])      #  Separar dia, mes y año
        año = int(fechas[2])
        bisiesto = es_bisiesto(año)
        
        if (1 <= dia <= 31 and 1 <= mes <= 12 and año >= 0):
            if (mes == 2 and ((bisiesto and dia <= 29) or (not bisiesto and dia <= 28))) or \
               (mes in [4, 6, 9, 11] and dia <= 30) or \
               (mes in [1, 3, 5, 7, 8, 10, 12] and dia <= 31): break
        else:
            print("\nFormato de fecha no válido, intente nuevamente.\n")
            continue
    else:
        print("\nFormato de fecha no válido, intente nuevamente.\n")
        continue

dia_del_año = dias_por_mes(mes, bisiesto) + dia
total_dias = 366 if bisiesto else 365
print(f"Fecha: {fecha}\nDía del año: {dia_del_año} de {total_dias}\nDías restantes: {total_dias - dia_del_año}")