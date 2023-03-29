print('Please enter with your sequences')

l1 = []
#open ended list
list1_input = input()
#major input for creating list
l1.append(list1_input)
#adding items to the list in specific order. this time at the end as that is what append does.
if list1_input == 'finished':
#This is the first bit of logic to see if new inputs should be created. Once they are it will consistently check for the value 'finished' or continue.
    print(f"{l1} contains all inputs you have made.")
while list1_input != 'finished':
    #this begins the loop process of adding items into the list.
    list1_input = input()
    l1.append(list1_input)
    print()
    #This is immediate user input feedback. Whenever they press [enter] they should have some response to indicate their value is being stored.#
    print(f"'{list1_input}' has just been added ") #Specific value is being stored#
    print()
    print(f"{l1} this is your current list of items added. as you press [enter] you will notice each input being stored.")
    #all values stored to the list are shown as a finished product to inform the user of what they are doing.
    if list1_input == 'finished':
        list1_input = l1.pop()
    #removes the final 'finished' from the end of the list.#
    else:
        print()
else:
    print(f"(Let's move on to the next section.")
print(l1)