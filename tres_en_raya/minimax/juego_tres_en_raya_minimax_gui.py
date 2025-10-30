import tkinter as tk
from tkinter import messagebox
import random
from motor_tres_en_raya import es_estado_final, obtener_movimientos_validos, aplicar_movimiento
from tresEnRaya_minimax import minimax

JUGADOR_HUMANO = -1  # 'O'
JUGADOR_IA = 1       # 'X'

COLOR_FONDO = '#1A1A1A'       
COLOR_TABLERO = '#1A1A1A'     
COLOR_BOTON = '#2C2C2C'    
COLOR_BOTON_HOVER = '#3C3C3C'   
COLOR_TEXTO = '#EAEAEA'         
COLOR_X = '#40E0D0'   
COLOR_O = '#FF4136'            
COLOR_ACCENT = '#9D4EDD'       
FONT_PRINCIPAL = ('Consolas', 14)
FONT_TABLERO = ('Consolas', 48, 'bold')

class TresEnRayaGUIMinimax:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya - Humano vs IA (Minimax)")
        self.estado_juego = [0] * 9
        self.botones = []
        self.crear_widgets()
        self.juego_terminado = False
        self.respuesta_inicio = None

        self.root.config(bg=COLOR_FONDO, padx=10, pady=10)
        self.label_estado = tk.Label(self.root, text="¡Bienvenido!", font=FONT_PRINCIPAL, bg=COLOR_FONDO, fg=COLOR_TEXTO)
        self.label_estado.grid(row=1, column=0, pady=(15, 20))
        
        self.iniciar_nuevo_juego()

    def crear_widgets(self):
        frame_tablero = tk.Frame(self.root, bg=COLOR_TABLERO, bd=5)
        frame_tablero.grid(row=0, column=0)

        for i in range(9):
            boton = tk.Button(frame_tablero, text=' ', font=FONT_TABLERO,
                              width=3, height=1,
                              bg=COLOR_BOTON, fg=COLOR_TEXTO, relief='flat', bd=5,
                              command=lambda i=i: self.click_humano(i))
            boton.grid(row=i//3, column=i%3, padx=3, pady=3)
            boton.bind("<Enter>", lambda e, b=boton: b.config(bg=COLOR_BOTON_HOVER, highlightbackground=COLOR_ACCENT, highlightthickness=2))
            boton.bind("<Leave>", lambda e, b=boton: b.config(bg=COLOR_BOTON, highlightthickness=0))
            self.botones.append(boton)

        boton_reiniciar = tk.Button(self.root, text="Reiniciar Juego", command=self.reiniciar_juego,
                                    font=FONT_PRINCIPAL, bg=COLOR_ACCENT, fg=COLOR_TEXTO,
                                    relief='flat', padx=10, pady=5)
        boton_reiniciar.grid(row=2, column=0, pady=(20, 10), sticky="ew")
        boton_reiniciar.bind("<Enter>", lambda e: e.widget.config(bg='#B57EE5'))
        boton_reiniciar.bind("<Leave>", lambda e: e.widget.config(bg=COLOR_ACCENT))

    def click_humano(self, indice):
        if self.juego_terminado or self.turno_actual != JUGADOR_HUMANO:
            return

        if self.estado_juego[indice] == 0:
            self.realizar_movimiento(indice, JUGADOR_HUMANO)

            if not self.juego_terminado:
                self.turno_actual = JUGADOR_IA
                self.label_estado.config(text="Turno de la IA. Pensando...")
                self.root.update() 
                self.root.after(500, self.movimiento_ia) 

    def dialogo_inicio(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("¿Quién empieza?")
        dialog.config(bg=COLOR_FONDO, padx=20, pady=20)
        dialog.resizable(False, False)
        dialog.transient(self.root)

        tk.Label(dialog, text="¿Deseas empezar primero?", font=FONT_PRINCIPAL, bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(0, 20))

        frame_botones = tk.Frame(dialog, bg=COLOR_FONDO)
        frame_botones.pack()

        btn_si = tk.Button(frame_botones, text="Sí", font=FONT_PRINCIPAL, bg=COLOR_O, fg=COLOR_TEXTO, relief='flat', padx=10, pady=5, command=lambda: self.cerrar_dialogo(dialog, True))
        btn_no = tk.Button(frame_botones, text="No", font=FONT_PRINCIPAL, bg=COLOR_X, fg=COLOR_TEXTO, relief='flat', padx=10, pady=5, command=lambda: self.cerrar_dialogo(dialog, False))
        btn_si.pack(side='left', padx=10)
        btn_no.pack(side='right', padx=10)

        self.root.wait_window(dialog) 

    def movimiento_ia(self):
        if self.juego_terminado:
            return

        print("\n--- Pensamiento de la IA (Minimax) ---")

        if all(casilla == 0 for casilla in self.estado_juego):
            print("Es el primer movimiento. Eligiendo una casilla al azar para variar el juego.")
            movimiento = random.choice(obtener_movimientos_validos(self.estado_juego))
            print(f"Decisión: Mover a la casilla {movimiento}.")
            self.realizar_movimiento(movimiento, JUGADOR_IA)
            self.turno_actual = JUGADOR_HUMANO
            self.label_estado.config(text="Tu turno")
            return

        print("Calculando el mejor movimiento con Minimax...")
        valor_optimo, movimiento = minimax(self.estado_juego, self.turno_actual)
        
        print(f"Minimax ha calculado un valor óptimo de {valor_optimo} para el estado actual.")
        print(f"El mejor movimiento para la IA es en la casilla: {movimiento}.")

        self.realizar_movimiento(movimiento, JUGADOR_IA)
        if not self.juego_terminado:
            self.turno_actual = JUGADOR_HUMANO
            self.label_estado.config(text="Tu turno")

    def realizar_movimiento(self, indice, jugador):
        if self.estado_juego[indice] != 0: return

        self.estado_juego = aplicar_movimiento(self.estado_juego, indice, jugador)
        simbolo = 'X' if jugador == JUGADOR_IA else 'O'
        color_simbolo = COLOR_X if simbolo == 'X' else COLOR_O
        
        boton = self.botones[indice]
        boton.config(state='disabled', disabledforeground=color_simbolo, text=simbolo)
 
        self.animar_aparicion(boton, simbolo, color_simbolo)

        self.verificar_estado_juego()

    def animar_aparicion(self, boton, simbolo, color_final, paso=0):
        if paso <= 10:
            nuevo_tamano = int(FONT_TABLERO[1] * (paso / 10.0))
            boton.config(font=(FONT_TABLERO[0], nuevo_tamano, FONT_TABLERO[2]))
            self.root.after(15, lambda: self.animar_aparicion(boton, simbolo, color_final, paso + 1))

    def verificar_estado_juego(self):
        resultado = es_estado_final(self.estado_juego)
        
        if resultado is not None:
            self.juego_terminado = True
            mensaje = ""
            if resultado == JUGADOR_IA:
                mensaje = "¡La IA ha ganado!"
                self.label_estado.config(text="La IA ha ganado.")
            elif resultado == JUGADOR_HUMANO:
                mensaje = "¡Felicidades, has ganado!"
                self.label_estado.config(text="¡Has ganado!")
            elif resultado == 0:
                mensaje = "¡Es un empate!"
                self.label_estado.config(text="Es un empate.")
            
            messagebox.showinfo("Fin del Juego", mensaje)

    def cerrar_dialogo(self, dialog, respuesta):
        self.respuesta_inicio = respuesta
        dialog.destroy()

    def iniciar_nuevo_juego(self):
        self.juego_terminado = False
        self.estado_juego = [0] * 9
        for boton in self.botones:
            boton.config(text=' ', state='normal', bg=COLOR_BOTON)

        self.dialogo_inicio()

        if self.respuesta_inicio:
            self.turno_actual = JUGADOR_HUMANO
            self.label_estado.config(text="Empiezas tú. ¡Haz tu movimiento!")
        else: 
            self.turno_actual = JUGADOR_IA
            self.label_estado.config(text="La IA empieza. Pensando...")
            self.root.after(500, self.movimiento_ia)

    def reiniciar_juego(self):
        self.iniciar_nuevo_juego()

def iniciar_juego_minimax():
    root = tk.Tk()
    juego = TresEnRayaGUIMinimax(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_juego_minimax()
