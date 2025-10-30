from collections import deque

# --- Configuración del Entorno ---
ESTADO_INICIAL = [0, 0, 0, 0, 0, 0, 0, 0, 0] # 0=Vacío, 1='X', -1='O'

def es_estado_final(estado):
    """Retorna 1 si gana X, -1 si gana O, 0 si hay empate, o None si sigue en juego."""
    combinaciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)             # Diagonales
    ]
    for a, b, c in combinaciones_ganadoras:
        suma = estado[a] + estado[b] + estado[c]
        if suma == 3: return 1   # Gana 'X'
        if suma == -3: return -1 # Gana 'O'
    
    if 0 not in estado: return 0 # Empate
    return None # Sigue en juego

def obtener_movimientos_validos(estado):
    """Devuelve los índices (0-8) de las casillas vacías."""
    return [i for i, casilla in enumerate(estado) if casilla == 0]

def aplicar_movimiento(estado, movimiento, jugador):
    """Retorna un *nuevo* estado."""
    nuevo_estado = list(estado)
    nuevo_estado[movimiento] = jugador
    return nuevo_estado

# --- Implementación BFS ---
def bfs_encontrar_camino_ganador(estado_inicial, jugador_meta):
    """Busca el camino más corto (menos movimientos) para que gane el jugador_meta."""
    # Cola: (estado_actual, camino_de_movimientos_hasta_aqui)
    cola = deque([(estado_inicial, [])]) 
    visitados = {tuple(estado_inicial)}

    while cola:
        estado_actual, camino = cola.popleft()
        resultado = es_estado_final(estado_actual)

        # PRUEBA DE META: Si el estado actual es el objetivo
        if resultado == jugador_meta:
            return camino # ¡Solución encontrada!

        # Expandir si el juego sigue
        if resultado is None:
            # Determinar de quién es el turno (X=1, O=-1)
            turno = 1 if len(camino) % 2 == 0 else -1 
            
            for movimiento in obtener_movimientos_validos(estado_actual):
                nuevo_estado = aplicar_movimiento(estado_actual, movimiento, turno)
                
                if tuple(nuevo_estado) not in visitados:
                    visitados.add(tuple(nuevo_estado))
                    # El camino incluye el índice de la casilla movida
                    nuevo_camino = camino + [movimiento]
                    cola.append((nuevo_estado, nuevo_camino))
                    
    return None # No se encontró un camino ganador

# --- Ejecución de Prueba BFS ---
print("--- BFS: Búsqueda del camino ganador más corto para 'X' (1) ---")
camino = bfs_encontrar_camino_ganador(ESTADO_INICIAL, 1)

if camino:
    print(f"Camino de {len(camino)} movimientos (índices 0-8) encontrado: {camino}")
else:
    print("No se encontró un camino ganador.")