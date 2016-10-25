# 8.1
fruit = "banana"
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)
print()

# 8.2
fruit = "banana"
print(len(fruit))

length = len(fruit)
last = fruit[length - 1]
print(last)
print()
print(fruit[-1])
print(fruit[-2])
print()
print(fruit[:1])
print(fruit[0])
print()

# 8.3

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

print()

'''Exercise 1 - Write a function that takes a string as an argument and displays the letters backward, one per line.'''

def reversal_printer(str):
    index = len(str) - 1
    while index < len(str):
        character = str[index]
        print(character)
        index -= 1
        if index < 0:
            break


reversal_printer("Oklahoma")
print()
reversal_printer("Mississippi")
print()
reversal_printer("Roll Tide!")
print()

prefixes = "JKLMNOPQ"
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

print()

# Exercise 2

def duck_printer():
    prefixes = "JKLMNOPQ"
    suffix = 'ack'
    index = 0

    while index < len(prefixes):
        print(prefixes[index] + suffix)
        index += 1
        if index == len(prefixes) - 1:
            print(prefixes[index] + "u" + suffix)
            break


duck_printer()
print()

# 8.4  String slices

s = "Monty Python"
print(s[0:5])

print(s[6:12])
print()

fruit = "banana"
print(fruit[:3])
print(fruit[3:])

#Exercise 3
#Given that fruit is a string, what does fruit[:] mean?

print(fruit[:], "should be from beginning to end, a copy")
print()
# 8.5  Strings are immutable

immutabilty_test_string = "Strings are Immutable"
# immutabilty_test_string[0] = "F"
new_string = "X" + immutabilty_test_string[1:]
print(new_string)
print(immutabilty_test_string)
print()

# 8.6  Searching
# Exercise 4

def find_else(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find_else("Oklahoma", "a", 1), "= first match")

# 8.7
print()
# Exercise 5

def count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count

print(count("Oklahomans", "a"), "results found")
print(count("sheree", "e"), "results found")

print()
# Exercise 6

def count_better(word_to_parse, letter_to_find, starting_point):
    index = starting_point
    counts = 0
    while index < len(word_to_parse):
        if word_to_parse[index] == letter_to_find:
            counts += 1
            index += 1
        else:
            index += 1
        if index > len(word_to_parse):
            break
    return counts

print(count_better("Michelle Obamaaaaaa", "a", 1), "count")
print()
# 8.8  String methods

word = "Banana"
new_word = word.upper()
print(new_word)

index = word.find("a")
print(index)
print(word.find("na"))
print(word.find("na", 3))

name = "Bob"
print(name.find("B", 1, 2))
# this is a failure because it's not in the range specified

# Exercise 7
print()
new_stringy = "banana"
print(new_stringy.count("a"))
print()
my_name_string = "sheree maria pena-dominguez"
print(my_name_string.count("e"))
print()

# Exercise 8

print(my_name_string.capitalize())
print(my_name_string.center(50, "*"))
print(my_name_string.count("e"))
my_name_string = "Sheree María Peña-Domínguez"
#print(my_name_string.decode)
#looks to be 2 only, looks like I was looking at the wrong docs! whupz
print("Moving On")

print(my_name_string.casefold())
print(my_name_string.encode())
print("The sum of 5 + 6 is {0} and {1}".format(5 + 6, "foo"))
print()

# 8.9  The in operator

print("a" in "Sheree Maria Pena")
print("foo" in "there is a seed in my banana")
print()

def in_both(first_word, second_word):
    for letter in first_word:
        if letter in second_word:
            print(letter)

print(in_both("Sheree Maria Pena", "Charles Daniel Fried"))

print()
#8.10  String comparison

words = "bananas"
if words == "bananas":
    print("OK, bananas")

print()
if words < 'bananas':
    print('Your word,' + word + ', comes before bananas.')
elif words > 'bananas':
    print('Your word,' + word + ', comes after bananas.')
else:
    print('All right, bananas.')
#8.13  Exercises
print()
#Exercise 10

def is_palindrome(str):
    cleaned_up_string = str.replace(" ", "").casefold()
    return cleaned_up_string[::-1] == cleaned_up_string[:]

print(is_palindrome("sheree maria pena"))
print(is_palindrome("tacocat"))
print(is_palindrome("Mr Owl ate my metal worm"))
print()

