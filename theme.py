from tkinter import ttk
from Setting import win, APPFRAME


def apply_theme():
    # Define your color palette
    bg_color = '#121212'  # Dark background
    fg_color = '#FFFFFF'  # White text
    btn_bg_color = '#009688'  # Teal
    btn_hover_color = '#00796B'  # Darker teal
    btn_active_color = '#004D40'  # Darkest teal

    # Set styles for different widgets
    win.configure(bg=bg_color)
    APPFRAME.config(bg=bg_color)

    ttk.Style().theme_use('clam')

    # Button style
    ttk.Style().configure('TButton',
                          background=btn_bg_color,
                          foreground='white',
                          font=('Arial', 14, 'bold'),
                          padding=10,
                          relief='flat')  # Note: Use 'flat' instead of ttk.FLAT
    ttk.Style().map('TButton',
                    background=[('active', btn_active_color), ('hover', btn_hover_color)])

    # Entry style
    ttk.Style().configure('TEntry',
                          fieldbackground=bg_color,  # Background color
                          foreground=fg_color,  # Text color
                          font=('Arial', 12),
                          padding=5,
                          borderwidth=2,
                          relief='flat')

    # If you have other widgets like Labels, Frames, etc., configure their styles here as well


# Apply the theme immediately upon import
apply_theme()
