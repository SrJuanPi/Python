# Creando una Calculadora

def calculadora():
    print("Bienvenido a Calculadora")
    print("""
    Las operaciones disponibles son:
    suma: sum
    resta: res
    multiplicación: mul
    división: div
        
    SOLO INGRESAR VALORES NUMÉRICOS

    Para Salir escriba: "salir"
    """)

    resultado = ""

    while True:

    #   Ingresando datos
        if not resultado:
            resultado = input("Ingrese un valor: ")
            if resultado.lower() == "salir":
                print("Saliendo de Calculadora...")
                break

        op = input("Ingrese operación: ")
        if op.lower() == "salir":
            print("Saliendo de Calculadora...")
            break

        dato2 = input("Ingrese otro valor: ")
        if dato2.lower() == "salir":
            print("Saliendo de Calculadora...")
            break

    #   Operaciones
        if op.lower() == "sum":
            suma = float(resultado) + float(dato2)
            print(f"Resultado: {suma}")
        elif op.lower() == "res":
            resta = float(resultado) - float(dato2)
            print(f"Resultado: {resta}")
        elif op.lower() == "mul":
            multi = float(resultado) * float(dato2)
            print(f"Resultado: {multi}")
        elif op.lower() == "div":
            divi = float(resultado) / float(dato2)
            print(f"Resultado: {divi}")
        else:
            print("Operación no válida")

# COMPLETADO... Entre "comillas" porque aún falta corregir los posibles errores}
