import bcrypt
import csv
import os
from tkinter import *
from tkinter import ttk, messagebox
from Setting import APPFRAME
from Clean import CLEAN

# Constants for file paths
USERS_DATA_FILE = "users_data.csv"

# Global variables for GUI elements
username_entry = None
email_entry = None
password_entry = None
confirm_password_entry = None
terms_check = None

# Function to handle username validation


def username_validation(username):
    if len(username) == 0:
        messagebox.showerror("Invalid Username", "Username cannot be empty.")
        return False
    elif len(username) > 20:
        messagebox.showerror("Invalid Username",
                             "Username must be less than 20 characters.")
        return False
    elif not username.isalnum():
        messagebox.showerror(
            "Invalid Username", "Username must contain only alphanumeric characters.")
        return False
    else:
        return True

# Function to handle email validation


def email_validation(email):
    if len(email) == 0:
        messagebox.showerror("Invalid Email", "Email cannot be empty.")
        return False
    elif '@' not in email or '.' not in email:
        messagebox.showerror("Invalid Email", "Enter a valid email address.")
        return False
    else:
        return True

# Function to handle password validation


def password_validation(password):
    if len(password) < 10 or len(password) > 20:
        messagebox.showerror("Invalid Password",
                             "Password must be between 10 and 20 characters.")
        return False
    elif not any(char.isdigit() for char in password):
        messagebox.showerror("Invalid Password",
                             "Password must contain at least one digit.")
        return False
    elif not any(char.isupper() for char in password):
        messagebox.showerror(
            "Invalid Password", "Password must contain at least one uppercase letter.")
        return False
    elif not any(char.islower() for char in password):
        messagebox.showerror(
            "Invalid Password", "Password must contain at least one lowercase letter.")
        return False
    elif not any(char in '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?' for char in password):
        messagebox.showerror(
            "Invalid Password", "Password must contain at least one special character.")
        return False
    else:
        return True

# Function to handle password confirmation validation


def confirm_password_validation(password, confirm_password):
    if password != confirm_password:
        messagebox.showerror("Password Mismatch", "Passwords do not match.")
        return False
    else:
        return True

# Function to ensure terms and conditions are accepted


def terms_accepted():
    global terms_check
    if terms_check.get() == 0:
        messagebox.showerror("Terms not accepted",
                             "Please accept the terms and conditions.")
        return False
    else:
        return True

# Function to check if the user already exists


def check_user_exists(username, email):
    if os.path.exists(USERS_DATA_FILE):
        with open(USERS_DATA_FILE, "r", newline="") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                existing_username, existing_email, _ = row
                if username == existing_username or email == existing_email:
                    return True
    return False

# Function to save user data securely using bcrypt


