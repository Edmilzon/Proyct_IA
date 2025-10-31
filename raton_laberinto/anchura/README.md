# Solución del Laberinto con Búsqueda por Anchura (BFS)

Este proyecto implementa una solución al problema del laberinto utilizando el algoritmo de **Búsqueda por Anchura (Breadth-First Search, BFS)**. El objetivo es encontrar un camino para que un ratón ('I') llegue hasta un queso ('Q').

A diferencia de la Búsqueda en Profundidad (DFS), BFS garantiza encontrar **la ruta más corta** posible en términos del número de casillas recorridas.

## ¿Cómo funciona el algoritmo de Búsqueda por Anchura?

La Búsqueda por Anchura explora el laberinto de una manera muy sistemática y ordenada, como las ondas que se expanden en un estanque. En lugar de profundizar por un solo camino, explora todos los caminos vecinos a la vez, nivel por nivel.

Imagina que estás en el laberinto. Con la estrategia BFS, primero miras todas las casillas a un paso de distancia. Luego, desde todas esas casillas, miras todas las que están a dos pasos de distancia del origen, y así sucesivamente, hasta que encuentras el queso.

### Analogía: El Ratón Metódico

Piensa en el ratón como un explorador muy metódico y organizado:

1.  **Prepara una lista de tareas (Cola)**: El ratón empieza en la casilla inicial ('I') y la anota como el primer lugar en su "lista de lugares por visitar".
2.  **Explora por niveles**: El ratón toma el primer lugar de su lista (al principio, la casilla inicial). Desde allí, mira todas las casillas vecinas a las que puede moverse (que no sean paredes ni hayan sido visitadas).
3.  **Añade a la lista**: Cada nueva casilla válida que encuentra, la añade al **final** de su lista de tareas. También anota de dónde vino para poder recordar el camino.
4.  **Repite el proceso**: El ratón tacha el lugar que acaba de explorar de su lista y pasa al siguiente. Repite el paso 2 y 3. Como siempre añade los nuevos lugares al final y procesa los del principio, explora el laberinto en capas concéntricas.
5.  **Llega al queso (¡Éxito por la ruta más corta!)**: Cuando el ratón llega a la casilla del queso, se detiene. Como ha explorado todas las rutas de 1 paso, luego todas las de 2 pasos, etc., en orden, la primera vez que encuentra el queso tiene la garantía de haberlo hecho por el camino más corto.

Este proceso es muy eficiente para encontrar la ruta óptima. A diferencia del ratón obstinado de DFS que se lanza por un solo camino, este ratón explora de manera uniforme en todas las direcciones.

### Puntos Clave del Código:

*   **`cola` (deque)**: Esta es la estructura central de BFS. Su comportamiento FIFO (First-In, First-Out) asegura que exploremos nivel por nivel. `popleft()` saca el elemento más antiguo.
*   **`visitados` (Set)**: Al igual que en DFS, es crucial para evitar volver a procesar casillas y caer en bucles.
*   **`padres` (dict)**: Este diccionario es la "memoria" del ratón. Para cada casilla, guarda desde qué casilla ("padre") se llegó a ella. Es esencial para poder `reconstruir_camino` una vez que se encuentra la meta.
*   **Bucle `while`**: El algoritmo se ejecuta mientras haya lugares en la cola por explorar. Si la cola se vacía antes de encontrar el queso, significa que es inalcanzable.

## Conclusión

La Búsqueda por Anchura es el algoritmo ideal cuando el objetivo es encontrar la **ruta más corta** en un grafo no ponderado (como nuestro laberinto, donde cada paso cuesta lo mismo). Su enfoque metódico y por niveles lo hace robusto y predecible, aunque puede consumir más memoria que DFS en laberintos muy anchos y ramificados.
