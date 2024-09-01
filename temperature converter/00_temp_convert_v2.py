import setuptools
from tkinter import *
from tkinter import font
from functools import partial # To prevent unwanted windows 
from datetime import date
import re


class Converter():

    def __init__(self):

        #initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        #this variable is used when there is a problem
        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []
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
        instructions = "Please enter a temperature below and then press one of the buttons to convert it from Centrigrade to Fahrenheit"
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

        self.to_help_button = Button(self.button_frame, text = "Help/Info ", bg = "#CC6600", fg =button_fg, font=button_font, width = 12,command= self.to_help)
        self.to_help_button.grid(row=1 , column=0,padx=5,pady=5)
    
        self.to_history_button = Button(self.button_frame, text = "History/Export ", bg = "#004C99", fg =button_fg, font=button_font, width = 12,state=DISABLED ,command=lambda:self.to_history(self.all_calculations))
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
      
  
    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return"{:.0f}".format(var_rounded)
    
    #check the temperature is valid and convert it
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
            print(feedback)
            self.all_calculations.append(feedback)
            print(self.all_calculations)


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

    #opens history/export cuntion
    def to_history(self, all_calculations):
        HistoryExport(self, all_calculations)

    def to_help(self):
        DisplayHelp(self)
class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"
    
        self.help_box = Toplevel()
    
        #disable help button
        partner.to_help_button.config(state=DISABLED)

        #if user press cross at top, closes help menu and enables help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help,partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg= background)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg =background, text ="Help / info",font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert "\
                    "to either degrees Celsius (centigrade) or "\
                    "Fahrenheit..\n\n"\
                    "Note that -273 degrees C"\
                    "(-459 F) is absolute zero (the coldest possible "\
                    "temperature). If you try to convert a "\
                    "temperature that is less than -273 degrees C, " \
                    "you will get an error message. \n\n" \
                    "To see your "\
                    "calculation history and export it to a text " \
                    "file, please click the 'History / Export' button."
        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap = 350, justify="left")
        self.help_text_label.grid(row = 1, padx= 10)

        self.dismiss_button = Button(self.help_frame, font=("Arial","12","bold"), text= "Dismiss",bg="#CC6600", 
                                        fg="#FFFFFF", 
                                        command=partial(self.close_help,partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)
            

    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()

class HistoryExport:

    def __init__(self, partner, calc_list):
        
        
        #set maximum number to 5, this can be changed if we want to show fewer or more calculations

        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        #set variables to hold filename and date
        #for when writing to file
        self.var_filename = StringVar()
        self.var_todays_date = StringVar()
        self.var_calc_list = StringVar()
        calc_string_text = self.get_calc_string(calc_list)
    
        self.history_box = Toplevel()
        
        #disable help button
        partner.to_history_button.config(state=DISABLED)

        #if user press cross at top, closes help menu and enables help button
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history,partner))

        self.history_frame = Frame(self.history_box, width=300, height=200)

        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame, text ="History/Export",font=("Arial", "16", "bold"),justify="right")
        self.history_heading_label.grid(row=0)
        
        num_calcs = len(calc_list)

        if num_calcs > max_calcs:
            calc_background = "#FFE6CC"#PEACH
            showing_all = "Below are your recent calculations-(showing {}/{} calculations)"\
                          "To see your full calculation history, use the export button".format(max_calcs, num_calcs)
            

        else:
            calc_background = "#B4FACB" #PALE GREEN
            showing_all = "Below is your calculation history- (showing {}/{} Calculations)".format(max_calcs, num_calcs)
            

            
            
        hist_text="{}\n\nAll calculations are  shown to the nearest degree.".format(showing_all)
        self.text_instructions_label = Label(self.history_frame ,text=hist_text,width=45,justify="left",wraplength=300, padx=10,pady=10)
        self.text_instructions_label.grid(row=1)

        self.all_calcs_label = Label(self.history_frame, text=calc_string_text ,padx=10,pady=10,bg=calc_background,width="40",justify="left")
        self.all_calcs_label.grid(row=2)

        #instructions for saving files
        save_text ="Either choose a custom file name (and push Export) or simply push Export to save your calculations in a text file,"\
                    " If the filename already exists, it will be overwritten."

        self.save_instructions_label = Label(self.history_frame, text=save_text, wraplength="300",width="40",justify="left" )
        self.save_instructions_label.grid(row=3)
        
        self.filename_entry = Entry(self.history_frame,font=("Arial","14"),bg="#ffffff",width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)
        
        self.filename_feedback_label = Label(self.history_frame, text="",font=("Arial","12","bold"))
        self.filename_feedback_label.grid(row=5)

        self.button_frame = Frame(self.history_frame) 
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame,font=("Arial","12","bold"), text= "Export",bg="#004C99", 
                                     fg="#FFFFFF", width=12, command=self.make_file) 
        self.export_button.grid(row=0,column=0, padx=10, pady=10)


        self.dismiss_button = Button(self.button_frame, font=("Arial","12","bold"), text= "Dismiss",bg="#666666", 
                                     fg="#FFFFFF", width=12, command=partial(self.close_history,partner))
        self.dismiss_button.grid(row=0,column=1 ,padx=10, pady=10)
    
    def get_calc_string(self, var_calculations):
        #get maximum calculations to dispaly

        max_calcs = self.var_max_calcs.get()
        calc_string = ""

        #Generate for writing to file
        #oldest calculation first
        oldest_first = ""
        for item in var_calculations:
            oldest_first += item
            oldest_first += "\n"

        self.var_calc_list.set(oldest_first)

        #work out how many times we need to loop
        #to output either the last five calculations or all the calculations
        if len(var_calculations) >= max_calcs:
            stop = max_calcs
        
        else:
            stop = len(var_calculations)
            
        #iterate to all but last item, additing item and line breaks to calculation string
        for item in range(0, stop):
            calc_string += var_calculations[len(var_calculations) - item - 1]
            calc_string += "\n"

        calc_string = calc_string.strip()
        return calc_string
        #add final item without an xtra line break, eg: last item on list will be fifth from the end
    


    def make_file(self):
        #retrieve filename
        filename = self.filename_entry.get()

        filename_ok = ""
        date_part = self.get_date()
        if filename == "":
            #get date and create default filename
            
            filename = "_{}_temperature_conversions".format(date_part)
        else:
            #check that filename is valid   
            filename_ok = self.check_filename(filename)
        
        if filename_ok == "":
            filename +=".txt"
            success ="Success, your filename has been saved "\
                        "as {}".format(filename)
            self.var_filename.set(filename)
            self.filename_feedback_label.config(text=success,fg="#228B22")
            self.filename_entry.config(bg="#FFFFFF")

            #write content to file 
            self.write_to_file()

        else: 
            self.filename_feedback_label.config(text=filename_ok,fg="#9C0000")
            self.filename_entry.config(bg="#F8CECC")
           
            


    def get_date(self):
        today = date.today()

        #get day, month and year as individual in strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%y") 

        todays_date = "{}/{}/{}".format(day,month,year)
        self.var_todays_date.set(todays_date)

        
        return "{}_{}_{}".format(day,month,year)
    
    @staticmethod
    def check_filename(filename):
        problem = ""

        #regular expressions to check filename is valid
        valid_char = "[A-Za-z0-9_]"

        #iterates through filename and checks each letter
        for letter in filename:
            if re.match(valid_char, letter):
                continue


            elif letter ==  " " :
                problem = "Sorry no spaces alllowed"

            else:
                problem = ("Sorry, no {}'s allowed".format(letter))
            break
            
        if problem != "":
            problem = "{}. \n Use letters / numbers / underscores only".format(problem)
        return problem
    
    def write_to_file(self):
        filename = self.var_filename.get()
        generated_date = self.var_todays_date.get()

        #set up strings to be written onto file
        heading = "**** Temperature calculations   ****"
        generated = "Generated:{} \n".format(generated_date)
        subheading = "Here is your calcualtion history (oldest to newest)\n"

        all_calculations = self.var_calc_list.get()

        to_output_list = [heading, generated,subheading, all_calculations]

        text_file = open(filename, "w+")

        for item in to_output_list:
            text_file.write(item)
            text_file.write("\n")
        
        #closes text file
        text_file.close()
        

    #closes     
    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

### main routine ###

if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()