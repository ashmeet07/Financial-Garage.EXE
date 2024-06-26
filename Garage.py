from tkinter import ttk, messagebox, Button, Label
from tkinter import *
import tkinter as tk
from Clean import CLEAN
from Setting import win, APPFRAME
from BalanceSheet import Balancesheet
from Main import PROFILE
import PandL
from UploadFiles import import_files


def GARAGE():
    CLEAN()
    win.title('Garage')

    # Define colors
    bg_color = '#1e1e1e'         # Dark background
    fg_color = '#ffffff'         # White text
    button_bg_color = '#ffcc00'  # Yellow button background
    button_fg_color = '#1e1e1e'  # Dark button foreground
    highlight_color = '#e74c3c'  # Red highlight color

    # Update frame periodically
    def update():
        APPFRAME.after(1000, update)

    update()

    # Top bar for icons
    top_bar = Frame(APPFRAME, bg=bg_color)
    top_bar.pack(side=TOP, fill=X, padx=0, pady=0)

    # Search icon button
    search_button = Button(top_bar, text="🔍", command=None, fg=button_fg_color, bg=button_bg_color,
                           font='Sans-serif 16 bold', width=2, height=1, relief=RAISED, bd=0)
    search_button.pack(side=LEFT, padx=0, pady=0)

    # File icon button
    file_button = Button(top_bar, text="📂", command=import_files, fg=button_fg_color, bg=button_bg_color,
                         font='Sans-serif 16 bold', width=2, height=1, relief=RAISED, bd=0)
    file_button.pack(side=LEFT, padx=0, pady=0)

    # Menu bar for menus
    menu_bar = Frame(APPFRAME, bg=bg_color)
    menu_bar.pack(side=TOP, fill=X, padx=0, pady=0)

    # Menu buttons
    menu_buttons = [
        ("📓 Balance Sheet", Balancesheet),
        ("💸 Profit/Loss", PandL.PROFIT_LOSS),
        ("📐 Analysis", win.destroy),
        ("💰 Cash Flow", win.destroy),
        ("↩ LOG OUT", PROFILE)
    ]

    for text, command in menu_buttons:
        menu_button = Button(menu_bar, text=text, command=command, fg=button_fg_color,
                             bg=highlight_color, font='Sans-serif 12 bold', width=20, height=2, relief=RAISED, bd=0)
        menu_button.pack(side=LEFT, padx=0, pady=0)


# Main loop
if __name__ == "__main__":
    GARAGE()
