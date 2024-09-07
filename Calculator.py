# Creando una Calculadora

def calculator():
    print("Welcome to Calculator")
    print("""
    The available operations are:
    addition: add
    subtraction: sub
    multiplication: mul
    division: div
        
    ONLY ENTER NUMERICAL VALUES

    To exit type: "exit"
    """)

    result = ""

    while True:

    #   Ingresando datos
        if not result:
            result = input("Enter a value: ")
            if result.lower() == "exit":
                print("Exiting Calculator...")
                break

        op = input("Enter operation: ")
        if op.lower() == "exit":
            print("Exiting Calculator...")
            break

        value = input("Enter another value: ")
        if value.lower() == "exit":
            print("Exiting Calculator...")
            break

    #   Operaciones
        if op.lower() == "add":
            add = float(result) + float(value)
            print(f"result: {add}")
        elif op.lower() == "sub":
            sub = float(result) - float(value)
            print(f"result: {sub}")
        elif op.lower() == "mul":
            mul = float(result) * float(value)
            print(f"result: {mul}")
        elif op.lower() == "div":
            div = float(result) / float(value)
            print(f"result: {div}")
        else:
            print("Invalid operation")
calculator()

# COMPLETADO... Entre "comillas" porque aún falta corregir los posibles errores}
