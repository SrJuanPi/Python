
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tablero = f"""
 {lista[0]} | {lista[1]} | {lista[2]} 
---+---+---
 {lista[3]} | {lista[4]} | {lista[5]} 
---+---+---
 {lista[6]} | {lista[7]} | {lista[8]} 
"""
print(tablero)
movimiento1 = input("Ingrese su movimiento: ")
lista[int(movimiento1)-1] = "X"
print(tablero)