from collections import deque

def reconstruir_camino(padres, inicio, meta):
    camino = []
    actual = meta
    while actual is not None:
        camino.append(actual)
        actual = padres.get(actual)
    return camino[::-1]

def bfs_laberinto(laberinto, inicio, meta):
    """
    Resuelve el laberinto usando Búsqueda por Amplitud (BFS).
    Devuelve la ruta más corta (lista de coordenadas) o None si no hay solución.
    """
    filas = len(laberinto)
    if filas == 0:
        return None
    columnas = len(laberinto[0])

    cola = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while cola:
        actual = cola.popleft()

        # 1. Prueba de Meta
        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        # 2. Expansión: Funcion sucesora
        for df, dc in movimientos:
            f_nueva, c_nueva = actual[0] + df, actual[1] + dc
            nueva = (f_nueva, c_nueva)

            # Verificar si la nueva posición es válida y no visitada
            es_valido = (0 <= f_nueva < filas and
                         0 <= c_nueva < columnas and
                         laberinto[f_nueva][c_nueva] != '#')

            if es_valido and nueva not in visitados:
                visitados.add(nueva)
                # Guardamos de dónde venimos para poder reconstruir la ruta
                padres[nueva] = actual
                cola.append(nueva)

    return None
