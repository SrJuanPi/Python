# Constantes
SIMBOLO_X = "X"
SIMBOLO_O = "O"
CASILLAS_TOTALES = 9
CASILLA_VACIA = ""

tablero = [["","",""],
           ["","",""],
           ["","",""]]

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

# Mostrar Tablero
def mostrar_tablero(tablero: list[list[str]]) -> None:
    """
    Muestra el tablero actual del juego en formato 3x3.
    
    Args:
        tablero: Matriz 3x3 con símbolos "X", "O" o ""
    """
    print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
-----------
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
-----------
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")

# Empate
def empate(tablero: list[list[str]]) -> bool:
    """
    Verifica si hay empate (tablero lleno sin ganador).
    
    Args:
        tablero: Matriz 3x3 con símbolos "X", "O" o ""
    
    Returns:
        True si todas las casillas están ocupadas, False en caso contrario
    """
    return all(celda in (SIMBOLO_X, SIMBOLO_O) for fila in tablero for celda in fila)

# Obtener Jugada
def obtener_jugada(simbolo: str) -> None:
    """
    Solicita al jugador una casilla válida y la marca en el tablero.
    Muestra el tablero después de la jugada.
    
    Args:
        simbolo: "X" o "O" del jugador actual
    """
    while True:
        try: 
            jugador = int(input(f"Jugador ({simbolo}) Seleccione una casilla del 1 al 9: "))
            if jugador < 1 or jugador > CASILLAS_TOTALES:
                print(f"Por favor ingrese un número entre 1 y {CASILLAS_TOTALES}.")
                continue
        except ValueError:
            print(f"Jugador ({simbolo}), por favor ingrese un número válido (1-9)")
            continue
        
        jugador_coords = conversion[jugador]
        
        if tablero[jugador_coords[0]][jugador_coords[1]] in (SIMBOLO_X, SIMBOLO_O):
            print("No puedes marcar esta casilla porque ya fue jugada, por favor selecciona otra casilla.")
            continue
        
        tablero[jugador_coords[0]][jugador_coords[1]] = simbolo
        mostrar_tablero(tablero)
        break

# Detectar ganador
def ganador(tablero: list[list[str]]) -> str | None:
    """
    Verifica si hay un ganador en el tablero.
    
    Args:
        tablero: Matriz 3x3 con símbolos "X", "O" o ""
    
    Returns:
        "X" o "O" si hay ganador, None en caso contrario
    """
    # Verificar horizontales
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] in (SIMBOLO_X, SIMBOLO_O):
            return fila[0]
    
    # Verificar verticales
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] in (SIMBOLO_X, SIMBOLO_O):
            return tablero[0][col]
    
    # Verificar diagonal principal
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] in (SIMBOLO_X, SIMBOLO_O):
        return tablero[0][0]
    
    # Verificar diagonal secundaria
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] in (SIMBOLO_X, SIMBOLO_O):
        return tablero[0][2]
    
    return None

# Finalizar juego
def finalizar_juego(simbolo_ganador: str | None) -> None:
    """
    Muestra el tablero final y el resultado del juego.
    
    Args:
        simbolo_ganador: "X" o "O" si hay ganador, None si hay empate
    """
    if simbolo_ganador:
        print(f"¡Jugador ({simbolo_ganador}) ha ganado el juego!")
    else:
        print("¡Empate!")

# Main
def main() -> None:
    """
    Función principal que controla el flujo del juego Tic Tac Toe.
    """
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
    
    mostrar_tablero(tablero)
    
    while True:
        # JUGADOR 1
        obtener_jugada(SIMBOLO_X)
        ganador_actual = ganador(tablero)
        
        if ganador_actual:
            finalizar_juego(ganador_actual)
            break
        
        if empate(tablero):
            finalizar_juego(None)
            break
        
        # JUGADOR 2
        obtener_jugada(SIMBOLO_O)
        ganador_actual = ganador(tablero)
        
        if ganador_actual:
            finalizar_juego(ganador_actual)
            break
        
        if empate(tablero):
            finalizar_juego(None)
            break

if __name__ == "__main__":
    main()