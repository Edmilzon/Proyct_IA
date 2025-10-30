
COMBINACIONES_GANADORAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), 
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  
    (0, 4, 8), (2, 4, 6)            
]

def es_estado_final(estado):
    for a, b, c in COMBINACIONES_GANADORAS:
        suma = estado[a] + estado[b] + estado[c]
        if suma == 3: return 1   # Gana 'X'
        if suma == -3: return -1 # Gana 'O'
    
    if 0 not in estado: return 0
    return None 

def obtener_movimientos_validos(estado):
    return [i for i, casilla in enumerate(estado) if casilla == 0]

def aplicar_movimiento(estado, movimiento, jugador):
    nuevo_estado = list(estado)
    if 0 <= movimiento < 9 and nuevo_estado[movimiento] == 0:
        nuevo_estado[movimiento] = jugador
    return nuevo_estado
