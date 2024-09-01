from tkinter import *
from tkinter import colorchooser


self = Tk()
self.title=("MABAMBA")
self.geometry("400x400")

list = []
def color():
    color.hasbeencalled = True
    my_color = colorchooser.askcolor()[1]
    list.append(my_color)
    
    color_label= Label(self, text ="You picked a color!", font=("Helvetica, 32"), bg = my_color).pack()
    print(list)

color.hasbeencalled=False
if color.hasbeencalled == True:
    print("bombos") 
my_button = Button(self, text="Pick a Colour", command=color,).pack()

self.mainloop()
