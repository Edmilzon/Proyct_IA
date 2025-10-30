import tkinter as tk
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'minimax'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'anchura'))

from juego_tres_en_raya_minimax_gui import iniciar_juego_minimax
from juego_tres_en_raya_gui import iniciar_juego_bfs

COLOR_FONDO = '#121212'
COLOR_TEXTO = '#EAEAEA'
COLOR_BOTON = '#6200EE'
COLOR_BOTON_HOVER = '#3700B3'
FONT_TITULO = ('Consolas', 20, 'bold')
FONT_BOTON = ('Consolas', 14)

def crear_menu_principal():
    root = tk.Tk()
    root.title("Selector de Juegos - Tres en Raya")
    root.config(bg=COLOR_FONDO, padx=40, pady=30)
    root.resizable(False, False)

    label_titulo = tk.Label(root, text="Elige una versión del Tres en Raya",
                            font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_titulo.pack(pady=(0, 25))

    def lanzar_juego(juego_func, ventana_actual):
        ventana_actual.destroy() 
        juego_func()         

    btn_minimax = tk.Button(root, text="Jugar contra IA (Minimax)",
                            font=FONT_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO,
                            relief='flat', padx=20, pady=10,
                            command=lambda: lanzar_juego(iniciar_juego_minimax, root))
    btn_minimax.pack(fill='x', pady=5)

    btn_bfs = tk.Button(root, text="Jugar contra IA (Búsqueda en Anchura)",
                        font=FONT_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO,
                        relief='flat', padx=20, pady=10,
                        command=lambda: lanzar_juego(iniciar_juego_bfs, root))
    btn_bfs.pack(fill='x', pady=5)

    root.mainloop()

if __name__ == "__main__":
    crear_menu_principal()
