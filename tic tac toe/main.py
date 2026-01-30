# Horizontales
def horizontal_solutions(tablero):
    if tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] in ("X", "O"):
        return True
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] in ("X", "O"):
        return True
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] in ("X", "O"):
        return True
    else:
        return False
    
# Verticales
def vertical_solutions(tablero):
    if tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] in ("X", "O"):
        return True
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] in ("X", "O"):
        return True
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] in ("X", "O"):
        return True
    else:
        return False
    
# Diagonales
def diagonal_solutions(tablero):
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] in ("X", "O"):
        return True
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] in ("X", "O"):
        return True
    else:
        return False

# Mostrar Tablero
def mostrar_tablero(tablero):
    print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
-----------
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
-----------
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")

# Empate
def empate(tablero):
    if tablero[0][0] and tablero[0][1] and tablero[0][2] and tablero[1][0] and tablero[1][1] and tablero[1][2] and tablero[2][0] and tablero[2][1] and tablero[2][2] in ("X", "O"):
        return True
    else:
        return False

# Verificar
def verificacion(h,v,d):
    if h: return True
    elif v: return True
    elif d: return True
    else: return False


def main():
    print("""
Bienvenidos a Tic Tac Python, el juego de Tic Tac Toe más sencillo
y aburrido posible hecho en python!

- Las reglas son simples, hay 9 casillas en el tablero, 3 de arriba a abajo y
  3 de izquierda a derecha.
- En cada turno el jugador solo puede escoger una casilla para marcar.
- El jugador 1 siempre es X y el jugador 2 siempre es O.
- El juego termina si uno de los jugadores hace 3 en raya o hay empate.

¡A Jugar!
""")
    
    tablero = [["","",""],
               ["","",""],
               ["","",""]]
    # Inputs
    conversion = {
    1 : [0,0],
    2 : [0,1],
    3 : [0,2],
    4 : [1,0],
    5 : [1,1],
    6 : [1,2],
    7 : [2,0],
    8 : [2,1],
    9 : [2,2],
}
    
    while True:
        mostrar_tablero(tablero=tablero)
        
        # JUGADOR 1
        while True:
            try: 
                jugador1 = int(input("Jugador 1 (X) Seleccione una casilla del 1 al 9: "))
                if jugador1 < 1 or jugador1 > 9:
                    print("Por favor ingrese un número entre 1 y 9.")
                    continue
            except:
                print("Jugador 1 (X), por favor ingrese un número válido (1-9)")
                continue
            
            jugador1 = conversion[jugador1]
            
            if tablero[jugador1[0]][jugador1[1]] in ("X", "O"):
                print("No puedes marcar esta casilla porque ya fue jugada, por favor selecciona otra casilla.")
                continue
            
            tablero[jugador1[0]][jugador1[1]] = "X"
            break
        
        if empate(tablero=tablero) == True:
            mostrar_tablero(tablero=tablero)
            print("Empate.")
            break
        if verificacion(horizontal_solutions(tablero), vertical_solutions(tablero), diagonal_solutions(tablero)):
            mostrar_tablero(tablero=tablero)
            print("Jugador 1 (X) ha ganado el juego.")
            break
        
        mostrar_tablero(tablero=tablero)
        
        # JUGADOR 2
        while True:
            try:
                jugador2 = int(input("Jugador 2 (O) Seleccione una casilla del 1 al 9: "))
                if jugador2 < 1 or jugador2 > 9:
                    print("Por favor ingrese un número entre 1 y 9.")
                    continue
            except:
                print("Jugador 2 (O), por favor ingrese un número válido (1-9)")
                continue
            
            jugador2 = conversion[jugador2]
            
            if tablero[jugador2[0]][jugador2[1]] in ("X", "O"):
                print("No puedes marcar esta casilla porque ya fue jugada, por favor selecciona otra casilla.")
                continue
            
            tablero[jugador2[0]][jugador2[1]] = "O"
            break
        
        if empate(tablero=tablero) == True:
            mostrar_tablero(tablero=tablero)
            print("Empate.")
            break
        if verificacion(horizontal_solutions(tablero), vertical_solutions(tablero), diagonal_solutions(tablero)):
            mostrar_tablero(tablero=tablero)
            print("Jugador 2 (O) ha ganado el juego.")
            break

if __name__ == "__main__":
    main()