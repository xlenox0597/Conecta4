# Inicializamos todo lo que se va a utilizar en el juego.

tablero = 0
juego_activo = 0
jugador_actual = 0
fila = 0
columna = 0
ficha = 0
victoria = 0
col = 0
empate = 0


tablero = [[' ' for _ in range(7)] for _ in range(6)]
juego_activo = True
jugador_actual = 1

# Imprimir el tablero
for fila in tablero:
    print("| " + " | ".join(fila) + " |")
print("  1   2   3   4   5   6   7  ")

# Mostrar el tablero

while juego_activo:
    
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")
    print("  1   2   3   4   5   6   7  ")
    
    print(f"Turno del Jugador {jugador_actual}")
    
    # Seleccionar y validar columna
    columna = int(input("Selecciona una columna (1-7): ")) - 1
    while columna < 0 or columna > 6 or tablero[0][columna] != ' ':
        columna = int(input("Columna inválida. Selecciona otra (1-7): ")) - 1

    # Colocar ficha en la posición más baja de la columna
    ficha = 'X' if jugador_actual == 1 else 'O'
    for i in range(5, -1, -1):
        if tablero[i][columna] == ' ':
            tablero[i][columna] = ficha
            break

    # Verificar victoria
    victoria = False
    for fila in range(6):
        for col in range(4):
            if tablero[fila][col] == ficha and tablero[fila][col+1] == ficha and tablero[fila][col+2] == ficha and tablero[fila][col+3] == ficha:
                victoria = True

    for fila in range(3):
        for col in range(7):
            if tablero[fila][col] == ficha and tablero[fila+1][col] == ficha and tablero[fila+2][col] == ficha and tablero[fila+3][col] == ficha:
                victoria = True

    for fila in range(3):
        for col in range(4):
            if tablero[fila][col] == ficha and tablero[fila+1][col+1] == ficha and tablero[fila+2][col+2] == ficha and tablero[fila+3][col+3] == ficha:
                victoria = True

    for fila in range(3, 6):
        for col in range(4):
            if tablero[fila][col] == ficha and tablero[fila-1][col+1] == ficha and tablero[fila-2][col+2] == ficha and tablero[fila-3][col+3] == ficha:
                victoria = True

    # Declarar ganador si se cumple una condición de victoria
    if victoria:
        for fila in tablero:
            print("| " + " | ".join(fila) + " |")
        print("  1   2   3   4   5   6   7  ")
        print(f"¡Jugador {jugador_actual} ha ganado!")
        juego_activo = False
        continue

    # Verificar empate
    empate = True
    for col in range(7):
        if tablero[0][col] == ' ':
            empate = False
            break

    if empate:
        for fila in tablero:
            print("| " + " | ".join(fila) + " |")
        print("  1   2   3   4   5   6   7  ")
        print("¡El juego terminó en empate!")
        juego_activo = False
        continue

    # Cambiar turno
    jugador_actual = 2 if jugador_actual == 1 else 1
