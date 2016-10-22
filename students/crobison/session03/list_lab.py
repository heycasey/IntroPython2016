# Charles Robison
# 2016.10.15
# List Lab

#!/usr/bin/env python3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
str_length = len(fruits)

print("Here's the current list of fruits: ")
for i in fruits:
    print(i)

# Ask the user for another fruit and add it to the end of the list.
response = input("Please add another to the list: ")
fruits.append(response)
str_length = len(fruits)

print("Here's the updated list of fruits: ")
for i in fruits:
    print(i)

# Ask the user for a number and display the number back to the user
# and the fruit corresponding to that number (on a 1-is-first basis).
response = input("Pick a number from the list of fruits, equal to or less than " + str(str_length) + ":")

print("You picked " + fruits[int(response)-1] +".  Good choice!")

# Add another fruit to the beginning of the list using “+” and display the list.
response = input("Please add another to the list: ")
fruits = [response] + fruits

print("Here's the updated list of fruits: ")
for i in fruits:
    print(i)

# Add another fruit to the beginning of the list using insert()
# and display the list.
response = input("Please add another to the list: ")
fruits.insert(0, response)
print("Here's the updated list of fruits: ")
for i in fruits:
    print(i)

# Display all the fruits that begin with “P”, using a for loop.
print("Here are all the fruits in the list that begin with 'P': ")
for i in fruits:
    if i[0] == 'P':
        print(i)

# Display the list.
print("Here's the current list of fruits: ")
for i in fruits:
    print(i)

# Remove the last fruit from the list.
print("Now, we'll remove the last item. ")
last_item = len(fruits)-1
del fruits[last_item]

# Display the list.
print("Here's the updated list of fruits: ")
for i in fruits:
    print(i)

# Ask the user for a fruit to delete and find it and delete it.
response = input("Which item would you like removed? ")
fruits.remove(response)
print("Done - here's the current list: ")
for i in fruits:
    print(i)

# Ask the user for input displaying a line like “Do you like apples?”
# for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
# Display the list.

list_count = 0
while list_count < len(fruits):
    response = input("Do you like " + fruits[list_count] + "? y/n:")
    if response == 'n':
        del fruits[list_count]
        #list_count += 1
    elif response == 'y':
        list_count += 1
    else:
        print("Please answer only 'y' or 'n'")

print("Okay then, here are the fruits you do like: ")
for i in fruits:
    print(i)

# Make a copy of the list and reverse the letters in each fruit in the copy.
print("Here's the currently list backward: ")
back_fruit = fruits
for i in back_fruit:
    print(i[::-1])

# Delete the last item of the original list.
# Display the original list and the copy.
print("Deleting last item of original list: ")
del fruits[-1]
print("Here's the updated original list: ")
for i in fruits:
    print(i)

print("And here's the copy: ")
for i in back_fruit:
    print(i)














