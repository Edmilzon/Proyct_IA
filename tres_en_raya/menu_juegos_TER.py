import tkinter as tk
import sys
import os
from tkinter import font as tkfont

sys.path.append(os.path.join(os.path.dirname(__file__), 'minimax'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'anchura'))

try:
    from juego_tres_en_raya_minimax_gui import iniciar_juego_minimax
except Exception:
    def iniciar_juego_minimax():
        tk.messagebox.showerror('Error', 'No se encontró la versión Minimax')

try:
    from juego_tres_en_raya_gui import iniciar_juego_bfs
except Exception:
    def iniciar_juego_bfs():
        tk.messagebox.showerror('Error', 'No se encontró la versión BFS')

BG = '#0b0f14'           
NEON_PRIMARY = '#7C4DFF'  
NEON_ACCENT = '#00E5FF' 
TEXT = '#E6F0FF'
BUTTON_BG = '#11121A'
BUTTON_ACTIVE = '#1E1B2D'
FONT_TITLE = ('Consolas', 22, 'bold')
FONT_SUB = ('Consolas', 10)
FONT_BTN = ('Consolas', 13, 'bold')


class Tooltip:
    def __init__(self, widget, text=''):
        self.widget = widget
        self.text = text
        self.tip = None

    def show(self, x=None, y=None):
        if self.tip:
            return
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.wm_attributes('-topmost', True)
        label = tk.Label(self.tip, text=self.text, bg='#0f1720', fg=TEXT,
                         font=FONT_SUB, bd=1, relief='solid', padx=6, pady=4)
        label.pack()
        if x is None or y is None:
            x = self.widget.winfo_rootx() + 20
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
        self.tip.geometry(f'+{x}+{y}')

    def hide(self):
        if self.tip:
            self.tip.destroy()
            self.tip = None


def crear_menu_principal(master_window):
    root = tk.Toplevel(master_window)
    root.title('Launcher - Tres en Raya')
    root.configure(bg=BG)

    def on_close():
        master_window.deiconify() # Mostramos la ventana principal de nuevo al cerrar esta
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_close)

    root.resizable(False, False)

    W, H = 520, 360
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w - W) // 2
    y = (screen_h - H) // 2
    root.geometry(f'{W}x{H}+{x}+{y}')

    header = tk.Frame(root, bg=BG)
    header.pack(fill='x', pady=(18, 6))

    title = tk.Label(header, text='TRES EN RAYA', font=FONT_TITLE, bg=BG, fg=NEON_PRIMARY)
    title.pack()

    subtitle = tk.Label(header, text='• Elige tu modo de IA', font=FONT_SUB, bg=BG, fg=NEON_ACCENT)
    subtitle.pack(pady=(4, 0))

    info_frame = tk.Frame(root, bg=BG, bd=0)
    info_frame.pack(fill='x', padx=28, pady=(8, 6))
    info_label = tk.Label(info_frame, text='Selecciona una opción para jugar. Atajos: M = Minimax, B = BFS, Esc = Salir',
                          bg=BG, fg=TEXT, font=FONT_SUB, anchor='w', justify='left')
    info_label.pack(fill='x')

    main_frame = tk.Frame(root, bg=BG)
    main_frame.pack(fill='both', expand=True, padx=28, pady=10)

    def lanzar_juego(juego_func, menu_window):
        menu_window.withdraw() # Ocultamos el menú del juego
        # Pasamos la ventana maestra (el lanzador principal) al juego
        juego_func(master_window)

    def make_button(parent, title_text, desc, cmd, key_hint=None):
        container = tk.Frame(parent, bg=BG)
        container.pack(fill='x', pady=8)

        btn = tk.Button(container, text=title_text, font=FONT_BTN,
                        bg=BUTTON_BG, fg=TEXT, activebackground=BUTTON_ACTIVE,
                        relief='flat', bd=0, padx=14, pady=10, anchor='w', command=cmd)
        btn.pack(fill='x')

        def on_enter(e):
            info_label.config(text=desc)
            btn.config(bg=NEON_PRIMARY, fg='#021018')

        def on_leave(e):
            info_label.config(text='Selecciona una opción para jugar. Atajos: M = Minimax, B = BFS, Esc = Salir')
            btn.config(bg=BUTTON_BG, fg=TEXT)

        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)

        tip = Tooltip(btn, text=(desc + (('\nAtajo: ' + key_hint) if key_hint else '')))

        def schedule_tooltip(e):
            btn._tt_after = btn.after(650, lambda: tip.show())

        def cancel_tooltip(e):
            if hasattr(btn, '_tt_after'):
                btn.after_cancel(btn._tt_after)
                delattr(btn, '_tt_after')
            tip.hide()

        btn.bind('<Enter>', schedule_tooltip, add='+')
        btn.bind('<Leave>', cancel_tooltip, add='+')

        return btn

    btn_minimax = make_button(main_frame, 'Jugar vs IA (Minimax)',
                              'IA invencible que usa el algoritmo Minimax. Ideal para un verdadero desafío.',
                              lambda: lanzar_juego(iniciar_juego_minimax, root), key_hint='M')

    btn_bfs = make_button(main_frame, 'Jugar vs IA (Busqueda por anchura)',
                          'IA con estrategia simple basada en búsqueda en anchura. Buena para entender la IA.',
                          lambda: lanzar_juego(iniciar_juego_bfs, root), key_hint='B')

    footer = tk.Frame(root, bg=BG)
    footer.pack(fill='x', side='bottom', pady=(6, 12))
    ver = tk.Label(footer, text='Launcher v1.0 • Gamer Theme', bg=BG, fg=NEON_ACCENT, font=FONT_SUB)
    ver.pack(side='left', padx=(28, 0))
    credits = tk.Label(footer, text='By Edmilzon', bg=BG, fg=TEXT, font=FONT_SUB)
    credits.pack(side='right', padx=(0, 28))

    root.bind('<m>', lambda e: btn_minimax.invoke())
    root.bind('<M>', lambda e: btn_minimax.invoke())
    root.bind('<b>', lambda e: btn_bfs.invoke())
    root.bind('<B>', lambda e: btn_bfs.invoke())
    root.bind('<Escape>', lambda e: on_close())

    glow_state = {'on': True}

    def pulse():
        if glow_state['on']:
            title.config(fg=NEON_PRIMARY)
        else:
            title.config(fg=NEON_ACCENT)
        glow_state['on'] = not glow_state['on']
        root.after(800, pulse)

    root.after(200, pulse)


if __name__ == '__main__':
    main_launcher = tk.Tk()
    main_launcher.withdraw() # Lo ocultamos si ejecutamos este archivo directamente
    crear_menu_principal(main_launcher)
    main_launcher.mainloop()
