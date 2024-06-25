from tkinter import ttk, messagebox
from tkinter import *
import tkinter as tk
import pandas as pd
import numpy as np
import os
from Clean import CLEAN
from Database_Chain import mysql as db
from Setting import win, APPFRAME
from UploadFiles import import_files
from BalanceSheet import Balancesheet
from Main import PROFILE
import PandL


def GARAGE():
    CLEAN()
    win.title('Garage')

    # Define colors
    bg_color = '#f5f5f5'       # Light grey background
    fg_color = '#333333'       # Dark grey foreground
    button_bg_color = '#ffcc00'  # Yellow button background
    button_fg_color = '#333333'  # Dark grey button foreground
    highlight_color = '#e74c3c'  # Red highlight color

    # Update frame periodically
    def update():
        APPFRAME.after(1000, update)

    update()

    # Title label
    label = Label(APPFRAME, text="🛠 Garage", font=(
        "Sans-serif 29 bold"), background=bg_color, foreground=fg_color)
    label.pack(pady=20)

    # Buttons
    buttons = [
        ("📓 Balance Sheet", Balancesheet, 150),
        ("💸 Profit/Loss", PandL.PROFIT_LOSS, 200),
        ("📐 Analysis", win.destroy, 250),
        ("💰 Cash Flow", win.destroy, 300),
    ]

    for (text, command, y_pos) in buttons:
        button = Button(APPFRAME, text=text, width=30, command=command, foreground=button_fg_color,
                        background=button_bg_color, font='Sans-serif 13', relief=RAISED)
        button.pack(pady=10)
        button.place(relx=0.5, y=y_pos, anchor=CENTER)

    # Additional buttons with icons
    icon_buttons = [
        ("🔍", None, 600, 50),  # Placeholder for functionality
        ("📂", import_files, 600, 1190),
    ]

    for (text, command, y_pos, x_pos) in icon_buttons:
        button = Button(APPFRAME, text=text, command=command, foreground=button_fg_color, background=button_bg_color,
                        font='Sans-serif 20 bold', width=4, height=2, relief=RAISED)
        button.pack(pady=10)
        # Anchored to bottom-right corner
        button.place(x=x_pos, y=y_pos, anchor=SE)

    # Logout button
    logout = Button(APPFRAME, text="↩ LOG OUT", command=PROFILE, foreground=button_fg_color, background=highlight_color,
                    font='Sans-serif 10 bold', width=10, relief=RAISED, borderwidth=2)
    logout.pack(pady=20)
    logout.place(x=1180, y=10)


# Main loop
if __name__ == "__main__":
    GARAGE()
