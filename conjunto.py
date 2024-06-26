# Obtener un conjunto de numeros separados por comas y crear una lista

# Ejemplo del resultado: conjunto = [4,5,2,4,5,78,892,3,4]

entrada = input('Ingrese un conjunto de números separados por comas: ')
entrada = entrada.replace(" ", "")
numeros = entrada.split(",")
numeros = [i for i in numeros if i != ""] # Esta línea fue hecha con IA
print(numeros)

# Completado con éxito
# Nota: Se le puede agregar 2 cosas. 1-Convertir los elementos a numeros, y 2-Crear una función en caso de ingresar una letra.