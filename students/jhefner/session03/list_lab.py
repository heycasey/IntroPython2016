#!/Users/jhefner/python_dev/uw_python/bin/python

print("----------------")
print("List Lab Start")
print("----------------")

"""
When the script is run, it should accomplish the following four series of actions:
x Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
x Display the list.
x Ask the user for another fruit and add it to the end of the list.
x Display the list.
x Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
x Add another fruit to the beginning of the list using “+” and display the list.
x Add another fruit to the beginning of the list using insert() and display the list.
x Display all the fruits that begin with “P”, using a for loop.
"""
print("\n")
print("----------------")
print("Section 1")
print("----------------")
items = ["Apples", "Pears", "Oranges", "Peaches"]
print("Current List: ",items,"\n")

first_input = input("Please enter another fruit\n>>> ")
items.append(first_input)
print("Current List: ",items,"\n")


second_input_str = input("Please enter a number between 1 and 5\n>>> ")
second_input_int = int(second_input_str)
print("Your number is: "+second_input_str+"\nThe input you chose is: "+items[(second_input_int-1)],"\n")

items = ["Strawberries"]+items
print("Adding Strawberries to the list")
print("Current List: ",items,"\n")

items.insert(0, "Cherries")
print("Adding Cherries to the list")
print("Current List: ",items,"\n")

print("Printing all items that start with P")
for i in items:
    if i[0] == "P":
        print(i)

"""
Using the list created in series 1 above:
x Display the list.
x Remove the last fruit from the list.
x Display the list.
x Ask the user for a fruit to delete and find it and delete it.
* (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""
print("\n")
print("----------------")
print("Section 2")
print("----------------")
items2 = items[:]

print("Current List: ",items2,"\n")
print("Removing the last item: ",items2.pop())

print("Current List: ",items2,"\n")

third_input = input("Pick a number between 1 and 6\n>>> ")
print("Removing the item you picked: ",items2.pop((int(third_input)-1)))


"""
Using the list created in series 1 above:
x Display the list.
x Remove the last fruit from the list.
x Display the list.
x Ask the user for a fruit to delete and find it and delete it.
* (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""
print("\n")
print("----------------")
print("Section 3")
print("----------------")
items3 = items[:]

print("Current List: ",items3,"\n")
print("Removing the last item: ",items3.pop())

print("Current List: ",items3,"\n")

fourth_input = input("Type the name of a fruit from the list to remote it\n>>> ")
count=0
for i in items:
    count+=1
    if i == fourth_input:
        print("Removing the item you picked: ",items3.pop((count-1)))


"""
Again, using the list from series 1:
* Ask the user for input displaying a line like “Do you like apples?”
* For each fruit in the list (making the fruit all lowercase).
* For each “no”, delete that fruit from the list.
* For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
* Display the list.
"""
print("\n")
print("----------------")
print("Section 4")
print("----------------")
items4 = items[:]
repeat = True

print(items4)
count=0
for i in items4:
    z = i.lower()
    items4[count]=z
    count+=1

print ("All: ",items4)

while items4:
    fifth_input = input(">>> ")
#TODO: finish this later


"""
Once more, using the list from series 1:
* Make a copy of the list and reverse the letters in each fruit in the copy.
* Delete the last item of the original list. Display the original list and the copy.
"""
print("\n")
print("----------------")
print("Section 5")
print("----------------")
items5 = items[:]

