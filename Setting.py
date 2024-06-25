from tkinter import Tk, Frame, messagebox

try:
    # Initialize the main window
    win = Tk()
    win.title("Your Window Title")  # Set your window title here

    # Define screen resolutions
    x = ['1280x800', '1366x768', '1600x900', '1920x1080', '2256x1504',
         '2736x1824', '2560x1440', '3200x1800', '3200x1800']

    # Create main application frame
    APPFRAME = Frame(win)
    APPFRAME.pack(side="top", expand=True, fill="both")
    # Set your desired background color
    APPFRAME.configure(background='#FAFAF0')

    # Additional variables
    file = []
    CHARTS = ['Line Representation', 'Bar Representation',
              'Scatter Representation', 'Histo Representation']
    BALSHEETFILES = []
    PLFILES = []

except Exception as e:
    messagebox.showerror(
        "Error", f"An error occurred while initializing the application: {e}")

# Example usage or additional code if needed
