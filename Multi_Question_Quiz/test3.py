# Import the Tkinter library
from tkinter import *

# Create an instance of Tkinter window
self=Tk()

# Set the size of the window
self.geometry("300x300")

# Set the window background color
self.configure(bg="red")

#Uncomment below lines to use

# set the window background color using bg or background property
# window['bg'] = "#32a2a8"
# window['background'] = "#8732a8"

# Create a label widget
label=Label(self, text="Hello from Educative !!!").pack()

self.mainloop()