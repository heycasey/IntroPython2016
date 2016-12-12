#comprehensions lab, Enrique Silva

# Print the dict by passing it to a string format method, so that you get something like:

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}


print('{name} is from {city}, and he likes {cake} cake, {fruit}, {salad}, {pasta}'.format(**food_prefs))

#list ocomprehension for storing values from a dicitonary.
list_comprehension=[value for value in food_prefs.values()]

print(list_comprehension)

#Using a list comprehension, build a dictionary of numbers from zero to
#fifteen and the hexadecimal equivalent (string is fine). (the hex()
#function gives you the hexidecimal representation of a number.

dict_hex_numbers={number:hex(number) for number in range(0,15,1)}

print(dict_hex_numbers)

#Using the dictionary from item 1: Make a dictionary using
#the same keys but with the number of ‘a’s in each value.

food_prefs_a={key:value.count('a') for key, value in food_prefs.items()}

print (food_prefs_a)

#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
n=5
sets = [{i for i in range(21) if not i % j} for j in range(2, n + 1)]

print(sets)