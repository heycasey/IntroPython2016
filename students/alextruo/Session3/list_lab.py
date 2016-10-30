#!/usr/bin/env python3

#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit  = ["Apples", "Pears",  "Oranges", "Peaches"]
#Display the list.
print(fruit)
#Ask the user for another fruit and add it to the end of the list.
def first_function():
    new_fruit = input("Give me another fruit >" )
    #this appends the new fruit to the original list
    fruit.append(new_fruit)
    #Display the list.
    print(fruit)

    #Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
    number1 = (int(input("Give me a number >" )) )
    #this subtracts the 1, so the customer gets the 0th value, not 1
    number2 = number1 -1
    #take that number and put it into the index of the list so I can find it!
    print(number1, fruit[number2])

    #new_fruit2 = str(input("Give me a second fruit>"))
    #[new_fruit2] + fruit

    #ask for the third fruit
    new_fruit3 = str(input("Give me a another fruit>"))
    #inserts the fruit at 0
    fruit.insert(0, new_fruit3) 
    #prints the new list
    print(fruit)

    #returns all fruit that starts with "P"
    for items in fruit:
        if "P" in items:
            print("This starts with a 'P':", items)

    #this pops out the last itme in the list
    print("Good bye! You are the last fruit.", fruit.pop(-1))
    print(fruit)
    delete_fruit = input("What do you want to remove? ")
    if delete_fruit in fruit:
        #deletes the fruit from the list
        print("Goodbye {name}!".format(name = delete_fruit))
        fruit.remove(delete_fruit)
        #prints the new list
        print(fruit)

first_function()

# this is a duplicate list of fruit
def duplicate():
    duplicate_fruit = fruit * 2
    print("These are all the fruits in the original list:", fruit)
    delete_fruit = str(input("What fruit do you want to delete? "))
    while delete_fruit in duplicate_fruit:
        duplicate_fruit.remove(delete_fruit)
        print("\nThis is the with the fruit gone:", duplicate_fruit)
#call the function here
duplicate()

#Ask the user for input displaying a line like “Do you like apples?”
def yes_no():
    for item in fruit[:]:
    #ask if the user likes the fruit in the list
        favorite = input("Do you like: {name}? yes or no: ".format(name=item))
        if favorite == 'no':
            while item in fruit:
                fruit.remove(item)
                print("We are removing it.")
        elif favorite == 'yes':
            #skip to the next item in the list
            pass
        else:
            print("Sorry, try again please.")
    print("These are the suriving fruit.", fruit)
#call the function
yes_no()

def reverse_fruit():
    new_fruits = []
    for items in fruit:
        #this returns each item, which is a string, in reverse [start:finish:by numeral]
        new_fruits.append(items[::-1])
        #Display the original list with string formatter to replace the values; then pop off the last item of the list!
    print("This is the original {name}, minus the last one: {name2}.".format(name=fruit, name2=fruit.pop(-1)))
    print("This is the new list in reverse: ", new_fruits)

#call the function
reverse_fruit()

