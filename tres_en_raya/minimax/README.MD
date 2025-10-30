# Comportamiento del Algoritmo Minimax en Tres en Raya

Este documento explica el comportamiento del algoritmo Minimax implementado en el juego de Tres en Raya, particularmente por qué la IA no siempre elige el "camino más corto" hacia la victoria, incluso cuando tiene la oportunidad.

## ¿Por qué la IA no siempre elige la "movida más eficiente" o la "ganadora más directa"?

### 1. Minimax busca el mejor resultado posible, no necesariamente el camino más corto:

*   El algoritmo Minimax está diseñado para encontrar la jugada que garantiza el mejor resultado para el jugador actual, asumiendo que el oponente también jugará de forma óptima.
*   En el Tres en Raya, los resultados posibles son: ganar (`+1`), perder (`-1`) o empatar (`0`).
*   Si la IA (MAX) puede ganar, Minimax le asignará un valor de `1` a cualquier secuencia de movimientos que lleve a una victoria. Si hay múltiples movimientos que conducen a una victoria, y todos garantizan un `+1` (es decir, una victoria), Minimax elegirá el primero que encuentre en su búsqueda.

### 2. Orden de evaluación de movimientos:

*   La función `minimax` itera sobre los movimientos válidos que le devuelve `obtener_movimientos_validos`.
*   Cuando encuentra un movimiento que lleva al `mejor_valor` (por ejemplo, una victoria), lo selecciona. Si luego encuentra otro movimiento que también lleva al mismo `mejor_valor`, no lo reemplaza porque la condición `if comparar(valor, mejor_valor)` (que es `valor > mejor_valor` para MAX) no se cumple si `valor` es igual a `mejor_valor`.
*   Esto significa que si la IA puede ganar en 1 movimiento (por ejemplo, casilla 5) y también puede ganar en 2 movimientos a través de otra casilla (por ejemplo, casilla 2), y la casilla 2 aparece antes en la lista de movimientos válidos, la IA podría elegir la casilla 2, ya que ambas garantizan la victoria (valor `+1`).

### 3. El Tres en Raya es un juego "resuelto":

*   En el Tres en Raya, si ambos jugadores juegan perfectamente, el resultado siempre es un empate.
*   Minimax, al ser un algoritmo de búsqueda exhaustiva (para un juego tan pequeño), es un "jugador perfecto". Si la IA tiene la oportunidad de ganar, la tomará. Si no puede ganar, buscará empatar. Si no puede ni ganar ni empatar, intentará prolongar el juego o minimizar la pérdida.

## Conclusión

El comportamiento observado no es un error del algoritmo, sino una característica de cómo Minimax toma decisiones cuando hay múltiples caminos que conducen al mismo resultado óptimo. La IA no está haciendo una "mala" jugada; simplemente está eligiendo *una* de las jugadas óptimas que garantizan el mejor resultado posible.