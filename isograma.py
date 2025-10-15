import re

# Isograma: palabra que no tiene letras repetidas
# Objetivo: pasar una palabra mediante un input y retornar True en consola

# Un string vacio es un isograma
# La funcion es case insensitive (no distingue A y a)
# Si hay más de una palabra retorna false
# no hay palabras con acentos

palabra = input("Ingresa una palabra: ").strip().lower()

# condicionales para las excepciones aclaradas en las reglas
# bucles (como for) para comparar cada letra con el texto

def mas_palabras(palabra):
    if " " in palabra:
        return False
    else:
        return True
    
def numero(palabra):
    for i in palabra:
        if i.isdigit():
            return False
        else:
            return True
    
def isograma(palabra):
    verificador = set()
    for i in palabra:
        verificador.add(i)
    if len(verificador) != len(palabra):
        return False
    else:
        return True
    
def verificacion(mas_palabras, isograma, palabra, numero):
    if palabra == "":
        return True
    elif mas_palabras == True and isograma == True and numero == True:
        return True
    else:
        return False
    
print(verificacion(mas_palabras=mas_palabras(palabra), palabra=palabra, isograma=isograma(palabra), numero=numero(palabra)))

# Completado! Obviamente hay muchas posibles mejoras, pero ya funciona :)