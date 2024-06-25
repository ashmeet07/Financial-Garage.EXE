from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Required for working with images
from Clean import CLEAN
from Setting import win, APPFRAME
from Main import PROFILE  # Assuming PROFILE function is in Profile.py
from theme import apply_theme





def resize_image(image_path, width, height):
    """
    Resize the image at the given path to the specified width and height.
    Returns the resized Image object.
    """
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return resized_image


def WELCOME(RESOLUTION):
    CLEAN()
    win.geometry(RESOLUTION)
    apply_theme()  # Apply the defined theme

    # Load and display logo image
    logo_path = 'applogo.png'  # Adjust the path as per your file location
    logo_img = resize_image(logo_path, 100, 100)
    logo_photo = ImageTk.PhotoImage(logo_img)

    # Create a label with the welcome message
    welcome_label = Label(APPFRAME,
                          text='Welcome To Financial Garage',
                          background='#121212',
                          foreground='#FFFFFF',
                          font=('sans', 36, 'bold'),
                          anchor='center'
                          )
    welcome_label.place(relx=0.5, rely=0.6, anchor=CENTER)

    # Place the logo image on top of the welcome text
    logo_label = Label(APPFRAME, image=logo_photo, bg='#121212')
    logo_label.image = logo_photo  # Keep a reference to the image
    logo_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Function to destroy widgets and call PROFILE
    def proceed_to_profile():
        welcome_label.destroy()
        Go.destroy()
        logo_label.destroy()  # Destroy the logo label as well
        PROFILE()

    # Create a button to proceed
    Go = ttk.Button(APPFRAME,
                    text='Let\'s Go',
                    style='TButton',
                    command=proceed_to_profile,
                    width=20
                    )
    Go.place(relx=0.5, rely=0.8, anchor=CENTER)


# Main function to start the Tkinter application
if __name__ == "__main__":
    WELCOME('800x600')  # Adjust the resolution as needed
    win.mainloop()
