

import setuptools
from tkinter import *
from tkinter import font


class Converter():

  def __init__(self):

    #initialise variables (such as the feedback variable)
    self.var_feedback = StringVar()
    self.var_feedback.set("")

    #this variable is used when there is a problem
    self.var_has_error = StringVar()
    self.var_has_error.set("no")

    #common format for all buttons
    #Arial size 14 bold, with white text 
    button_font = ("Arial","14","bold")
    button_fg = ("#FFFFFF")

    #set up GUI frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    #heading/ instructions gui
    self.temp_heading = Label(self.temp_frame, text="Temperature Converter",font=("YU Gothic UI Semibold","16","bold"))
    self.temp_heading.grid(row=0 )
    instructions = "Please enter a temperature below and then press one of the buttons to convert it from centrigrade to farenheit"
    self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify = "left")
    self.temp_instructions.grid(row=1)
    
    #entry box
    self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
    self.temp_entry.grid(row=2, padx=10, pady=10)
    
    error = "Please enter a number"
    self.output_labelerror = Label(self.temp_frame, text ="", fg ="#9C0000")
    self.output_labelerror.grid(row=3)

    #Conversion, help and history / export buttons
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.to_celcius_button = Button(self.button_frame, text = "To Celcius", bg = "#990099", fg =button_fg, font=button_font, width = 12, command=lambda: self.temp_convert(-459))
    self.to_celcius_button.grid(row=0 , column=0,padx=5,pady=5)
   
    self.to_farenheit_button = Button(self.button_frame, text = "To Farenheit", bg = "#009900", fg =button_fg, font=button_font, width = 12, command=lambda:self.temp_convert(-273))
    self.to_farenheit_button.grid(row=0, column=1,padx=5,pady=5)

    self.to_help_button = Button(self.button_frame, text = "Help/Info ", bg = "#CC6600", fg =button_fg, font=button_font, width = 12)
    self.to_help_button.grid(row=1 , column=0,padx=5,pady=5)
   
    self.to_history_button = Button(self.button_frame, text = "History/Export ", bg = "#004C99", fg =button_fg, font=button_font, width = 12, state = DISABLED)
    self.to_history_button.grid(row=1 , column=1,padx=5,pady=5)
   
  def check_temp(self, min_value):
      has_error = "no"
      error = "Please ensure that the number is more than{}".format(min_value)
      #check that user has entered a valid 

      response = self.temp_entry.get()

      try:
          
          response = float(response)

          if response < min_value:
            has_error = "yes"
          
      except ValueError:
        has_error = "yes"

      #sets var_has_error so that entry box and labels can be correctly formated by
      #formating function
      if has_error == "yes":
        self.var_has_error.set("yes")
        self.var_feedback.set(error)
        return("invalid")
      
      #if there are no errors, do the normal shii
      else:
        self.var_has_error.set("no")

        #return number to be converted and enable history button
        self.to_history_button.config(state=NORMAL)
        return response
      
  #check the temperature is valid and convert it
  @staticmethod
  def round_ans(val):
    var_rounded = (val * 2 + 1) // 2
    return"{:.0f}".format(var_rounded)

  def temp_convert(self, min_val):
    
    to_convert = self.check_temp(min_val)
    set_feedback = "yes"
    answer = ""
    from_to = ""

    if to_convert == "invalid":
      set_feedback = "no"
    #convert to celcius
    elif min_val == -459:
      answer =(to_convert - 32) * 5 / 9
      from_to = "{} F° is {} C°"
      #do calculation
    
    #convert to farenheit
    else:
      answer = to_convert * 1.8  + 32
      from_to = "{} C° is {} F°"

    if set_feedback == "yes":
     to_convert = self.round_ans(to_convert)
     answer = self.round_ans(answer)

     feedback = from_to.format(to_convert, answer)
     self.var_feedback.set(feedback)

    self.output_answer()

  # Shows user output and clears entry widget
  # ready for next calculation
    
  def output_answer(self):
    output = self.var_feedback.get()
    has_errors = self.var_has_error.get()
    
    #if error occurs, label red, and entry box will be pink
    if has_errors == "yes":
      #red text, pink entry box
      self.output_labelerror.config(fg="#9C0000")
      self.temp_entry.config(bg="#F8CECC")
  
    
    #no issues, label wil be blue and entry box white
    else:
      self.output_labelerror.config(fg="#004C00")
      self.temp_entry.config(bg="#FFFFFF")
    
    self.output_labelerror.config(text=output)
### main routine ###

if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()