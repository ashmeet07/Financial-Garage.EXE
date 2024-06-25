from tkinter import ttk, messagebox
from tkinter import *
import os

from Setting import APPFRAME, x, win
from App import APP
from WelcomeApp import WELCOME

def create_directories():
    """Create necessary directories if they don't exist."""
    try:
        if not os.path.exists('BalanceSheets'):
            os.mkdir('BalanceSheets')
        if not os.path.exists('Profit&Losss'):
            os.mkdir('Profit&Losss')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while creating directories: {e}")

def initialize_styles():
    """Initialize custom styles for buttons."""
    try:
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Green.TButton', background='#388E3C',
                        foreground='white', font=('Helvetica', 12, 'bold'))
        style.configure('Orange.TButton', background='#D84315',
                        foreground='white', font=('Helvetica', 12, 'bold'))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while initializing styles: {e}")

def create_buttons():
    """Create buttons in a grid layout with custom styles."""
    try:
        for i, resolution in enumerate(x):
            btn_style = 'Green.TButton' if i % 2 == 0 else 'Orange.TButton'
            yearbut = ttk.Button(APPFRAME,
                                 text=f"🖥️  {resolution}",
                                 style=btn_style,
                                 command=lambda r=resolution: WELCOME(r),
                                 width=20)
            yearbut.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky='nsew')
        
        # Configure grid rows and columns to expand
        for i in range(2):  # Number of columns
            APPFRAME.grid_columnconfigure(i, weight=1)
        for i in range((len(x) + 1) // 2):  # Number of rows
            APPFRAME.grid_rowconfigure(i, weight=1)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while creating buttons: {e}")

def main():
    """Main function to set up the application."""
    try:
        create_directories()
        initialize_styles()
        create_buttons()
        
        # Bind a keyboard shortcut to quit the application
        win.bind('<Control-slash>', lambda e: win.quit())
        
        # Start the Tkinter main loop
        win.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
