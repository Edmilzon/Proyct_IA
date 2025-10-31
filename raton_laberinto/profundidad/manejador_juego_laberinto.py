from raton_laberinto_profundidad import dfs_laberinto

class ManejadorJuegoLaberinto:
    """
    Gestiona el estado y la lógica del juego del laberinto,
    independientemente de la interfaz gráfica.
    """
    def __init__(self, laberinto_mapa):
        self.laberinto = [list(fila) for fila in laberinto_mapa] # Copia mutable
        self.filas = len(self.laberinto)
        self.columnas = len(self.laberinto[0])
        self.inicio, self.meta = self._encontrar_inicio_meta()
        self.ruta_actual = None

    def _encontrar_inicio_meta(self):
        """Busca las coordenadas de 'I' (inicio) y 'Q' (meta) en el laberinto."""
        inicio, meta = None, None
        for f, fila in enumerate(self.laberinto):
            for c, celda in enumerate(fila):
                if celda == 'I':
                    inicio = (f, c)
                elif celda == 'Q':
                    meta = (f, c)
        return inicio, meta

    def buscar_nueva_ruta(self):
        """Ejecuta el algoritmo BFS para encontrar la ruta desde el inicio a la meta actual."""
        if self.inicio and self.meta:
            self.ruta_actual = dfs_laberinto(self.laberinto, self.inicio, self.meta)
            return self.ruta_actual
        return None

    def actualizar_meta(self, nueva_f, nueva_c):
        """
        Mueve la meta (el queso) a una nueva posición si es válida.
        Devuelve True si la actualización fue exitosa, False en caso contrario.
        """
        # Verificar que la nueva posición es válida (no es una pared)
        if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas and self.laberinto[nueva_f][nueva_c] != '#':
            # La posición anterior de la meta se convierte en el nuevo inicio
            if self.meta:
                # Limpiar la posición del inicio anterior
                if self.inicio:
                    self.laberinto[self.inicio[0]][self.inicio[1]] = '.'
                self.inicio = self.meta # El nuevo inicio es la meta anterior
                self.laberinto[self.inicio[0]][self.inicio[1]] = 'I'
            
            # Establecer la nueva meta
            self.meta = (nueva_f, nueva_c)
            self.laberinto[nueva_f][nueva_c] = 'Q'
            return True
        return False
