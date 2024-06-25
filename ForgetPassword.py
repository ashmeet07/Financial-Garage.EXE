from tkinter import ttk, messagebox
from tkinter import *
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
import random
import string
import mysql.connector
from Clean import CLEAN
from Setting import win, x, APPFRAME, file, CHARTS, BALSHEETFILES, PLFILES
from LogIn import LOGIN
from Database_Chain import mysql as db
import Garage
# Database connection


# Email settings
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"


def generate_temp_password():
    """Generate a random temporary password."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


def send_temp_password(email, temp_password):
    """Send the temporary password to the user's email."""
    try:
        msg = MIMEText(f"Your temporary password is: {temp_password}")
        msg['Subject'] = "Temporary Password"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, email, msg.as_string())

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def show_email_dialog():
    """Show the email dialog to send a temporary password."""
    email_window = Toplevel(win)
    email_window.title("Forgot Password")
    email_window.geometry("400x250")
    email_window.configure(bg='#EAF6F6')

    Label(email_window, text="Enter your email address:", font=(
        'Sans-serif', 14), bg='#EAF6F6', fg='#2B2D42').pack(pady=20)
    email_entry = Entry(email_window, width=30, font='Sans-serif')
    email_entry.pack(pady=10)

    def send_email():
        email = email_entry.get()
        cursor = db.cursor()
        cursor.execute("SELECT email FROM regist WHERE email = %s", (email,))
        result = cursor.fetchone()
        if result:
            temp_password = generate_temp_password()
            cursor.execute(
                "UPDATE regist SET temp_password = %s WHERE email = %s", (temp_password, email))
            db.commit()
            if send_temp_password(email, temp_password):
                messagebox.showinfo(
                    "Success", "Temporary password sent to your email.")
                email_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to send email.")
        else:
            messagebox.showerror("Error", "Email not found.")

    Button(email_window, text="Send", command=send_email,
           font='Sans-serif 12', bg='#FF6F61', fg='white').pack(pady=20)


def show_password_reset_dialog():
    """Show the password reset dialog."""
    reset_window = Toplevel(win)
    reset_window.title("Reset Password")
    reset_window.geometry("400x350")
    reset_window.configure(bg='#EAF6F6')

    Label(reset_window, text="Enter your email address:", font=(
        'Sans-serif', 14), bg='#EAF6F6', fg='#2B2D42').pack(pady=10)
    email_entry = Entry(reset_window, width=30, font='Sans-serif')
    email_entry.pack(pady=10)

    Label(reset_window, text="Enter the temporary password:", font=(
        'Sans-serif', 14), bg='#EAF6F6', fg='#2B2D42').pack(pady=10)
    temp_pass_entry = Entry(reset_window, width=30,
                            font='Sans-serif', show='*')
    temp_pass_entry.pack(pady=10)

    Label(reset_window, text="Enter your new password:", font=(
        'Sans-serif', 14), bg='#EAF6F6', fg='#2B2D42').pack(pady=10)
    new_pass_entry = Entry(reset_window, width=30, font='Sans-serif', show='*')
    new_pass_entry.pack(pady=10)

    def reset_password():
        email = email_entry.get()
        temp_password = temp_pass_entry.get()
        new_password = new_pass_entry.get()

        cursor = db.cursor()
        cursor.execute(
            "SELECT temp_password FROM regist WHERE email = %s", (email,))
        result = cursor.fetchone()
        if result and result[0] == temp_password:
            cursor.execute(
                "UPDATE regist SET password = %s, temp_password = NULL WHERE email = %s", (new_password, email))
            db.commit()
            messagebox.showinfo("Success", "Password changed successfully.")
            reset_window.destroy()
            LOGIN()
        else:
            messagebox.showerror("Error", "Invalid temporary password.")

    Button(reset_window, text="Reset", command=reset_password,
           font='Sans-serif 12', bg='#FF6F61', fg='white').pack(pady=20)


def FORGETPASSWORD():
    CLEAN()
    win.title('Change Password')

    bg_color = '#EAF6F6'
    fg_color = '#2B2D42'
    accent_color = '#FF6F61'

    label = Label(APPFRAME, text='📝 Change Password', font=(
        'Sans-serif', 29), foreground=fg_color, background=bg_color)
    label.place(relx=0.5, y=60, anchor=CENTER)

    send_email_button = Button(APPFRAME, text="Send Temporary Password", command=show_email_dialog,
                               font='Sans-serif 12', bg=accent_color, fg='white', width=25)
    send_email_button.place(relx=0.5, y=200, anchor=CENTER)

    reset_password_button = Button(APPFRAME, text="Reset Password", command=show_password_reset_dialog,
                                   font='Sans-serif 12', bg=accent_color, fg='white', width=25)
    reset_password_button.place(relx=0.5, y=300, anchor=CENTER)

    MainMenu = Button(APPFRAME, text="Main", command=Garage.GARAGE, foreground='white',
                      background=accent_color, font='Sans-serif 10 bold', width=6)
    MainMenu.place(x=10, y=10)

    # Copyright notice
    copyright_label = Label(APPFRAME, text="© Ashmeet Singh", font=(
        "Helvetica", 10, "italic"), bg=bg_color, fg=fg_color)
    copyright_label.place(relx=0.5, rely=0.95, anchor=CENTER)


# Main loop
if __name__ == "__main__":
    FORGETPASSWORD()
