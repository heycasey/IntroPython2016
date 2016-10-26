#!/usr/bin/env python

# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
person = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}

def display_dict(dictionary):
    for key, value in dictionary.items():
        print(key + " : " + value)


# Display the dictionary.
display_dict(person)

# Delete the entry for “cake”.
del person["cake"]

# Display the dictionary.
display_dict(person)

# Add an entry for “fruit” with “Mango” and display the dictionary.
person["fruit"] = "mango"
display_dict(person)

# Display the dictionary keys.
print(person.keys())

# Display the dictionary values.
print(person.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("cake" in person)

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("mango" in person.values())

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
t_dict = {}
for key, value in person.items():
    t_dict[key] = "t" * len(value)
print(t_dict)

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
def make_divisible_set(divisor):
    set_list = [x for x in range(20) if x % divisor == 0]
    return set(set_list)

s2 = make_divisible_set(2)
s3 = make_divisible_set(3)
s4 = make_divisible_set(4)

# Display the sets.
print(s2, s3, s4)

# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))

# and if s4 is a subset of s2 (True)
print(s4.issubset(s2))

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
python = set(list("python"))
python.add("i")

# Create a frozenset with the letters in ‘marathon’
frozen = frozenset(list("marathon"))

# display the union and intersection of the two sets.
print(frozen.union(python))
print(frozen.intersection(python))
