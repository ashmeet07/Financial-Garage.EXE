from tkinter import ttk, messagebox
from tkinter import *
import tkinter as tk
import webbrowser
from Clean import CLEAN
from Database_Chain import mysql as db
from Setting import win, x, APPFRAME, file, CHARTS, BALSHEETFILES, PLFILES
from UploadFiles import import_files
import Main
# from Main import MAIN

# Function to open more information dialog


def open_more_info_dialog():
    def open_link(event):
        webbrowser.open_new("https://www.tatamotors.com")

    info_dialog = Toplevel(win)
    info_dialog.title("More Information")
    info_dialog.geometry("600x400")
    info_dialog.configure(bg="#FAFAF0")

    Label(info_dialog, text="Detailed Information", font=(
        "Helvetica", 20, "bold"), bg="#FAFAF0", fg="#10104E").pack(pady=20)
    info_text = (
        "This program helps to analyze Tata Motors annual report, providing insights on:\n"
        "- Whether the company bears loss or gains income.\n"
        "- Identify Company's Financial Condition.\n"
        "- Determine Company Net Profit As Well As Net Loss.\n"
        "- Also Determine Gross Profit/Loss.\n"
        "- Protection Of Assets.\n\n"
        "All Rights Are Reserved By (Tata Motors)\n"
        "© Ashmeet Singh\n"
        "For more information, visit our official website."
    )
    Label(info_dialog, text=info_text, font=("Helvetica", 14), bg="#FAFAF0",
          fg="#10104E", justify=LEFT, wraplength=550).pack(pady=10)

    link_label = Label(info_dialog, text="Tata Motors Official Website", font=(
        "Helvetica", 14, "underline"), bg="#FAFAF0", fg="blue", cursor="hand2")
    link_label.pack(pady=20)
    link_label.bind("<Button-1>", open_link)


def QUICKGUIDE():
    CLEAN()
    win.title('Program Information')
    bg_color = '#FAFAF0'
    fg_color = '#10104E'
    accent_color = '#FF5733'

    label = Label(APPFRAME, text='ℹ️ Program Information', foreground=fg_color, font=(
        'Helvetica 29 bold'), background=bg_color)
    label.place(relx=0.5, y=80, anchor=CENTER)

    info_text = (
        "------------------------------------------------------------------------------------\n"
        "This is a python based analysis program created by Ashmeet Singh which \n"
        "helps to analyze the Tata Motors annual report which helps to identify:\n"
        "- Whether the company bear loss or gain income.\n"
        "- Identify Companies Financial Condition.\n"
        "- Determine Company Net Profit As Well As Net loss.\n"
        "- Also Determine Gross Profit/Loss.\n"
        "- Protection Of Assets.\n"
        "All Rights Are Reserved By (Tata Motors)\n"
        "------------------------------------------------------------------------------------"
    )
    label = Label(APPFRAME, text=info_text, foreground=fg_color, font=(
        'Helvetica 17 bold'), background=bg_color, justify=LEFT, wraplength=1000)
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    MainMenu = Button(APPFRAME, text="Main", foreground='white',
                      background=accent_color,command=Main.PROFILE, font='Helvetica 12 bold', width=10)
    MainMenu.place(x=10, y=10)

    MoreInfo = Button(APPFRAME, text="More Info", command=open_more_info_dialog,
                      foreground='white', background=accent_color, font='Helvetica 12 bold', width=10)
    MoreInfo.place(relx=0.5, y=550, anchor=CENTER)

    # Copyright notice
    copyright_label = Label(APPFRAME, text="© Ashmeet Singh", font=(
        "Helvetica", 10, "italic"), bg=bg_color, fg=fg_color)
    copyright_label.place(relx=0.5, rely=0.95, anchor=CENTER)


# Main loop
if __name__ == "__main__":
    QUICKGUIDE()
