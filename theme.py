from tkinter import ttk
from Setting import win, APPFRAME


def apply_theme(theme):
    if theme == "dark":
        bg_color = '#121212'
        fg_color = '#FFFFFF'
        btn_bg_color = '#009688'
        btn_hover_color = '#00796B'
        btn_active_color = '#004D40'
    else:
        bg_color = '#F0F4F8'
        fg_color = '#2B2D42'
        btn_bg_color = '#007BFF'
        btn_hover_color = '#0056B3'
        btn_active_color = '#003580'

    win.configure(bg=bg_color)
    APPFRAME.config(bg=bg_color)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure('TButton',
                    background=btn_bg_color,
                    foreground='white',
                    font=('Arial', 14, 'bold'),
                    padding=10,
                    relief='flat')
    style.map('TButton',
              background=[('active', btn_active_color), ('hover', btn_hover_color)])

    style.configure('TEntry',
                    fieldbackground=bg_color,
                    foreground=fg_color,
                    font=('Arial', 12),
                    padding=5,
                    borderwidth=2,
                    relief='flat')


# Apply the dark theme by default upon import
apply_theme("dark")
