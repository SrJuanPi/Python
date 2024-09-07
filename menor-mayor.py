# Ordenar una lista de numbers de menor a mayor (y viceversa)

lista = [1,23,4,5,236,63,573,57,56]
lista.sort()
menor_mayor = lista
mayor_menor = lista[::-1]
print(f"lista ordenada de menor a mayor: {menor_mayor}")
print(f"lista ordenada de mayor a menor: {mayor_menor}")