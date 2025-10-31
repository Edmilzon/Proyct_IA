from raton_laberinto_anchura import bfs_laberinto

class ManejadorJuegoLaberinto:

    def __init__(self, laberinto_mapa):
        self.laberinto = [list(fila) for fila in laberinto_mapa] # Copia mutable
        self.filas = len(self.laberinto)
        self.columnas = len(self.laberinto[0])
        self.inicio, self.meta = self._encontrar_inicio_meta()
        self.ruta_actual = None

    def _encontrar_inicio_meta(self):
        inicio, meta = None, None
        for f, fila in enumerate(self.laberinto):
            for c, celda in enumerate(fila):
                if celda == 'I':
                    inicio = (f, c)
                elif celda == 'Q':
                    meta = (f, c)
        return inicio, meta

    def buscar_nueva_ruta(self):
        if self.inicio and self.meta:
            self.ruta_actual = bfs_laberinto(self.laberinto, self.inicio, self.meta)
            return self.ruta_actual
        return None

    def actualizar_meta(self, nueva_f, nueva_c):
        if 0 <= nueva_f < self.filas and 0 <= nueva_c < self.columnas and self.laberinto[nueva_f][nueva_c] != '#':
            if self.meta:
                if self.inicio:
                    self.laberinto[self.inicio[0]][self.inicio[1]] = '.'
                self.inicio = self.meta
                self.laberinto[self.inicio[0]][self.inicio[1]] = 'I'
            
            self.meta = (nueva_f, nueva_c)
            self.laberinto[nueva_f][nueva_c] = 'Q'
            return True
        return False
