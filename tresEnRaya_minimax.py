# Se reutilizan las funciones es_estado_final, obtener_movimientos_validos y aplicar_movimiento 
# del código anterior.

# --- Función de Utilidad ---
def utilidad(estado):
    """
    Función de utilidad (evaluación final):
    Devuelve +1 si gana MAX (X), -1 si gana MIN (O), o 0 si hay empate.
    """
    return es_estado_final(estado) if es_estado_final(estado) is not None else 0

# --- Algoritmo Minimax (Función Principal Recursiva) ---
def minimax(estado, turno):
    """
    Calcula el valor óptimo (mejor resultado) del estado para el 'turno' actual.
    """
    # Caso Base: El juego ha terminado
    if es_estado_final(estado) is not None:
        return utilidad(estado), None # Devuelve valor, sin movimiento

    movimientos = obtener_movimientos_validos(estado)

    # El jugador MAX (IA, 'X') busca el valor más alto (1)
    if turno == 1: 
        mejor_valor = -float('inf') 
        
        for movimiento in movimientos:
            nuevo_estado = aplicar_movimiento(estado, movimiento, turno)
            # Llamada recursiva para el oponente (MIN)
            valor, _ = minimax(nuevo_estado, -1) 
            
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = movimiento
        return mejor_valor, mejor_movimiento

    # El jugador MIN (Oponente, 'O') busca el valor más bajo (-1)
    else: 
        mejor_valor = float('inf') 
        
        for movimiento in movimientos:
            nuevo_estado = aplicar_movimiento(estado, movimiento, turno)
            # Llamada recursiva para el oponente (MAX)
            valor, _ = minimax(nuevo_estado, 1) 
            
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = movimiento
        return mejor_valor, mejor_movimiento

# --- Ejecución de Prueba Minimax ---
def imprimir_tablero(estado):
    """Muestra el tablero de forma legible."""
    simbolos = {0: ' ', 1: 'X', -1: 'O'}
    print("-" * 13)
    for i in range(3):
        print(f"| {simbolos[estado[i*3]]} | {simbolos[estado[i*3+1]]} | {simbolos[estado[i*3+2]]} |")
        print("-" * 13)

print("\n--- MINIMAX: Búsqueda del movimiento óptimo para 'X' (1) ---")

# Un tablero donde 'X' tiene un movimiento ganador obvio (casilla 6)
tablero_prueba = [1, 1, 0,
                  -1, -1, 0,
                  0, 0, 0] 
imprimir_tablero(tablero_prueba)

# La IA (X) calcula su mejor jugada
valor_optimo, movimiento_optimo = minimax(tablero_prueba, 1)

print(f"\nEl valor óptimo (mejor resultado posible) es: {valor_optimo}")
print(f"El mejor movimiento para 'X' (IA) es en la casilla: {movimiento_optimo} (índice 0-8)")

# --- Ejecución de Prueba Minimax (Continuación) ---

estado_despues_movimiento = aplicar_movimiento(tablero_prueba, movimiento_optimo, 1)
print("\nTablero después del movimiento óptimo:")
imprimir_tablero(estado_despues_movimiento)
print(f"Resultado final del tablero (1 = X gana): {es_estado_final(estado_despues_movimiento)}")