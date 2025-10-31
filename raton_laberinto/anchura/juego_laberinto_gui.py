import tkinter as tk
from PIL import Image, ImageTk
import os

from manejador_juego_laberinto import ManejadorJuegoLaberinto
TAM_CELDA = 50

COLOR_FONDO = '#1a1a1a'         
COLOR_RUTA = '#00ffdd'          
COLOR_RUTA_BORDE = '#00aaff'   
COLOR_TEXTO = '#e0e0e0'      
COLOR_BOTON = '#5e00b3'      
COLOR_BOTON_HOVER = '#7a00e6' 

class LaberintoGUI:
    def __init__(self, master_window, laberinto_mapa):
        self.master = master_window
        self.root = tk.Toplevel(self.master)
        self.juego = ManejadorJuegoLaberinto(laberinto_mapa)

        try:
            self.img_camino = ImageTk.PhotoImage(Image.open("assets/camino.png").resize((TAM_CELDA, TAM_CELDA)))
            self.img_pared = ImageTk.PhotoImage(Image.open("assets/pared.png").resize((TAM_CELDA, TAM_CELDA)))
            self.img_raton = ImageTk.PhotoImage(Image.open("assets/raton.png").resize((TAM_CELDA, TAM_CELDA)))
            self.img_queso = ImageTk.PhotoImage(Image.open("assets/queso.png").resize((TAM_CELDA, TAM_CELDA)))
        except FileNotFoundError as e:
            print(f"Error: No se encontró una imagen. Asegúrate de que la carpeta 'assets' exista y contenga los archivos .png. Detalle: {e}")
            self.root.destroy()
            return

        def on_close():
            self.master.deiconify()
            self.root.destroy()
        self.root.protocol("WM_DELETE_WINDOW", on_close)

        self.root.title("Laberinto - Solución con Búsqueda por Anchura (BFS)")
        self.root.configure(bg=COLOR_FONDO)
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=self.juego.columnas * TAM_CELDA,
            height=self.juego.filas * TAM_CELDA,
            bg=COLOR_FONDO,
            highlightthickness=0
        )
        self.canvas.pack(padx=20, pady=20)
        self.canvas.bind("<Button-1>", self._manejar_clic_canvas)

        self.label_estado = tk.Label(
            self.root,
            text="Haz clic en una celda para mover el queso",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=('Consolas', 12)
        )
        self.label_estado.pack(pady=(0, 10))

        self.boton_iniciar = tk.Button(
            self.root,
            text="Buscar Queso",
            command=self.iniciar_busqueda,
            font=('Consolas', 12, 'bold'),
            bg=COLOR_BOTON,
            fg='white',
            relief='flat',
            padx=10,
            pady=5
        )
        self.boton_iniciar.pack(pady=(0, 20))
        self.boton_iniciar.bind("<Enter>", lambda e: e.widget.config(bg=COLOR_BOTON_HOVER))
        self.boton_iniciar.bind("<Leave>", lambda e: e.widget.config(bg=COLOR_BOTON))

        self.dibujar_laberinto()

    def _manejar_clic_canvas(self, event):
        c = event.x // TAM_CELDA
        f = event.y // TAM_CELDA

        if self.juego.actualizar_meta(f, c):
            print(f"Queso movido a la posición: ({f}, {c})")
            self.iniciar_busqueda()
        else:
            print(f"Posición inválida para el queso: ({f}, {c}) es una pared.")

    def dibujar_laberinto(self):
        self.canvas.delete("all")
        for f in range(self.juego.filas):
            for c in range(self.juego.columnas):
                x1, y1 = c * TAM_CELDA, f * TAM_CELDA
                x2, y2 = x1 + TAM_CELDA, y1 + TAM_CELDA
                
                if self.juego.laberinto[f][c] == '#':
                    self.canvas.create_image(x1, y1, image=self.img_pared, anchor='nw')
                else:
                    self.canvas.create_image(x1, y1, image=self.img_camino, anchor='nw')

                if (f, c) == self.juego.inicio:
                    self.canvas.create_image(x1, y1, image=self.img_raton, anchor='nw')
                elif (f, c) == self.juego.meta:
                    self.canvas.create_image(x1, y1, image=self.img_queso, anchor='nw')

    def iniciar_busqueda(self):
        self.dibujar_laberinto()
        self.boton_iniciar.config(state='disabled', text="Buscando...")
        self.label_estado.config(text="Ejecutando Búsqueda por Anchura...")
        self.root.update()

        ruta = self.juego.buscar_nueva_ruta()
        if ruta:
            self.label_estado.config(text=f"¡Ruta encontrada! Pasos: {len(ruta) - 1}")
            self.animar_ruta(ruta)
        else:
            self.label_estado.config(text="El ratón no puede alcanzar el queso.")
            self.boton_iniciar.config(state='normal', text="Buscar Queso")

    def animar_ruta(self, ruta, paso=1):
        if paso >= len(ruta):
            self.boton_iniciar.config(state='normal', text="Buscar Queso")
            return

        self.juego.inicio = ruta[paso]
        self.dibujar_laberinto()

        self.root.after(75, lambda: self.animar_ruta(ruta, paso + 1))


def iniciar_juego_anchura(master_window):
    LABERINTO_MAPA = [
        ['#', 'I', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#'],
        ['#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    
    app = LaberintoGUI(master_window, LABERINTO_MAPA)


if __name__ == "__main__":
    main_launcher = tk.Tk()
    main_launcher.withdraw()
    iniciar_juego_anchura(main_launcher)
    main_launcher.mainloop()
