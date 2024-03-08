from collections import deque

def encontrar_camino_laberinto(laberinto, inicio, destino):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Definir las direcciones arriba, abajo, izquierda y derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Función para verificar si una posición es válida en el laberinto
    def es_valida(x, y):
        return 0 <= x < filas and 0 <= y < columnas and laberinto[x][y] == 0

    # Inicializar la cola con la posición de inicio y su distancia
    cola = deque([(inicio[0], inicio[1], 0)])
    visitado = set([(inicio[0], inicio[1])])

    while cola:
        x, y, distancia = cola.popleft()

        # Verificar si hemos llegado al destino
        if (x, y) == destino:
            print(f"Camino más corto encontrado. Distancia: {distancia}")
            return

        # Explorar las posiciones vecinas
        for dx, dy in direcciones:
            nueva_x, nueva_y = x + dx, y + dy

            # Verificar si la posición vecina es válida y no ha sido visitada
            if es_valida(nueva_x, nueva_y) and (nueva_x, nueva_y) not in visitado:
                cola.append((nueva_x, nueva_y, distancia + 1))
                visitado.add((nueva_x, nueva_y))

    print("No se encontró un camino al destino.")

# Ejemplo de uso
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

punto_inicio = (0, 0)
punto_destino = (4, 4)

encontrar_camino_laberinto(laberinto, punto_inicio, punto_destino)
