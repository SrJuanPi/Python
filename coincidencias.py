# Contar las coincidencias en un texto

texto = input("Ingrese texto: ")
palabra = input("Ingrese texto a buscar: ")
coincidencias = texto.count(palabra)

if coincidencias > 0:
    print(f'Se encontró "{palabra}" {coincidencias} veces en el texto')
else:
    print("No se encontraron coincidencias")