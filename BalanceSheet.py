# BalanceSheet.py

from tkinter import ttk, messagebox
import tkinter as tk
import pandas as pd
import os
from tkinter import *
from Clean import CLEAN
from Setting import win, APPFRAME, BALSHEETFILES
from UploadFiles import import_files


def Balancesheet():
    CLEAN()

    balance_sheets_dir = "C:\\Users\\OneDrive\\Documents\\Financial Garage\\BalanceSheets"
    balance_sheet_files = os.listdir(balance_sheets_dir)

    BALSHEETFILES.extend(balance_sheet_files)

    x_start = 150
    y_start = 80

    for idx, filename in enumerate(balance_sheet_files):
        yearbut = Button(
            APPFRAME,
            text=filename,
            background='saddlebrown',
            foreground='white',
            font='Sans-serif 9',
            command=lambda file=filename: my_fun(file)
        )
        yearbut.place(x=x_start, y=y_start + idx * 40)

    card1 = Label(APPFRAME, width=25, height=10, background='sandybrown')
    card1.place(x=340, y=80)

    details_buttons = [
        ('Assets', 90),
        ('Total Liability', 130),
        ('Total Equity', 170),
        ('Total Reserve/Surplus', 210),
        ('Total', 250)
    ]

    for text, y_pos in details_buttons:
        btn = Button(
            APPFRAME,
            text=text,
            font='Sans-serif 9',
            width=22,
            background='saddlebrown',
            foreground="white"
        )
        btn.place(x=360, y=y_pos)

    back = Button(
        APPFRAME,
        text="Back",
        command=lambda: GARAGE(),  # Use lambda to avoid import issue
        foreground='white',
        background='#000064',
        font='Sans-serif 10 bold',
        width=6
    )
    back.place(x=10, y=10)


def my_fun(selected_file):
    file_path = os.path.join(
        "C:\\Users\\OneDrive\\Documents\\Financial Garage\\BalanceSheets", selected_file)

    if os.path.exists(file_path):
        try:
            readfile = pd.read_csv(file_path)
            readfile.drop(columns='Column3', inplace=True, errors='ignore')

            treeview = ttk.Treeview(
                APPFRAME, columns=readfile.columns, show='headings', height=26)
            for col in readfile.columns:
                treeview.column(col, width=300, anchor='nw')
                treeview.heading(col, text=col)

            for index, row in readfile.iterrows():
                treeview.insert("", "end", values=tuple(row))

            treeview.place(x=600, y=20)

        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while reading the file: {e}")

    else:
        messagebox.showwarning(
            "File not found", f"File '{selected_file}' does not exist.")
