# Lanzador de Proyectos de IA

Este proyecto es una colección de juegos clásicos implementados en Python con interfaces gráficas construidas con `tkinter`. El objetivo principal es demostrar y comparar diferentes algoritmas de inteligencia artificial en un entorno interactivo.

## Características

*   **Menú Principal**: Un lanzador central para seleccionar y ejecutar los diferentes proyectos.
*   **Juego Tres en Raya (Tic-Tac-Toe)**:
    *   **IA con Algoritmo Minimax**: Un oponente invencible que utiliza el algoritmo Minimax para determinar el movimiento óptimo en cada turno.
    *   **IA con Búsqueda en Anchura (BFS)**: Un oponente que utiliza una estrategia basada en heurísticas y el algoritmo BFS para encontrar caminos ganadores o bloquear al jugador.
*   **Próximamente**:
    *   Juego del Laberinto.

## Tecnologías Utilizadas

*   **Python 3**
*   **Tkinter** para la interfaz gráfica de usuario (GUI).

---

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Prerrequisitos

*   Asegúrate de tener Python 3 instalado en tu sistema.

### 2. Clonar el Repositorio

```bash
git clone https://github.com/Edmilzon/Proyct_IA.git
cd Proyt_IA
```

### 3. Crear y Activar un Entorno Virtual

Usar un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno virtual
py -m venv .venv

# Activar en Windows
.venv\Scripts\activate

# Activar en macOS/Linux
source .venv/bin/activate
```

### 4. Instalar Dependencias

Instala las librerías necesarias que se encuentran en `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el Proyecto

Para iniciar el lanzador principal de juegos, ejecuta el siguiente comando desde la raíz del proyecto:

```bash
py juegos.py
```








---

## Para Desarrolladores

Si añades nuevas librerías al proyecto, no olvides actualizar el archivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```