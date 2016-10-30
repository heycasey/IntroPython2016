#!/usr/bin/env python3


# Part 1

# Add fruits to a list. Assuming you're wanting to create a list rather than making a list manually.

fruits = []
fruits.append('Apples')
fruits.append('Oranges')
fruits.append('Pears')
fruits.append('Peaches')

print(fruits)

# Add fruits by prompt
fruits.append(input('What fruit would you like to add?: '))

print(fruits)

# Index the list with enumeration but labeling the number starting with 1. Then print the fruit selected from this index.
for fruit in enumerate(fruits, 1):
    print(fruit)
pick = int(input('Pick a number: ')) - 1
print(fruits[pick])


# Add a fruit to the end of list by using +
fruits = ['Grapes'] + fruits
print(fruits)

# Insert a fruit at the beginning of the list
fruits.insert(0, 'Watermelon')
print(fruits)

# Print only items that start with the letter P
for fruit in fruits:
    if fruit[0].upper() == 'P':
        print(fruit)

# Part 2

print(fruits)

# Remove the last item from the list
fruits.pop()

print(fruits)

# Prompt user for a fruit to remove
rm_fruit = input('What fruit would you like to remove? ')
fruits.remove(rm_fruit)

print(fruits)

# Didn't understand the bonus question.

# Part 3

# Ask user if they like a fruit. If they don't remove it. If they do, continue. But if they don't answer no or yes,
# re-prompt and ask for only yes or no answers. Maybe I should have done it all in a while loop but the instructions
# sounded like it was supposed to be just the last part.
# NEED TO FIX
for fruit in fruits:
    del_fruit = input('Do you like {}? '.format(fruit.lower()))
    if del_fruit.lower() != 'yes' or 'no':
        del_fruit = input('Do you like {}? Answer only yes or no '.format(fruit.lower()))
    elif del_fruit.lower() == 'no':
        fruits.remove(fruit)
    elif del_fruit.lower() == 'yes':
        pass


print(fruits)

# Part 4

# Make a shallow copy of fruits
fruits_copy = fruits.copy()

# Now reverse the spelling of every word in the copy list
for fruit in fruits_copy:
    print(fruit[::-1])

# Delete the last item in the original list then print both lists.
fruits.pop()

print(fruits)
print(fruits_copy)