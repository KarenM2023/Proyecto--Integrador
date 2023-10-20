#Texto
laberinto = [
    "##########",
    "#P......#",
    "#.######.#",
    "#.#....#.#",
    "#.######.#",
    "#........#",
    "##########"
]

#Función para el  laberinto
def imprimir_laberinto():
    for fila in laberinto:
        print(fila)

#Mover al jugador
def mover_jugador(direccion):
    for i in range(len(laberinto)):
        if 'P' in laberinto[i]:
            fila = i
            columna = laberinto[i].index('P')
            break

    if direccion == 'arriba':
        if laberinto[fila - 1][columna] != '#':
            laberinto[fila] = laberinto[fila][:columna] + '.' + laberinto[fila][columna + 1:]
            laberinto[fila - 1] = laberinto[fila - 1][:columna] + 'P' + laberinto[fila - 1][columna + 1:]
    elif direccion == 'abajo':
        if laberinto[fila + 1][columna] != '#':
            laberinto[fila] = laberinto[fila][:columna] + '.' + laberinto[fila][columna + 1:]
            laberinto[fila + 1] = laberinto[fila + 1][:columna] + 'P' + laberinto[fila + 1][columna + 1:]
    elif direccion == 'izquierda':
        if laberinto[fila][columna - 1] != '#':
            laberinto[fila] = laberinto[fila][:columna] + '.' + laberinto[fila][columna + 1:]
            laberinto[fila] = 'P' + laberinto[fila][columna:]
    elif direccion == 'derecha':
        if laberinto[fila][columna + 1] != '#':
            laberinto[fila] = laberinto[fila][:columna] + '.' + laberinto[fila][columna + 1:]
            laberinto[fila] = laberinto[fila][:columna + 1] + 'P' + laberinto[fila][columna + 2:]

#Jugador
nombre_jugador = "KarenM"

#Bienvenida.
print(f"Bienvenida, {nombre_jugador}! ¡Comencemos a explorar el laberinto , Y Buena suerte!")

#Juego
while True:
    imprimir_laberinto()
    direccion = input("¿Hacia dónde quieres moverte? (arriba, abajo, izquierda, derecha): ")
    
    if direccion in ['arriba', 'abajo', 'izquierda', 'derecha']:
        mover_jugador(direccion)
    else:
        print("Dirección incorrecta.")
    
    if 'P' not in laberinto[-2]:
        imprimir_laberinto()
        print("¡Exelente lograstes llegar al Final.!")
        break