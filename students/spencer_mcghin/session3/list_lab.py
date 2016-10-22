#!/usr/bin/env python3

"""Generate and display list of fruits"""
print("Here's a list of fruits:")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
for fruit in fruits:
    print(fruit)

"""Prompt user for another fruit and add to list and check to see if that fruit is in list already"""
new_fruit = input("Please enter a new fruit I should add to the list > ")
while new_fruit in fruits:
    new_fruit = input("Not cool. Enter a fruit that isn't in the list already > ")
else:
    fruits.append(new_fruit)
print("Your new list of fruits is:")
for fruit in fruits:
    print(fruit)

"""Prompt user for a number that corresponds to a fruit and return that number and fruit"""
new_number = int(input("Please give me a number from 1 to 5 > "))
while new_number > 5 or new_number <= 0:
    new_number = int(input("Quit being difficult and give me a number between 1 and 5 > "))
else:
    print("Item " + str(new_number) + " " + "is" + " " + fruits[new_number - 1])

"""Add another fruit to the beginning of the list and check to see if it is in the list already"""
first_fruit = [input("Now give me another fruit to add to the beginning of the list > ")]
while first_fruit in fruits:
    first_fruit = input("Not cool. Enter a a fruit that isn't in the list already > ")
else:
    new_fruits_list = first_fruit + fruits
print("Your new list of fruits is:")
for fruit in new_fruits_list:
    print(fruit)

"""Add another fruit to the beginning of the list using the .insert method"""
second_fruit = input("For the last time, give me a fruit to add to the list > ")
new_fruits_list.insert(0, second_fruit)
print("Your final list of fruits is...drumroll please...:")
for fruit in new_fruits_list:
    print(fruit)

"""Display the fruits that begin with P"""
print("Check it out everyone, we're going to print all the fruits that begin with P!")
for fruit in new_fruits_list:
    if fruit[0] == 'P':
        print(fruit)