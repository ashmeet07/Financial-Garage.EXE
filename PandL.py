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
from Database_Chain import mysql as db
from Setting import win, x, APPFRAME, file, CHARTS, BALSHEETFILES, PLFILES
from UploadFiles import import_files
import Garage




def PROFIT_LOSS():
    CLEAN()
    PAL = os.listdir("D:\PROJECT_WORK\Final_Project\Profit&Losss")
    PLFILES.append(PAL)
    i = 0
    t = 100
    u = 100
    for x in PLFILES[i]:
            i += 1
            yearbut = Button(APPFRAME,
                             text=(str(x)),
                             background='saddlebrown',
                             foreground='white',
                             font='Sans-serif 9',
                             command=lambda k=x: my_fun(k),
                             wraplength=100, width=15
                             )
            yearbut.pack()
            yearbut.place(x=t, y=u)
            u += 50
    back = Button(APPFRAME,
                      text="Back",
                      command=Garage.GARAGE,
                      foreground='white',
                      background='#000064',
                      font='Sans-serif 10 bold',
                      width=6
                      )
    back.pack(pady=20)
    back.place(x=10, y=10)
    card1 = Label(APPFRAME,
                      width=25,
                      height=7,
                      background='sandybrown'
                      )
    card1.pack()
    card1.place(x=340, y=80)
    btn1 = Label(APPFRAME,
                     text='Charts',
                     font='Sans-serif 15 bold',
                     width=10,
                     background='sandybrown',
                     foreground="white",
                     anchor='sw'
                     )
    btn1.pack()
    btn1.place(x=360, y=90)
    btn2 = Button(APPFRAME,
                  text='📈',
                  font='Sans-serif 12',
                  background='saddlebrown',
                  foreground="white"
                  )
    btn2.pack()
    btn2.place(x=360, y=130)
    btn3 = Button(APPFRAME,
                  text='📶',
                  font='Sans-serif 12',
                  background='saddlebrown'
                  )
    btn3.pack()
    btn3.place(x=405, y=130)
    btn4 = Button(APPFRAME, text='⭕',
                  font='Sans-serif 12',
                  background='saddlebrown',
                  foreground="white"
                  )
    btn4.pack()
    btn4.place(x=450, y=130)
    btn5 = Button(APPFRAME,
                  text=':·.·',
                  font='Sans-serif 12',
                  background='saddlebrown',
                  foreground="white"
                  )
    btn5.pack()
    btn5.place(x=495, y=130)
    btn4 = Button(APPFRAME,
                  text='🌰',
                  font='Sans-serif 12',
                  background='saddlebrown'
                  )
    btn4.pack()
    btn4.place(x=360, y=180)
    btn4 = Button(APPFRAME,
                  text='🫧',
                  font='Sans-serif 12',
                  background='saddlebrown'
                  )
    btn4.pack()
    btn4.place(x=405, y=180)
    btn4 = Button(APPFRAME,
                  text='🗾',
                  font='Sans-serif 12',
                  background='saddlebrown',
                  foreground="white"
                  )
    btn4.pack()
    btn4.place(x=450, y=180)
    label = Label(APPFRAME,
                  text="",
                  width=80,
                  height=30,
                  background='grey'
                  )
    label.pack()
    label.place(x=600, y=30)
    def my_fun(k):
        if str(k) in PAL:
            HEAD = 'Balance sheet of the year ', k
            readfile = pd.read_csv("Profit&Losss/"+k)
            col = [col for col in readfile.columns]
            pd.set_option('display.max_rows', 66)
            s = ttk.Style()
            label = ttk.Treeview(APPFRAME, columns=(
                "c1", "c2"), show='headings', height=29)
            t = 0
            columns = []
            for i in col:
                label.column(t, width=321, anchor='nw')
                label.heading(t, text=str(i))
                columns.append(i)
                t += 1
            i = 0
            a, b = 0, 1
            particular = []
            amount = []
            for k, row in zip(readfile[columns[a]], readfile[columns[b]]):
                particular.append(k)
                pr = particular[i]
                amount.append(row)
                am = amount[i]
                label.insert("", "end", values=(pr, am))
                i += 1
            label.pack()
            label.place(x=600, y=30)
        else:
            label = Label(APPFRAME,
                          text="Enter Valid Year",
                          background='#FAFAF0',
                          foreground='#8B8B47',
                          font='Sans-serif'
                          )
            label.pack()
            label.place(x=500, y=0)