

from motor_tres_en_raya import es_estado_final, obtener_movimientos_validos, aplicar_movimiento

def utilidad(estado):
    return es_estado_final(estado)

def minimax(estado, turno):
    """
    Calcula el movimiento óptimo para el 'turno' actual usando el algoritmo Minimax.
    Devuelve una tupla (valor_óptimo, movimiento_óptimo).
    """
    resultado_final = utilidad(estado)
    if resultado_final is not None:
        return resultado_final, None

    movimientos = obtener_movimientos_validos(estado)
    mejor_movimiento = None

    if turno == 1:
        mejor_valor = -float('inf')
        comparar = lambda valor, mejor_valor: valor > mejor_valor
    else:
        mejor_valor = float('inf')
        comparar = lambda valor, mejor_valor: valor < mejor_valor

    for movimiento in movimientos:
        nuevo_estado = aplicar_movimiento(estado, movimiento, turno)
        valor, _ = minimax(nuevo_estado, -turno)
        if comparar(valor, mejor_valor):
            mejor_valor = valor
            mejor_movimiento = movimiento
    return mejor_valor, mejor_movimiento