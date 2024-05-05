from datetime import date
import re


#if filename is blank, returns default name
#otherwise checks filename and either returns
#an error or returns the filename (with .txt extension)
def filename_maker(filename):
    #creates  default filename
    #(YYYY_MM_DD_temperature_calculations)
    if filename == "":


        filename_ok = ""
        date_part = get_date()
        filename = "{}_temperature_calculations".format(date_part)
    
    # checks file name has only a-z / A-Z/ underscores
    else:
        filename_ok = check_filename(filename)
    
    if filename_ok == "":
        filename += ".txt"
    
    else:
        filename = filename_ok
    
    return filename




#retreives data and creates a string in YYYY_MM__DD Format
def get_date():
    today = date.today()

    #get day, month and year as individual in strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y") 

    
    return "{}_{}_{}".format(year, month, day)


# checks that filename only contains letters
# numbers and underscores. Returns either "" if
# OK or the problem if we have an error
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
        problem = "{}. Use letters / numbers / "\
                    "underscores only".format(problem)
    return problem










    



# *** main routine goes here ***
test_filenames = ["", "Test.txt","Test it ", "test" ]

for item in test_filenames:
    checked = filename_maker(item)
    print(checked)
    print()
    

