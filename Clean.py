from tkinter import messagebox

from Setting import APPFRAME


# Clean.py

def CLEAN():
    global APPFRAME
    for widget in APPFRAME.winfo_children():
        widget.destroy()


