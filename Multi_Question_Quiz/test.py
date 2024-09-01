import setuptools
from tkinter import *
from functools import partial




class MainMenu:
    def __init__(self):
        
        #self.menu_box = Toplevel()
        #self.menu_box.protocol("WM_DELETE_WINDOW", partial(self.close_menu))

        self.temp_frame = Frame(padx=10, pady= 10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Multi-Question Quiz",font=("YU Gothic UI Semibold","16","bold"))
        self.temp_heading.grid(row=0 )

        self.Sub_Heading = Label(self.temp_frame)
        self.Sub_Heading.grid() 
        
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.GameStartButton = Button(self.button_frame, text = "Play",  bg = "#990099", fg="#FFFFFF",relief=RIDGE,width=12)
        self.GameStartButton.grid(row=2, column = 0, padx=3, pady=3)

        self.SettingsButton =Button(self.button_frame, text = "Settings",  bg = "#990099", fg="#FFFFFF",relief=RIDGE,width=12)
        self.SettingsButton.grid(row=3, column = 0, padx=3, pady=3)

        self.QuitButton = Button(self.button_frame, text = "Quit",  bg = "#990099", fg="#FFFFFF",relief=RIDGE,width=12)
        self.QuitButton.grid(row=4, column = 0, padx=3, pady=3)

        self.button_test =Button(self.button_frame, text = "Quit",  bg = "#990099", fg="#FFFFFF",relief=RIDGE)
        self.button_test.grid(row=5, column = 3, padx=5, pady=5)





if __name__ == "__main__":
  root = Tk()
  #root.withdraw()
  root.title("Temperature Converter")
  MainMenu()
  root.mainloop()
