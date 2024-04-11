#get data from user and store it in a list
#then display the most recent three entries nicely

#set up list of calculations

all_calculations = []
MAX_CALCS = 5


#Get items of data
get_item =""
while get_item !="xxx":
    get_item = input("Enter an item:")

    if get_item == "xxx":
        break
    
    all_calculations.append(get_item)

print()
print("***The full list***")
print(all_calculations)

if len(all_calculations) >= MAX_CALCS:
    print() 
    print("***Most Recent 5***")
    for item in range(0, MAX_CALCS):
        print(all_calculations[len(all_calculations) - item - 1])

else: 
    print
    print("**items in order from newest to oldest***")
    for items in all_calculations:
        print(all_calculations[len(all_calculations)- all_calculations.index(item)- 1])
        