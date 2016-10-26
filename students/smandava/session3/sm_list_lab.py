#!/usr/bin/env python3
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print("Current Fruit Basket:", fruits)

f_input1 = input("Enter a fruit name to add to the list:")
fruits.append(f_input1)
print("Fruit Basket now:", fruits)

print("Enter a number less than or equal to:", len(fruits))
f_index = input()
if (int(f_index) > len(fruits)):
    print("Enter a number less than or equal to:", len(fruits))
else:
    print("Fruit at the index:", f_index, "is", fruits[int(f_index)])

f_input2 = input("Enter another fruit:")
fruits = [f_input2] + fruits
print("Fruit Basket now:", fruits)

f_input3 = input("Enter another fruit:")
fruits.insert(0, f_input3)
print("Fruit Basket now:", fruits)

# fruits that begin with “P”
print("The fruits starting with P:")
for fruit in fruits:
    if fruit[0] == 'P':
        print(fruit)

fruits.pop()
print("Fruit Basket now:", fruits)
f_input4 = input("Enter a fruit name to remove:")
fruits.remove(f_input4)
print("Fruit Basket now:", fruits)

# Bonus
bonus = fruits * 2
f_input5 = input("Enter a fruit name to remove:")
bonus_basket = [item for item in bonus if item != f_input5]
print("Bonus Fruit Basket now:", bonus_basket)

# Clear the Fruit Basket based on user input.
print("Enter 'Yes' or 'No':")
# fruits_copy = fruits[:]
index = 0
num = len(fruits)
while (index < num):
    print("Do you like ", fruits[index].lower(), "?")
    user_input = input()
    if (user_input == 'Yes'):
        index += 1
        continue
    elif (user_input == 'No'):
        del fruits[index]
        num = num - 1
        continue
    else:
        print("Please enter either Yes or No.")
        continue
print("Fruit Basket now:", fruits)

# Copy list and reverse the letters in each fruit
fruits_copy = fruits[:]
for fruit in fruits_copy:
    r_fruit = fruit[::-1]
    print(r_fruit)

fruits.pop()

print("Fruit Basket now:", fruits)
print("Fruit Basket now:", fruits)
print("Copy of Fruit Basket now:", fruits_copy)
