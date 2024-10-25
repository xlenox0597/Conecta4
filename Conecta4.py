# Función para inicializar el tablero
def crear_tablero():
    return [[' ' for _ in range(7)] for _ in range(6)]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")
    print("  1   2   3   4   5   6   7  ")

# Función para verificar si la columna tiene espacio disponible
def columna_valida(tablero, columna):
    return tablero[0][columna] == ' '

# Función para colocar una ficha en el tablero
def colocar_ficha(tablero, columna, ficha):
    for fila in reversed(tablero):
        if fila[columna] == ' ':
            fila[columna] = ficha
            break

# Función para verificar si un jugador ha ganado
def verificar_victoria(tablero, ficha):
    # Verificar horizontal
    for fila in range(6):
        for col in range(4):
            if all([tablero[fila][col+i] == ficha for i in range(4)]):
                return True

    # Verificar vertical
    for fila in range(3):
        for col in range(7):
            if all([tablero[fila+i][col] == ficha for i in range(4)]):
                return True

    # Verificar diagonal descendente
    for fila in range(3):
        for col in range(4):
            if all([tablero[fila+i][col+i] == ficha for i in range(4)]):
                return True

    # Verificar diagonal ascendente
    for fila in range(3, 6):
        for col in range(4):
            if all([tablero[fila-i][col+i] == ficha for i in range(4)]):
                return True

    return False

# Función para verificar si hay empate
def verificar_empate(tablero):
    return all([tablero[0][col] != ' ' for col in range(7)])

# Función principal del juego
def jugar():
    tablero = crear_tablero()
    juego_activo = True
    jugador_actual = 1

    while juego_activo:
        imprimir_tablero(tablero)
        print(f"Turno del Jugador {jugador_actual}")
        
        # Obtener columna válida del jugador
        columna = int(input("Selecciona una columna (1-7): ")) - 1
        while columna < 0 or columna > 6 or not columna_valida(tablero, columna):
            columna = int(input("Columna inválida. Selecciona otra (1-7): ")) - 1

        # Colocar la ficha
        ficha = 'X' if jugador_actual == 1 else 'O'
        colocar_ficha(tablero, columna, ficha)

        # Verificar si el jugador actual ha ganado
        if verificar_victoria(tablero, ficha):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} ha ganado!")
            juego_activo = False
        # Verificar si hay empate
        elif verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡El juego terminó en empate!")
            juego_activo = False
        else:
            jugador_actual = 2 if jugador_actual == 1 else 1

# Iniciar el juego
jugar()