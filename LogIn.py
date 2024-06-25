from tkinter import ttk, messagebox, Entry, Label, Button, GROOVE, RAISED
import tkinter as tk
import pandas as pd
import bcrypt
import os
from Clean import CLEAN  # Assuming CLEAN function is defined in Clean.py
from Setting import win, APPFRAME  # Assuming these are defined in Setting.py

# Global variables for Entry widgets
UN = None
PD = None

# Function to load user data from CSV (if it exists)


def load_users():
    filename = "users_data.csv"
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame(columns=["username", "email", "password_hash"])

# Function to hash a password


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to verify hashed password


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Function to perform login validation


def validate_login():
    username = UN.get()
    password = PD.get()

    if not username or not password:
        messagebox.showerror(
            "Login Failed", "Please enter both username and password.")
        return

    users = load_users()

    # Check if username exists in DataFrame
    user_data = users[users['username'] == username]

    if user_data.empty:
        messagebox.showerror(
            "Login Failed", "Invalid username or password. Please try again.")
    else:
        # Verify password
        stored_password_hash = user_data.iloc[0]['password_hash']
        if verify_password(password, stored_password_hash):
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            MAIN()  # Call your main function upon successful login
        else:
            messagebox.showerror(
                "Login Failed", "Invalid username or password. Please try again.")

# Function to setup the login screen


def LOGIN():
    CLEAN()
    win.title('LOGIN')

    # Define the theme colors and fonts
    bg_color = '#E8F8F5'  # Light teal background
    fg_color = '#0E6251'  # Dark teal for text
    accent_color = '#FF5733'  # Vibrant accent color
    button_bg_color = '#0E6251'  # Dark teal for buttons
    button_fg_color = '#FFFFFF'  # White text on buttons
    entry_bg_color = '#FFFFFF'  # White background for entry fields
    entry_fg_color = '#0E6251'  # Dark teal text in entry fields

    # Title label
    title_label = Label(APPFRAME, text="👤 LOGIN", font=(
        "Helvetica", 28, "bold"), bg=bg_color, fg=fg_color)
    title_label.place(relx=0.5, y=100, anchor=tk.CENTER)

    # Username label and entry
    username_label = Label(APPFRAME, text="Username", font=(
        "Helvetica", 18), bg=bg_color, fg=accent_color)
    username_label.place(relx=0.5, y=200, anchor=tk.CENTER)
    global UN
    UN = Entry(APPFRAME, font=("Helvetica", 14), bg=entry_bg_color,
               fg=entry_fg_color, relief=GROOVE, bd=2)
    UN.place(relx=0.5, y=240, anchor=tk.CENTER, width=300)

    # Password label and entry
    password_label = Label(APPFRAME, text="Password", font=(
        "Helvetica", 18), bg=bg_color, fg=accent_color)
    password_label.place(relx=0.5, y=300, anchor=tk.CENTER)
    global PD
    PD = Entry(APPFRAME, font=("Helvetica", 14), show='*',
               bg=entry_bg_color, fg=entry_fg_color, relief=GROOVE, bd=2)
    PD.place(relx=0.5, y=340, anchor=tk.CENTER, width=300)

    # Login button
    login_button = Button(APPFRAME, text="Login", command=validate_login, fg=button_fg_color,
                          bg=button_bg_color, font=("Helvetica", 14, "bold"), relief=RAISED, bd=3)
    login_button.place(relx=0.5, y=400, anchor=tk.CENTER, width=200)

    # Main menu button (assuming MAIN function is defined)
    main_menu_button = Button(APPFRAME, text="Main", command=MAIN, fg=button_fg_color,
                              bg=button_bg_color, font=("Helvetica", 12, "bold"), relief=RAISED, bd=3)
    main_menu_button.place(x=20, y=20)

# Placeholder function for main menu


def MAIN():
    messagebox.showinfo("Main Menu", "This is the main menu placeholder.")


# Main entry point for the application
if __name__ == "__main__":
    LOGIN()
    win.mainloop()
