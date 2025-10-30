import tkinter as tk
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'tres_en_raya'))

from menu_juegos_TER import crear_menu_principal

COLOR_FONDO = '#121212'
COLOR_TEXTO = '#EAEAEA'
COLOR_BOTON_PRINCIPAL = '#03DAC6'
COLOR_BOTON_SECUNDARIO = '#2C2C2C'
FONT_TITULO = ('Consolas', 24, 'bold')
FONT_BOTON = ('Consolas', 16)

def lanzar_menu_tres_en_raya(ventana_actual):

    print("Lanzando el menú de Tres en Raya...")
    ventana_actual.destroy()
    crear_menu_principal()

def crear_lanzador_principal():
    root = tk.Tk()
    root.title("Lanzador de Proyectos de IA")
    root.config(bg=COLOR_FONDO, padx=50, pady=40)
    root.resizable(False, False)

    label_titulo = tk.Label(root, text="Selector de Proyectos",
                            font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_titulo.pack(pady=(0, 30))

    btn_tres_en_raya = tk.Button(root, text="Jugar Tres en Raya",
                                 font=FONT_BOTON, bg=COLOR_BOTON_PRINCIPAL, fg='#000000',
                                 relief='flat', padx=20, pady=15,
                                 command=lambda: lanzar_menu_tres_en_raya(root))
    btn_tres_en_raya.pack(fill='x', pady=10)

    btn_laberinto = tk.Button(root, text="Laberinto (Próximamente)", state='disabled',
                              font=FONT_BOTON, bg=COLOR_BOTON_SECUNDARIO, fg='#888888', relief='flat', padx=20, pady=15)
    btn_laberinto.pack(fill='x', pady=10)

    root.mainloop()

if __name__ == "__main__":
    crear_lanzador_principal()