# PROFILE function in your main script

from tkinter import ttk, Frame, Label, BOTTOM, X, messagebox
from Setting import APPFRAME, win
from Quick_Guide import QUICKGUIDE
from LogIn import LOGIN
from ForgetPassword import FORGETPASSWORD
from SignUp import create_account
from Clean import CLEAN


def PROFILE():
    CLEAN()
    win.title('ANALYSIS APP')

    # Main Title
    title_label = Label(
        APPFRAME,
        text='Accounts',
        background='#121212',  # Use the dark background color directly
        foreground='#FFFFFF',  # Use the white text color directly
        font=('Arial', 36, 'bold')
    )
    title_label.place(relx=0.5, rely=0.2, anchor='center')

    # Helper function to create styled buttons
    def create_button(text, command, y_position):
        button = ttk.Button(
            APPFRAME,
            text=text,
            command=command,
            style='TButton',
            width=20  # Fixed width for all buttons
        )
        button.place(relx=0.5, y=y_position, anchor='center')
        return button

    # Create Account Button
    create_account_button = create_button(
        "📜 Create Account", create_account, 300)

    # Log In Button
    login_button = create_button("👤 Log In", LOGIN, 360)

    # Forgot Password Button
    forgot_password_button = create_button(
        "📝 Forgot Password", FORGETPASSWORD, 420)

    # Program Info Button
    guide_button = create_button("🛈 Program Info", QUICKGUIDE, 480)

    # Exit Button
    exit_button = ttk.Button(
        APPFRAME,
        text="🔜",
        command=win.destroy,
        style='TButton'
    )
    exit_button.place(x=10, y=10)

    # Profile Button
    profile_button = ttk.Button(
        APPFRAME,
        text="👤 Profile",
        command=lambda: messagebox.showinfo("Profile", "Profile details here"),
        style='TButton'
    )
    profile_button.place(relx=1.0, x=-10, y=10, anchor='ne')

    # Footer with welcome message
    footer_frame = Frame(APPFRAME, bg='#121212', height=50)
    footer_frame.pack(side=BOTTOM, fill=X)

    footer_label = Label(
        footer_frame,
        text='Welcome To Financial Garage',
        background='#121212',
        foreground='#FFFFFF',
        font=('Arial', 14, 'bold')
    )
    footer_label.pack(pady=10)


# Main function to start the Tkinter application
if __name__ == "__main__":
    PROFILE()
    win.mainloop()
