import setuptools
from tkinter import *
from tkinter import colorchooser
from functools import partial

bombolist = ["Question1", "Question2", "Question3", ""]



class QuizProgam():
    def __init__(self):
        
        self.quiz_frame = Frame(padx=10, pady=10) 
        self.quiz_frame.grid()  
        

        
        self.quiz_heading = Label(self.quiz_frame, text="Multi-Question Quiz",font=("YU Gothic UI Semibold","16","bold"))
        self.quiz_heading.grid(row=0 )

        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        self.QuestionOutput = Label(self.quiz_frame, text = bombolist[0],font=("YU Gothic UI Semibold","16","bold")  )
        self.QuestionOutput.grid(row=2)
        self.RedButton = Button(self.button_frame, text= "Red", bg= "#FF0000", fg= "#000000", relief=RIDGE, width=12)
        self.RedButton.grid(row =3, column = 1, padx=3, pady=5)

        self.GreenButton = Button(self.button_frame, text= "Green", bg= "#00ff00", fg= "#000000", relief=RIDGE, width=12)
        self.GreenButton.grid(row=3,column = 2, padx=3, pady=5)
        
        self.BlueButton = Button(self.button_frame, text= "Blue", bg= "#0000FF", fg= "#000000", relief=RIDGE, width=12)
        self.BlueButton.grid(row= 4, column = 1, padx=3, pady=5)
  
        self.YellowButton = Button(self.button_frame, text= "Yellow", bg= "#FFFF00", fg= "#000000", relief=RIDGE, width=12)
        self.YellowButton.grid(row=4, column = 2, padx=3, pady=5)
       
    



        
        










if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  QuizProgam()
  root.mainloop()