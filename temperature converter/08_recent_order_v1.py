#get data from user and store it in a list
#then display the most recent three entries nicely

#set up list of calculations

all_calculations = []

#Get items of data
get_item =""
while get_item !="xxx":
    get_item = input("Enter an item:")

    if get_item == "xxx":
        break
    
    all_calculations.append(get_item)

all_calculations.reverse()

print()
print("***The full list***")
print(all_calculations)

print()

print("***Most Recent 5***")
for item in range(0,5):
    print(all_calculations[item])