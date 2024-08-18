# Calculador de cuantas décadas y años tiene una Persona

while True:
    try: edad = int(input("Ingrese su edad: "))
    except: print("Por favor ingrese un número")
    else: break
decadas = edad // 10
años = edad % 10

print(f"Usted tiene {decadas} décadas y {años} años de edad")