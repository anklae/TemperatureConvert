
from tkinter import *
from functools import partial



class MainMenu():
    def __init__(self):
      
        self.temp_frame = Frame(padx=10, pady= 10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Multi-Question Quiz",font=("YU Gothic UI Semibold","16","bold"))
        self.temp_heading.grid(row=0 )

        self.Sub_Heading = Label(self.temp_frame)
        self.Sub_Heading.grid
        
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.GameStartButton = Button(self.button_frame, text = "Play",  bg = "#990099", fg="#FFFFFF",relief=RIDGE,width=12)
        self.GameStartButton.grid(row=2, column = 0, padx=3, pady=3)

        self.SettingsButton =Button(self.button_frame, text = "Settings",  bg = "#990099", fg="#FFFFFF",relief=RIDGE,width=12)
        self.SettingsButton.grid(row=3, column = 0, padx=3, pady=3)

        

        

if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  MainMenu()
  root.mainloop()