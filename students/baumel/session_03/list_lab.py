#!/usr/bin/env python3




#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
#Display the list.
print(fruit)
#Ask the user for another fruit and add it to the end of the list.
new_fruit = input("Enter another Fruit: ")
fruit.append(new_fruit)
#Display the list.
print(fruit)
#Ask the user for a number and display the number back to the user and 
#the fruit corresponding to that number (on a 1-is-first basis).
num = eval(input("Enter a number: "))
print('You Entered ',num,' which is ',fruit[(num-1)],' in the list')
#Add another fruit to the beginning of the list using “+” and display the list.
new_fruit1 = input("Enter another Fruit: ")
fruit = [new_fruit1] + fruit
print(fruit)
#Add another fruit to the beginning of the list using insert() and display the list.
new_fruit2 = input("Enter another Fruit: ")
fruit.insert(0,new_fruit2)
print(fruit)
#Display all the fruits that begin with “P”, using a for loop.
length = len(fruit)
for i in range (0,length):
    #print(fruit[i])
    if fruit[i][0]=='p' or fruit[i][0]=='P':
        print (fruit[i])

"""part two of lab"""
#Display the list.
print (fruit)
#Remove the last fruit from the list.
del fruit[-1]
#Display the list.
print(fruit)
#Ask the user for a fruit to delete and find it and delete it.
fruit_remove = input("Enter a Fruit to remove: ")
fruit.remove(fruit_remove)
print(fruit)

"""Part 3 of Lab"""
#Ask the user for input displaying a line like “Do you like apples?”
for i in fruit:
    print("do you like ",i)
    likes = input("Enter (y/n): ")
    if likes == 'n':
        i = 'remove'
fruit.remove('remove')
fruit.lower()
#for each fruit in the list (making the fruit all lowercase).
#For each “no”, delete that fruit from the list.
#For any answer that is not “yes” or “no”, prompt the user to answer 
#with one of those two values (a while loop is good here):
#Display the list.
print(fruit)





