# Calculador de cuantas décadas y años tiene una Persona

while True:
    edad = input("Ingrese su edad: ")
    try:
        decadas = int(edad) // 10
        años = int(edad) % 10
    except:
        print("Por favor ingrese un número")
    else:
        break

print(f"Usted tiene {decadas} décadas y {años} años de edad")