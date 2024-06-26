# Ejercicio 1
# nombre = input("Ingrese su nombre: ")
# print(f"{nombre.upper()} tiene {len(nombre)} letras")

# Ejercicio 2
# frase = input("Escriba cualquier frase: ")
# frase_invertida = frase[::-1]
# print(frase_invertida)

# Ejercicio 3
# correo = input("Ingrese su correo: ")
# print(correo[:correo.find('@')] + '@ceu.es')

# Ejercicio 4
# compras = input("Ingrese su lista de compras, los productos deben estar separados por comas: ")
# print(compras.replace(",", "\n"))

# Ejercicio 5
# producto = input("Nombre del producto: ")
# precio = float(input("Precio del producto: "))
# unidades = int(input("Cantidad de unidades: "))
# print(f"{producto.capitalize()} : {unidades} unidades x {round(precio,2)}$ = {round(precio*unidades,2)}$")

# Ejercicio 6
# edad = int(input("Ingrese su edad: "))
# if edad>=18:
#     print("Eres mayor de edad")
# elif edad<18:
#     print("Eres menor de edad")

# Ejercicio 7
contraseña = "hola123xd"
verificar = input("Ingrese la contraseña: ")
if contraseña==verificar.lower():
    print("Ambas contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")