def save_user_data(username, email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_password = hashed_password.decode(
        'utf-8')  # Convert bytes to string for storage

    with open(USERS_DATA_FILE, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([username, email, hashed_password])

# Function to submit the registration form


def submit_form():
    global username_entry, email_entry, password_entry, confirm_password_entry, terms_check

    username = username_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    confirm_password = confirm_password_entry.get().strip()

    if not (username_validation(username) and email_validation(email) and
            password_validation(password) and confirm_password_validation(password, confirm_password) and
            terms_accepted()):
        return

    if check_user_exists(username, email):
        messagebox.showerror("Error", "User already exists!")
        return

    save_user_data(username, email, password)
    messagebox.showinfo("Success", "Account created successfully!")
    CLEAN()

# Function to display terms and conditions


def show_terms():
    terms_window = Toplevel()
    terms_window.title("Terms and Conditions")
    terms_text = """
    Terms and Conditions:

    1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    2. Integer nec odio. Praesent libero.
    3. Sed cursus ante dapibus diam. Sed nisi.
    """
    terms_label = ttk.Label(terms_window, text=terms_text,
                            wraplength=500, justify=LEFT)
    terms_label.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Function to create the account registration form


def create_account():
    global username_entry, email_entry, password_entry, confirm_password_entry, terms_check

    CLEAN()

    # Define colors and fonts for the theme
    bg_color = "#f0f0f0"
    fg_color = "#333333"
    btn_bg_color = "#45A29E"
    btn_fg_color = "white"
    font_bold = ("Arial", 12, "bold")
    entry_bg_color = "#e0e0e0"

    # Create style for ttk widgets
    style = ttk.Style()
    style.configure("TFrame", background=bg_color)
    style.configure("TLabel", background=bg_color,
                    foreground=fg_color, font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12),
                    fieldbackground=entry_bg_color)
    style.configure("TButton", font=("Arial", 12, "bold"),
                    background=btn_bg_color, foreground=btn_fg_color)
    style.configure("TCheckbutton", font=("Arial", 10), background=bg_color)

    # Create a centered frame
    center_frame = ttk.Frame(APPFRAME, padding=20, style="TFrame")
    center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Title label
    title_label = Label(center_frame, text="Sign Up", font=(
        "Arial", 24, "bold"), fg="#2C3E50", bg=bg_color)
    title_label.grid(row=0, columnspan=2, pady=10)

    # Labels and Entries within center_frame
    username_label = Label(center_frame, text="Username:",
                           fg="#2980B9", font=("Arial", 12, "bold"), bg=bg_color)
    username_label.grid(row=1, column=0, sticky=E, pady=5, padx=5)
    username_entry = Entry(center_frame, width=30,
                           bg=entry_bg_color, font=("Arial", 12))
    username_entry.grid(row=1, column=1, pady=5, padx=5)

    username_tip = Label(center_frame, text="(Must be 1-20 characters, alphanumeric only)", font=("Arial", 10),
                         fg="#8E44AD", bg=bg_color)
    username_tip.grid(row=2, columnspan=2, pady=2)

    email_label = Label(center_frame, text="Email:",
                        fg="#2980B9", font=("Arial", 12, "bold"), bg=bg_color)
    email_label.grid(row=3, column=0, sticky=E, pady=5, padx=5)
    email_entry = Entry(center_frame, width=30,
                        bg=entry_bg_color, font=("Arial", 12))
    email_entry.grid(row=3, column=1, pady=5, padx=5)

    email_tip = Label(center_frame, text="(Must be a valid email address)", font=(
        "Arial", 10), fg="#8E44AD", bg=bg_color)
    email_tip.grid(row=4, columnspan=2, pady=2)

    password_label = Label(center_frame, text="Password:",
                           fg="#2980B9", font=("Arial", 12, "bold"), bg=bg_color)
    password_label.grid(row=5, column=0, sticky=E, pady=5, padx=5)
    password_entry = Entry(center_frame, show="*", width=30,
                           bg=entry_bg_color, font=("Arial", 12))
    password_entry.grid(row=5, column=1, pady=5, padx=5)

    password_tip = Label(center_frame, text="(10-20 chars, include upper, lower, digit, special)", font=("Arial", 10),
                         fg="#8E44AD", bg=bg_color)
    password_tip.grid(row=6, columnspan=2, pady=2)

    confirm_password_label = Label(center_frame, text="Confirm Password:", fg="#2980B9", font=("Arial", 12, "bold"),
                                   bg=bg_color)
    confirm_password_label.grid(row=7, column=0, sticky=E, pady=5, padx=5)
    confirm_password_entry = Entry(
        center_frame, show="*", width=30, bg=entry_bg_color, font=("Arial", 12))
    confirm_password_entry.grid(row=7, column=1, pady=5, padx=5)

    terms_check = IntVar()
    terms_checkbutton = Checkbutton(center_frame, text="I accept the Terms and Conditions", variable=terms_check,
                                    fg="#2980B9", font=("Arial", 10, "bold"), bg=bg_color)
    terms_checkbutton.grid(row=8, columnspan=2, pady=10)

    terms_button = Button(center_frame, text="Terms and Conditions", command=show_terms, font=font_bold,
                          bg=btn_bg_color, fg=btn_fg_color)
    terms_button.grid(row=9, columnspan=2, pady=10)
    submit_button = Button(center_frame, text="Submit", command=submit_form, font=font_bold,
                           bg=btn_bg_color, fg=btn_fg_color, width=20)
    submit_button.grid(row=10, column=0, columnspan=2, pady=10)


# Start Tkinter main loop
if __name__ == "__main__":
    if not os.path.exists(USERS_DATA_FILE):
        with open(USERS_DATA_FILE, "w", newline="") as file:
            pass  # Create an empty file if it doesn't exist
    create_account()
