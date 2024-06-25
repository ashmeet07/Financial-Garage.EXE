from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
import os
import shutil
import time
from tkinter.filedialog import askopenfile
from Clean import CLEAN
from Setting import APPFRAME


class FileHandler:
    def __init__(self, app_frame):
        self.app_frame = app_frame
        self.selected_files = {1: None, 2: None, 3: None}

    def open_file(self, i):
        try:
            file_path = askopenfile(mode='r', filetypes=[
                                    ('CSV Files', '*.csv')])
            if file_path is not None:
                self.selected_files[i] = file_path.name
                messagebox.showinfo(
                    "File Selected", f"File selected for option {i}: {file_path.name}")
            else:
                messagebox.showwarning("Warning", "Please select a file")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def upload_files(self):
        try:
            for i, file_path in self.selected_files.items():
                if file_path is not None:
                    if i == 1:
                        dst_path = "C:/Users/ashme/OneDrive/Documents/Financial Garage/garage_pkg/BalanceSheets"
                    elif i == 2:
                        dst_path = "C:/Users/ashme/OneDrive/Documents/Financial Garage/garage_pkd/Profit&Losss"
                    elif i == 3:
                        dst_path = "C:/Users/ashme/OneDrive/Documents/Financial Garage/garage_pkg/OtherDirectory"

                    # Check if the file already exists in the destination directory
                    file_name = os.path.basename(file_path)
                    dst_file_path = os.path.join(dst_path, file_name)

                    if os.path.exists(dst_file_path):
                        response = messagebox.askyesno(
                            "File Exists", f"{file_name} already exists in destination. Do you want to replace it?")
                        if response:
                            shutil.move(file_path, dst_path)
                            messagebox.showinfo(
                                "Success", f"{file_name} replaced successfully.")
                    else:
                        shutil.move(file_path, dst_path)
                        messagebox.showinfo(
                            "Success", f"{file_name} moved successfully.")
                else:
                    messagebox.showwarning(
                        "Warning", f"No file selected for option {i}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def import_files():
    CLEAN()
    s = ttk.Style()
    s.configure("red.Horizontal.TProgressbar", background='brown4')
    pb1 = ttk.Progressbar(
        APPFRAME,
        orient=HORIZONTAL,
        length=300,
        mode='determinate',
        style="red.Horizontal.TProgressbar"
    )
    pb1.grid(row=4, columnspan=3, pady=20)
    pb1.place(relx=0.5, rely=0.05, anchor=CENTER)

    # Simulating progress bar
    for _ in range(5):
        APPFRAME.update_idletasks()
        pb1['value'] += 20
        time.sleep(0.2)

    pb1.destroy()

    file_handler = FileHandler(APPFRAME)

    # Creating buttons for each file type
    label1 = Label(APPFRAME,
                   text='Balance Sheet\n⛓️',
                   font='Sans-serif 15 bold',
                   width=15,
                   background='#FAFAF0'
                   )
    label1.pack()
    label1.place(relx=0.25, rely=0.3, anchor=CENTER)

    adharbtn = Button(
        APPFRAME,
        text='📖',
        command=lambda: file_handler.open_file(1),
        fg='white',
        bg='black',
        font='Sans-serif ',
        width=8,
        relief='flat',  # Remove border
        activebackground='darkred',  # Color when button is pressed
        activeforeground='white'
    )
    adharbtn.grid(row=0, column=1)
    adharbtn.place(relx=0.25, rely=0.4, anchor=CENTER)

    label2 = Label(APPFRAME,
                   text='P&L\n⛓️',
                   font='Sans-serif 15 bold',
                   width=8,
                   background='#FAFAF0')
    label2.pack()
    label2.place(relx=0.5, rely=0.3, anchor=CENTER)

    dlbtn = Button(
        APPFRAME,
        text='📝',
        command=lambda: file_handler.open_file(2),
        fg='white',
        bg='black',
        font='Sans-serif ',
        width=8,
        relief='flat',  # Remove border
        activebackground='darkblue',  # Color when button is pressed
        activeforeground='white'
    )
    dlbtn.grid(row=1, column=1)
    dlbtn.place(relx=0.5, rely=0.4, anchor=CENTER)

    label3 = Label(APPFRAME,
                   text='Other\n⛓️',
                   font='Sans-serif 15 bold',
                   width=8,
                   background='#FAFAF0')
    label3.pack()
    label3.place(relx=0.75, rely=0.3, anchor=CENTER)

    msbtn = Button(
        APPFRAME,
        text='🌐',
        command=lambda: file_handler.open_file(3),
        fg='white',
        bg='black',
        font='Sans-serif ',
        width=8,
        relief='flat',  # Remove border
        activebackground='darkgreen',  # Color when button is pressed
        activeforeground='white'
    )
    msbtn.grid(row=2, column=1)
    msbtn.place(relx=0.75, rely=0.4, anchor=CENTER)

    upld = Button(
        APPFRAME,
        text='📤 Upload',
        command=file_handler.upload_files,
        width=10,
        background='green',
        font='Sans-serif',
        foreground='white',
        relief='flat',  # Remove border
        activebackground='darkgreen',  # Color when button is pressed
        activeforeground='white'
    )
    upld.grid(row=3, columnspan=3, pady=10)
    upld.place(relx=0.5, rely=0.6, anchor=CENTER)

    back = Button(APPFRAME,
                  text="⬅️ Back",
                  command=APPFRAME.quit,
                  foreground='white',
                  background='#000064',
                  font='Sans-serif 13 bold',
                  width=10,
                  relief='flat',  # Remove border
                  activebackground='#0000A0',  # Color when button is pressed
                  activeforeground='white'
                  )
    back.pack(pady=20)
    back.place(x=10, y=10)

    profile = Button(APPFRAME,
                     text="👤",
                     command=lambda: messagebox.showinfo(
                         "Profile", "Profile details here"),
                     foreground='white',
                     background='#3e4444',
                     font='Sans-serif 20 bold',
                     width=3,
                     relief='flat',  # Remove border
                     activebackground='#e6e2d3',  # Color when button is pressed
                     activeforeground='white'
                     )
    profile.pack(pady=10)
    profile.place(relx=1.0, x=-10, y=10, anchor=NE)
