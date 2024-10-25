# Se llama a la libreria y a uno de sus modulos.

import tkinter as tk
from tkinter import simpledialog

# Inicializamos todo lo que  se necesita para el programa.

ventana = 0
tablero = 0
juego_activo = 0
botones = 0
columna = 0
boton = 0
celda = 0
celdas = 0
fila = 0
fila_celdas = 0
ficha = 0
turno_jugador = 0
juego_activo = 0


# Se configuración de la ventana.

ventana = tk.Tk()
ventana.title("Conecta 4")

# Se inicializa el tablero lógico y los turnos.

tablero = [[' ' for _ in range(7)] for _ in range(6)]
turno_jugador = 'X'
juego_activo = True

# se crea los botones para seleccionar la columna.

botones = []
for columna in range(7):
    boton = tk.Button(ventana, text=str(columna + 1), width=5)
    boton.grid(row=0, column=columna)
    botones.append(boton)

# Se crea las celdas del tablero gráfico.

celdas = []
for fila in range(6):
    fila_celdas = []
    for columna in range(7):
        celda = tk.Label(ventana, text=' ', width=5, height=2, relief="ridge", borderwidth=2, font=('Arial', 16), bg="lightblue")
        celda.grid(row=fila + 1, column=columna)
        fila_celdas.append(celda)
    celdas.append(fila_celdas)

# Se indica el uso de una función para verificar victoria en cada movimiento.

def verificar_victoria(fila, columna):
    ficha = tablero[fila][columna]
    for direction in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        contar = 0
        for step in range(-3, 4):
            r = fila + step * direction[0]
            c = columna + step * direction[1]
            if 0 <= r < 6 and 0 <= c < 7 and tablero[r][c] == ficha:
                contar += 1
                if contar == 4:
                    return True
            else:
                contar = 0
    return False

# Se coloca ficha y se actualiza gráficos.
def colocar_ficha(event, columna):
    global turno_jugador, juego_activo
    if not juego_activo:
        return

    # Se solicita al usuario que elija el jugador.
    turno_jugador = simpledialog.askstring("Turno", "Ingrese el jugador (X o O):").upper()
    if turno_jugador not in ['X', 'O']:
        tk.Label(ventana, text="Entrada no válida. Intente de nuevo.", fg="red").grid(row=7, columnspan=7)
        return

    # Se coloca ficha en la posición más baja de la columna.
    for fila in range(5, -1, -1):
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = turno_jugador
            celdas[fila][columna].config(text=turno_jugador, fg="red" if turno_jugador == 'X' else "yellow")
            if verificar_victoria(fila, columna):
                tk.Label(ventana, text=f"¡Jugador {turno_jugador} ha ganado!", font=('Arial', 14), fg="green").grid(row=7, columnspan=7)
                juego_activo = False
            elif all(tablero[0][c] != ' ' for c in range(7)):
                tk.Label(ventana, text="¡Empate!", font=('Arial', 14), fg="orange").grid(row=7, columnspan=7)
                juego_activo = False
            break

# Se asignar la acción de clic a cada botón de columna.
for i, boton in enumerate(botones):
    boton.bind("<Button-1>", lambda event, col=i: colocar_ficha(event, col))

# Se ejecuta la ventana principal.
ventana.mainloop()
