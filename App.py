from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import pandas as pd
import numpy as np
from Clean import CLEAN
from Database_Chain import mysql as db
from Setting import win
from tkinter import ttk, messagebox
from Clean import CLEAN
from Setting import win, APPFRAME
from Garage import GARAGE
from SignUp import create_account
from LogIn import LOGIN
from ForgetPassword import FORGETPASSWORD
from Quick_Guide import QUICKGUIDE







def APP(RESOLUTION):
    CLEAN()
    win.geometry(RESOLUTION)
    # APPICON = PhotoImage(file='applogo.png')
    # win.iconphoto(False, APPICON)
    ttk.Style().theme_use("clam")
    ttk.Label(foreground='#8B8B47')


    def typecasting(listofstrings):
        a = np.array(listofstrings)
        a1 = a.astype(np.float64)
        return a1

    def Asset_Liability(X):
        Year = year()
        assetdataofeachyear = []
        NCliability = []
        Cliability = []
        for Y in Year:
            read = pd.read_csv("BalanceSheet/"+Y+".csv", index_col='Particula')
            Dropextracolumn = read.drop(columns='Column3', inplace=True)
            assetfilter = read.loc['Total Assets'].values
            assetdataofeachyear.append(*assetfilter)
            NoneCurrenLiabilityfilter = read.loc['Total Non-Current Liabilities'].values
            CurrentLibilityfilter = read.loc['Total Current Liabilities'].values
            NCliability.append(*NoneCurrenLiabilityfilter)
            Cliability.append(*CurrentLibilityfilter)
        dataofasset = []
        dataofNCL = []
        dataofCL = []
        for (x, y, z) in zip(assetdataofeachyear, NCliability, Cliability):
            data1 = str(x).replace(",", "")
            data2 = str(y).replace(",", "")
            data3 = str(z).replace(",", "")
            dataofasset.append(data1)
            dataofNCL.append(data2)
            dataofCL.append(data3)
        a1 = typecasting(dataofasset)
        b1 = typecasting(dataofNCL)
        c1 = typecasting(dataofCL)
        TotalLiability = b1+c1
        if X == False:
            print("1.Values\n2.Exit")
            ch = choice()
            if ch == 1:
                val = yearchoice()
                for x, y, z in zip(TotalLiability, a1, Year):
                    if val == z:
                        print("The Total Liability Of The Company Is Rs", x,
                              "And The Total Asset Of The Company Is Rs", y, "Crores", "In", z)
            elif ch == 2:
                format()
            else:
                print("Enter Valid Choice")
        elif X == True:
            return TotalLiability, a1

    def MAIN():
        CLEAN()

        win.title('ANALYSIS APP')

        # Main Title
        title_label = Label(
            APPFRAME,
            text='Accounts',
            background='#FAFAF0',
            foreground='salmon2',
            font=('Sans-serif 29 bold')
        )
        title_label.place(relx=0.5, y=100, anchor=CENTER)

        # Create Account Button
        create_account_button = Button(
            APPFRAME,
            text="📜 Create Account",
            width=30,
            command=create_account,
            foreground='white',
            background='brown4',
            font='Sans-serif 13 bold'
        )
        create_account_button.place(relx=0.5, y=200, anchor=CENTER)

        # Log In Button
        login_button = Button(
            APPFRAME,
            text="👤 Log In",
            width=30,
            command=LOGIN,
            foreground='white',
            background='brown4',
            font='Sans-serif 13 bold'
        )
        login_button.place(relx=0.5, y=250, anchor=CENTER)

        # Forgot Password Button
        forgot_password_button = Button(
            APPFRAME,
            text="📝 Forgot Password",
            width=30,
            command=FORGETPASSWORD,
            foreground='white',
            background='brown4',
            font='Sans-serif 13 bold'
        )
        forgot_password_button.place(relx=0.5, y=300, anchor=CENTER)

        # Program Info Button
        guide_button = Button(
            APPFRAME,
            text="🛈 Program Info",
            width=30,
            command=QUICKGUIDE,
            foreground='white',
            background='brown4',
            font='Sans-serif 13 bold'
        )
        guide_button.place(relx=0.5, y=350, anchor=CENTER)

        # Go Button
        go_button = Button(
            APPFRAME,
            text='Lets Go',
            background='brown4',
            font='Sans-serif 10 bold',
            height=2,
            width=40,
            command=GARAGE,
            foreground='white',
            borderwidth='7'
        )
        go_button.place(relx=0.5, y=400, anchor=CENTER)

        # Welcome Label
        welcome_label = Label(
            APPFRAME,
            text='Welcome To Financial Garage',
            background='#FAFAF0',
            foreground='salmon1',
            font=('Sans-serif 29 bold')
        )
        welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Exit Button
        exit_button = Button(
            APPFRAME,
            text="🔜",
            command=win.destroy,
            foreground='white',
            background='brown4',
            font='Sans-serif 20'
        )
        exit_button.place(x=10, y=10)

        # Profile Button
        profile_button = Button(
            APPFRAME,
            text="👤 Profile",
            command=lambda: messagebox.showinfo("Profile", "Profile details here"),
            foreground='white',
            background='#000064',
            font='Sans-serif 10 bold',
            width=10
        )
        profile_button.place(relx=1.0, x=-10, y=10, anchor=NE)



    

