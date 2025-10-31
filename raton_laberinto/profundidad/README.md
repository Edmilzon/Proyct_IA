# Solución del Laberinto con Búsqueda en Profundidad (DFS)

Este proyecto implementa una solución al clásico problema del laberinto utilizando el algoritmo de **Búsqueda en Profundidad (Depth-First Search, DFS)**. El objetivo es encontrar un camino para que un ratón ('I') llegue hasta un queso ('Q') a través de un laberinto con paredes ('#').

## ¿Cómo funciona el algoritmo de Búsqueda en Profundidad?

La Búsqueda en Profundidad es un algoritmo para recorrer o buscar en un grafo o una estructura de datos de árbol. La idea principal es explorar una rama del laberinto tan profundamente como sea posible antes de retroceder (hacer "backtracking") y probar otra rama.

Imagina que estás en un laberinto real. Con la estrategia DFS, elegirías un camino y seguirías por él sin desviarte. Si llegas a un callejón sin salida, retrocedes hasta la última intersección donde tenías otra opción y la tomas, repitiendo el proceso.

### Analogía: El Ratón Obstinado

Piensa en el ratón como un explorador muy obstinado:

1.  **Elige un camino y no mira atrás**: Desde su posición actual, el ratón mira las casillas adyacentes (arriba, abajo, izquierda, derecha) y elige la primera que puede visitar (que no sea una pared y que no haya visitado antes).
2.  **Avanza sin parar**: Se mueve a esa nueva casilla y repite el proceso, siempre avanzando por el primer camino disponible. Va dejando un rastro de "migas de pan" (marcando las casillas como `visitadas`) para no volver a pasar por el mismo sitio y evitar bucles infinitos.
3.  **Llega al queso (¡Éxito!)**: Si en algún momento llega a la casilla del queso, ¡lo ha logrado! El camino que ha seguido desde el inicio hasta el queso es la solución.
4.  **Llega a un callejón sin salida (¡Fracaso parcial!)**: Si el ratón llega a una casilla desde la cual no puede moverse a ninguna casilla nueva (todas las adyacentes son paredes o ya las visitó), se da cuenta de que ese camino no lleva a ninguna parte.
5.  **Retrocede (Backtracking)**: En este punto, el ratón "retrocede" un paso (vuelve a la casilla anterior) y borra la última "miga de pan". Desde esa posición, intenta tomar el siguiente camino que no había probado antes. Si no hay más caminos, retrocede otro paso, y así sucesivamente.

Este proceso garantiza que, si existe un camino, el algoritmo eventualmente lo encontrará. Sin embargo, no garantiza que sea el camino más corto, solo el primero que descubre siguiendo su estrategia de "profundizar primero".

### Puntos Clave del Código:

*   **Recursividad**: La función `buscar_profundo` se llama a sí misma para explorar más profundamente. Cada llamada a la función es como un paso adelante del ratón.
*   **`visitados` (Set)**: Usamos un `set` para un chequeo O(1) (muy rápido) de si ya hemos estado en una casilla. Esto es crucial para la eficiencia y para evitar bucles.
*   **`camino` (List)**: Esta lista actúa como la memoria del ratón sobre el camino que está siguiendo actualmente.
*   **`camino.append()`**: Corresponde al ratón avanzando y dejando una "miga de pan".
*   **`camino.pop()`**: Es el acto de "retroceder". Ocurre cuando una rama de exploración falla, y el ratón vuelve sobre sus pasos para probar una alternativa.

## Conclusión

La Búsqueda en Profundidad es una estrategia potente y relativamente sencilla de implementar. Es excelente para problemas donde solo necesitas encontrar *una* solución, no necesariamente la mejor o la más corta. Su naturaleza recursiva se adapta perfectamente a la exploración de laberintos y otras estructuras jerárquicas.
