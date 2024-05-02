from tkinter import *   
from  functools import partial # To prevent unwanted windows 


class Converter:
    
    def __init__(self):
        #common format for all buttons
        #Arial size 14 bold, with white text 
        button_font = ("Arial","12","bold")
        button_fg = ("#FFFFFF")
        
        #five item list
        self.all_calculations = ["0 F° is -18 C°", "0 C° is 32 F°",
                               "30 F° is -1 C°", " 30 C° is 86 F°",
                                "40 F° is 4 C°"]

        
        #self.all_calculations = ["0 F is -18 C°", "0 C° is 32 F°",
                               #"30 F° is -1 C°", " 30 C° is 86 F°", 
                               #"40 F° is 4 C°"," 100 C° is 212 F° "]
                               
        #set up GUI frame#
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)
        
        self.to_history_button = Button(self.button_frame,text="History/export",bg="#004C99",
                                        fg=button_fg,font=button_font, width=12,state=DISABLED,command=lambda: self.to_history(self.all_calculations))
        self.to_history_button.grid(row=1,column=1,padx=5,pady=5)

        self.to_history_button.config(state=NORMAL)
    
    def to_history(self, all_calculations):
        HistoryExport(self, all_calculations)



class HistoryExport:

    def __init__(self, partner, calc_list):
        
        #set maximum number to 5, this can be changed if we want to show fewer or more calculations

        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

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
        self.text_instructions_label = Label(self.history_frame ,text=hist_text,width=45
                                             ,justify="left",wraplength=300, padx=10,pady=10)
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
        
        self.filename_error_label = Label(self.history_frame, text="Filename error goes here",fg="#9C0000",font=("Arial","12","bold"))
        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame) 
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame,font=("Arial","12","bold"), text= "Export",bg="#004C99", 
                                     fg="#FFFFFF", width=12) 
        self.export_button.grid(row=0,column=0, padx=10, pady=10)


        self.dismiss_button = Button(self.button_frame, font=("Arial","12","bold"), text= "Dismiss",bg="#666666", 
                                     fg="#FFFFFF", width=12, command=partial(self.close_history,partner))
        self.dismiss_button.grid(row=0,column=1 ,padx=10, pady=10)

    def get_calc_string(self, var_calculations):
        #get maximum calculations to dispaly

        max_calcs = self.var_max_calcs.get()
        calc_string = ""


        #work out how many times we need to loop
        #to output either the last five calculations or all the calculations
        if len(var_calculations) >= max_calcs:
            stop = max_calcs
        
        else:
            stop = len(var_calculations)
            
        #iterate to all but last item, additing item and line breaks to calculation string
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations) - item - 1]
            calc_string += "\n"

        #add final item without an xtra line break, eg: last item on list will be fifth from the end
        calc_string += var_calculations[-max_calcs]

        return calc_string
        

    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()
