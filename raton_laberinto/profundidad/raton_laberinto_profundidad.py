def dfs_laberinto(laberinto, inicio, meta, movimientos=[(0, 1), (1, 0), (0, -1), (-1, 0)]):
    """
    Resuelve el laberinto usando Búsqueda en Profundidad (DFS) con recursividad.
    Devuelve la primera ruta encontrada (lista de coordenadas) o None si no hay solución.
    """
    filas = len(laberinto)
    if filas == 0:
        return None
    columnas = len(laberinto[0])

    visitados = set()
    camino = []

    def buscar_profundo(f, c):
        """Función recursiva interna que realiza la búsqueda."""
        coordenada_actual = (f, c)

        camino.append(coordenada_actual)
        visitados.add(coordenada_actual)

        # Test meta
        if coordenada_actual == meta:
            return True

        # Funcion sucesora
        for df, dc in movimientos:
            f_nueva, c_nueva = f + df, c + dc
            coordenada_nueva = (f_nueva, c_nueva)

            es_valido = (0 <= f_nueva < filas and
                         0 <= c_nueva < columnas and
                         laberinto[f_nueva][c_nueva] != '#')

            if es_valido and coordenada_nueva not in visitados:
                # Si la llamada recursiva encuentra la meta, propagamos el éxito.
                if buscar_profundo(f_nueva, c_nueva):
                    return True

        # Backtracking: Si ninguna rama desde aquí lleva a la meta,
        # quitamos la coordenada actual del camino y retornamos False.
        camino.pop()
        return False

    # Llamada inicial a la función recursiva
    if buscar_profundo(inicio[0], inicio[1]):
        return camino
    return None

def _imprimir_ruta(laberinto, ruta, inicio, meta):
    print("\n--- Laberinto Resuelto (Ruta con *) ---")
    mapa_impresion = [list(fila) for fila in laberinto]

    if ruta:
        for f, c in ruta:
            if (f, c) != inicio and (f, c) != meta:
                mapa_impresion[f][c] = '*'

    for fila in mapa_impresion:
        print(" ".join(fila))
    print("---------------------------------------")

if __name__ == "__main__":
    LABERINTO_EJEMPLO = [
        ['I', '.', '#', '.'],
        ['.', '#', '.', '.'],
        ['.', '.', '.', '#'],
        ['#', '.', 'Q', '.']
    ]
    INICIO_EJEMPLO = (0, 0)
    META_EJEMPLO = (3, 2)

    ruta_encontrada = dfs_laberinto(LABERINTO_EJEMPLO, INICIO_EJEMPLO, META_EJEMPLO)

    if ruta_encontrada:
        print(f"¡Ruta encontrada en {len(ruta_encontrada) - 1} pasos!")
        print(f"Ruta: {ruta_encontrada}")
        _imprimir_ruta(LABERINTO_EJEMPLO, ruta_encontrada, INICIO_EJEMPLO, META_EJEMPLO)
    else:
        print("No se pudo encontrar una ruta hacia el queso.")