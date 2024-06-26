from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Clean import CLEAN
from Setting import win, APPFRAME
from Main import PROFILE
from theme import apply_theme

current_theme = "dark"


def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme(current_theme)
    WELCOME(win.geometry())


def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return resized_image


def create_toggle_switch(canvas, x, y, width, height, command):
    border_radius = height // 2

    # Draw background rectangle with rounded corners
    def draw_rounded_rect(x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1,
            x1+r, y1,
            x2-r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y1+r,
            x2, y2-r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x2-r, y2,
            x1+r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y2-r,
            x1, y1+r,
            x1, y1+r,
            x1, y1,
        ]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    rect = draw_rounded_rect(x, y, x + width, y + height,
                             border_radius, outline="", fill="#CCCCCC")

    # Draw toggle circle
    circle = canvas.create_oval(
        x + 2, y + 2, x + height - 2, y + height - 2, outline="", fill="#FFFFFF", width=0)

    def move_circle(event):
        current_pos = canvas.coords(circle)[0]
        move_to = x + width - height if current_pos < x + width / 2 else x + 2
        step = 1 if current_pos < move_to else -1

        def animate():
            nonlocal current_pos
            if step > 0:
                if current_pos < move_to:
                    canvas.move(circle, step, 0)
                    current_pos += step
                    canvas.after(10, animate)
            else:
                if current_pos > move_to:
                    canvas.move(circle, step, 0)
                    current_pos += step
                    canvas.after(10, animate)

        animate()
        command()

    canvas.tag_bind(rect, "<Button-1>", move_circle)
    canvas.tag_bind(circle, "<Button-1>", move_circle)


def WELCOME(RESOLUTION):
    CLEAN()
    win.geometry(RESOLUTION)
    apply_theme(current_theme)

    logo_path = 'applogo.png'
    logo_img = resize_image(logo_path, 100, 100)
    logo_photo = ImageTk.PhotoImage(logo_img)

    welcome_label = Label(APPFRAME,
                          text='Welcome To Financial Garage',
                          background='#121212' if current_theme == "dark" else '#F0F4F8',
                          foreground='#FFFFFF' if current_theme == "dark" else '#2B2D42',
                          font=('sans', 36, 'bold'),
                          anchor='center'
                          )
    welcome_label.place(relx=0.5, rely=0.6, anchor=CENTER)

    logo_label = Label(APPFRAME, image=logo_photo,
                       bg='#121212' if current_theme == "dark" else '#F0F4F8')
    logo_label.image = logo_photo
    logo_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    def proceed_to_profile():
        welcome_label.destroy()
        Go.destroy()
        logo_label.destroy()
        PROFILE()

    Go = ttk.Button(APPFRAME,
                    text='Let\'s Go',
                    style='TButton',
                    command=proceed_to_profile,
                    width=20
                    )
    Go.place(relx=0.5, rely=0.8, anchor=CENTER)

    toggle_canvas = Canvas(APPFRAME, width=60, height=30,
                           bg='#121212' if current_theme == "dark" else '#F0F4F8', highlightthickness=0)
    toggle_canvas.place(relx=0.95, rely=0.05, anchor=NE)

    create_toggle_switch(toggle_canvas, 0, 0, 60, 30, toggle_theme)


if __name__ == "__main__":
    WELCOME('800x600')
    win.mainloop()
