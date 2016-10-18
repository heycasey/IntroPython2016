#!/usr/bin/env python3

# Author: Darryl Wong
# Date: 10/15/2016
# Week 3 homework

list = ["apples", "pears", "oranges", "peaches"]

print (list)

# prompt the user for a fruit to add to our list
fruit = input ("Add a fruit: ")
list.append(fruit)

print (list)

# prompt the user for a fruit by index number
index = 0

while (index <=0) or (index > len(list)):
    index = int (input ("Enter a number from your list: " ))

index = index - 1

print ("list[index] = ", list[index])

# prompt the user for a fruit to add to the beginning of the list using "+"
fruit = input ("Add a fruit to the front: ")
list = [fruit] + list
print (list)

# prompt the user for a fruit to add to the beginning of the list using insert()
fruit = input ("Add a fruit to the front: ")
list.insert(0, fruit)
print (list)

# using a for loop display all the fruits that begin with "P"
for fruit in list:
	if fruit[0] == "p":
		print (fruit)

print ("Current list")
print (list)

# remove the last fruit from the list
list.pop()
print ("New list")
print (list)

# prompt the user for a fruit and remove it from the list
user_input = input ("Enter a fruit to remove from the list: ")
newlist = []
for fruit in list:
	if user_input != fruit:
		newlist = newlist + [fruit]

list = newlist[:]
print (list)
