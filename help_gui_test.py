from tkinter import *   

class Converter:
    
    def __init__(self):
        #common format for all buttons
        #Arial size 14 bold, with white text 
        button_font = ("Arial","12","bold")
        button_fg = ("#FFFFFF")

        #set up GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)
        self.to_help_button = Button(self.button_frame, text = "help/info",bg="#CC6600", fg =button_fg, font=button_font, width=12, command=self.to_help)
        self.to_help_button.grid(row=1,column=0,padx=5,pady=5)
        
    @staticmethod
    def to_help():
        DisplayHelp()

class DisplayHelp():
    def __init__(self):
        background = "#ffe6cc"
        
        self.help_box = TopLevel()

        self.help_frame = Frame(self.help_box,)
        




### main routine ###

if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()