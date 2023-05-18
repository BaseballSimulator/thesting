import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

# Creating Tk window
root = Tk()
root.geometry("500x550")
root.title("Countdown Clock")

# Load and resize background image
background_image = Image.open("bg.jpg")
background_image = background_image.resize((500, 550), Image.ANTIALIAS)
background = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Styling for Entry and Button widgets
style = ttk.Style()
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry = ttk.Entry(root, width=3, textvariable=hour)
hourEntry.place(x=40, y=20)

minuteEntry = ttk.Entry(root, width=3, textvariable=minute)
minuteEntry.place(x=90, y=20)

secondEntry = ttk.Entry(root, width=3, textvariable=second)
secondEntry.place(x=130, y=20)

# Add styling to Entry widgets
hourEntry.config(style="TEntry")
minuteEntry.config(style="TEntry")
secondEntry.config(style="TEntry")

# Add a button for functionality
def start_timer():
    # Get the user input values
    hours = int(hour.get())
    minutes = int(minute.get())
    seconds = int(second.get())

    # Calculate the total seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Countdown loop
    while total_seconds >= 0:
        # Convert seconds to hours, minutes, and seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        # Update the entries with the remaining time
        hour.set(str(hours).zfill(2))
        minute.set(str(minutes).zfill(2))
        second.set(str(seconds).zfill(2))

        # Update the GUI
        root.update()

        # Delay of 1 second
        time.sleep(1)

        # Decrease the total seconds by 1
        total_seconds -= 1

    # Countdown finished
    messagebox.showinfo("Countdown Finished", "The countdown has ended!")

start_button = ttk.Button(root, text="Start", command=start_timer)
start_button.place(x=200, y=20)
start_button.config(style="TButton")

# Run the Tkinter event loop
root.mainloop()
