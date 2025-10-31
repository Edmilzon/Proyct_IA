import tkinter as tk
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'tres_en_raya'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'raton_laberinto'))

from menu_juegos_TER import crear_menu_principal as crear_menu_ter
from menu_juego_lab import crear_menu_principal as crear_menu_laberinto

BG = '#0b0f14'         
NEON_PRIMARY = '#7C4DFF'  
NEON_ACCENT = '#00E5FF'  
TEXT = '#E6F0FF'  
BUTTON_BG = '#11121A' 
BUTTON_ACTIVE = '#1E1B2D'  
FONT_TITLE = ('Consolas', 28, 'bold')
FONT_SUB = ('Consolas', 12)
FONT_BTN = ('Consolas', 14, 'bold')

def lanzar_menu_tres_en_raya(ventana_actual):
    print("Lanzando el menú de Tres en Raya...")
    ventana_actual.withdraw() 
    crear_menu_ter(ventana_actual)

def lanzar_menu_laberinto(ventana_actual):
    print("Lanzando el menú del Laberinto...")
    ventana_actual.withdraw()
    crear_menu_laberinto(ventana_actual)

def make_styled_button(parent, text, command):
    btn = tk.Button(parent, text=text, font=FONT_BTN,
                    bg=BUTTON_BG, fg=TEXT, activebackground=BUTTON_ACTIVE,
                    activeforeground=NEON_ACCENT, relief='flat', bd=0,
                    padx=20, pady=15, anchor='w', command=command)
    
    def on_enter(e):
        btn.config(bg=NEON_PRIMARY, fg='#021018')

    def on_leave(e):
        btn.config(bg=BUTTON_BG, fg=TEXT)

    btn.bind('<Enter>', on_enter)
    btn.bind('<Leave>', on_leave)
    
    return btn

def crear_lanzador_principal():
    root = tk.Tk()
    root.title("Lanzador de Proyectos de IA")
    root.configure(bg=BG)
    root.resizable(False, False)

    W, H = 550, 420
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w - W) // 2
    y = (screen_h - H) // 2
    root.geometry(f'{W}x{H}+{x}+{y}')

    header = tk.Frame(root, bg=BG)
    header.pack(fill='x', pady=(25, 10))

    title = tk.Label(header, text="PROYECTOS IA", font=FONT_TITLE, bg=BG, fg=NEON_PRIMARY)
    title.pack()

    subtitle = tk.Label(header, text='• Selecciona un juego para empezar •', font=FONT_SUB, bg=BG, fg=NEON_ACCENT)
    subtitle.pack(pady=(4, 0))

    main_frame = tk.Frame(root, bg=BG)
    main_frame.pack(fill='both', expand=True, padx=40, pady=20)

    btn_tres_en_raya = make_styled_button(main_frame, "Tres en Raya", lambda: lanzar_menu_tres_en_raya(root))
    btn_tres_en_raya.pack(fill='x', pady=8)
    
    btn_laberinto = make_styled_button(main_frame, "Raton y el Queso (Laberinto)", lambda: lanzar_menu_laberinto(root))
    btn_laberinto.pack(fill='x', pady=8)

    footer = tk.Frame(root, bg=BG)
    footer.pack(fill='x', side='bottom', pady=(6, 12))
    ver = tk.Label(footer, text='Launcher v2.0 • Pro Gamer Edition', bg=BG, fg=NEON_ACCENT, font=('Consolas', 9))
    ver.pack(side='left', padx=(28, 0))
    credits = tk.Label(footer, text='By Edmilzon', bg=BG, fg=TEXT, font=('Consolas', 9))
    credits.pack(side='right', padx=(0, 28))

    glow_state = {'on': True}
    def pulse():
        if glow_state['on']:
            title.config(fg=NEON_PRIMARY)
        else:
            title.config(fg=NEON_ACCENT)
        glow_state['on'] = not glow_state['on']
        root.after(900, pulse)

    root.after(300, pulse)

    root.mainloop()

if __name__ == "__main__":
    crear_lanzador_principal()