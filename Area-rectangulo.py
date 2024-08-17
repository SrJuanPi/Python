# area de un rectangulo xdxd
while True:
    try: base = float(input("ingrese base en cm: "))
    except: print("Ingrese un número en base")
    else: break
while True:   
    try: altura = float(input("ingrese altura en cm: "))
    except: print("Ingrese un número en altura")
    else: break

print(f"El área del rectángulo es {base*altura}cm²")