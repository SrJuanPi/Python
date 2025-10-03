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
# contraseña = "hola123xd"
# verify = input("Ingrese la contraseña: ")
# if contraseña==verify.lower():
#     print("Ambas contraseñas coinciden")
# else:
#     print("Las contraseñas no coinciden")

#--------Syntaxis y Estructuras de Datos---------

# Ejercicio 8
# lista = [1,2,3,4,5,6,7,8,9,10]
# nueva_lista = []
# for i in lista:
#     if i%2 == 0:
#         nueva_lista.append(i)
#     else: continue
# print(nueva_lista)
# Completado! Y muy fácil y rápido incluso sin haber programado tanto tiempo

# Ejercicio 9

# diccionario = {
#     "Juan" : 18,
#     "Carlos" : 16,
#     "Santiago": 17,
#     "Angel" : 21
# }

# for clave, valor in diccionario.items():
#     if valor >= 18: print(clave)
# Completado! Solo tuve que "recordar" (gpt) los métodos de listas y su función

# Ejercicio 10

# conjunto = {"palabra", "sol", "ola", "si", "palta", "amor"}
# nuevo_conjunto = {""}
# for i in conjunto:
#     if len(i) <= 4:
#         nuevo_conjunto.add(i)
# nuevo_conjunto.remove("")
# print(nuevo_conjunto)
# Completado! Pero costó un poco, y no me termina de convencer como lo hice

# Ejercicio 11

# lista_tuplas = [("iphone 15 pro", 1000),("PC Gamer", 850),("chocolate", 1)] # $usd

# def producto_mas_caro(lista_de_tuplas):
#     lista = []
#     for i in lista_de_tuplas:
#         lista.append(i[1])
#     return max(lista_de_tuplas, key=lambda t: t[1])[0], max(lista)

# print(producto_mas_caro(lista_tuplas))
# Completado! pero gpt de por medio para el nombre del producto

# Ejercicio 12

lista_palabras = ["hola", "sol", "hola", "sol", "sol", "azucar", "melon"]
diccionario = {}

for i in lista_palabras:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1
print(diccionario)
# Completado!