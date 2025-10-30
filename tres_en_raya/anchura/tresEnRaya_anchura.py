from collections import deque
from motor_tres_en_raya import es_estado_final, obtener_movimientos_validos, aplicar_movimiento

ESTADO_INICIAL = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def bfs_encontrar_camino_ganador(estado_inicial, jugador_meta, turno_inicial):
    """
    Busca el camino más corto (menos movimientos) para que gane el jugador_meta,
    empezando la búsqueda desde el turno_inicial.
    """
    cola = deque([(estado_inicial, [], turno_inicial)]) 
    visitados = {tuple(estado_inicial)}

    while cola:
        estado_actual, camino, turno = cola.popleft()
        resultado = es_estado_final(estado_actual)

        # PRUEBA DE META: Si el estado actual es el objetivo
        if resultado == jugador_meta:
            return camino # Ganador encontrado

        # Expandir si el juego sigue
        if resultado is None:
            for movimiento in obtener_movimientos_validos(estado_actual):
                nuevo_estado = aplicar_movimiento(estado_actual, movimiento, turno)
                
                if tuple(nuevo_estado) not in visitados:
                    visitados.add(tuple(nuevo_estado))
                    # El camino incluye el índice de la casilla movida
                    nuevo_camino = camino + [(movimiento, turno)]
                    siguiente_turno = -turno 
                    cola.append((nuevo_estado, nuevo_camino, siguiente_turno))
                    
    return None

if __name__ == "__main__":
    print("Búsqueda del camino ganador más corto para 'X'")
    camino = bfs_encontrar_camino_ganador(ESTADO_INICIAL, 1, 1)

    if camino:
        movimientos = [mov for mov, jug in camino]
        print(f"Camino de {len(movimientos)} movimientos encontrado: {movimientos}")
        print("\nDetalle del camino:")
        estado_temporal = ESTADO_INICIAL
        for movimiento, jugador in camino:
            simbolo = 'X' if jugador == 1 else 'O'
            print(f"- Jugador '{simbolo}' mueve a la casilla {movimiento}")
            estado_temporal = aplicar_movimiento(estado_temporal, movimiento, jugador)
    else:
        print("No se encontró un camino ganador.")