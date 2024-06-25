from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import pandas as pd
import numpy as np
import os
import shutil
import time
import tabulate as TB
from tkinter.filedialog import askopenfile
from Clean import CLEAN
from Database_Chain import DatabaseConnector as db
from Setting import win, x, APPFRAME, file, CHARTS, BALSHEETFILES, PLFILES
from UploadFiles import import_files


def charts():
    CLEAN()
    AL = Label(APPFRAME,
               text='Assets and Liability',
               width=20,
               background='forestgreen',
               foreground='white',
               anchor='center',
               font='Sans-serif 12 bold'
               )
    AL.pack()
    AL.place(x=0, y=50)
    x1 = 0
    y1 = 80
    for x in CHARTS:
        chart = Button(APPFRAME,
                           text=(str(x)),
                           background='steelblue',
                           foreground='white',
                           font='arial 9 bold',
                           width=20
                           )
        chart.pack()
        chart.place(x=x1, y=y1)
        y1 += 30
        CA = Label(APPFRAME,
                   text='Capital',
                   width=20,
                   background='forestgreen',
                   foreground='white',
                   anchor='center',
                   font='Sans-serif 12 bold'
                   )
        CA.pack()
        CA.place(x=0, y=200)
        x2 = 0
        y2 = 230
        for x in CHARTS:
            chart = Button(APPFRAME,
                           text=(str(x)),
                           background='steelblue',
                           foreground='white',
                           font='arial 9 bold',
                           width=20
                           )
            chart.pack()
            chart.place(x=x2, y=y2)
            y2 += 30
        PL = Label(APPFRAME,
                   text='Profit And Loss',
                   width=20,
                   background='forestgreen',
                   foreground='white',
                   anchor='center',
                   font='Sans-serif 12 bold'
                   )
        PL.pack()
        PL.place(x=0, y=350)
        x3 = 0
        y3 = 380
        for x in CHARTS:
            chart = Button(APPFRAME,
                           text=(str(x)),
                           background='steelblue',
                           foreground='white',
                           font='arial 9 bold',
                           width=20
                           )
            chart.pack()
            chart.place(x=x3, y=y3)
            y3 += 30
        EL = Label(APPFRAME,
                   text='Equity/Reserve&Surplus',
                   width=20,
                   background='forestgreen',
                   foreground='white',
                   anchor='center',
                   font='Sans-serif 12 bold'
                   )
        EL.pack()
        EL.place(x=0, y=500)
        x4 = 0
        y4 = 530
        for x in CHARTS:
            chart = Button(APPFRAME,
                           text=(str(x)),
                           background='steelblue',
                           foreground='white',
                           font='arial 9 bold',
                           width=20
                           )
            chart.pack()
            chart.place(x=x4, y=y4)
            y4 += 30
        back = Button(APPFRAME,
                      text="Back",
                      command=GARAGE,
                      foreground='white',
                      background='#000064',
                      font='Sans-serif 10 bold',
                      width=6
                      )
        back.pack(pady=20)
        back.place(x=10, y=10)
        label = Label(APPFRAME, text="", width=100,
                      height=20, background='grey')
        label.pack()
        label.place(x=300, y=50)
