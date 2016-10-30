#!/usr/bin/env python3

person = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print(person)

# Remove the cake entry
person.pop('cake')

print(person)

# add entry for fruit
person['fruit'] = 'Mango'

print(person)

# Display just the keys
print(person.keys())

# Display just the values
print(person.values())

# Is cake a key?
if 'cake' in person:
    print('True')
else: print('False')

# Is mango a value?
if 'Mango' in person.values():
    print('True')
else: print('False')

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
weird_dict = person.copy()
for value in person:
    weird_dict[value] = person[value.lower()].count('t')
print(weird_dict)

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
s1 = set(range(0, 21))
def create_sets(str, div):
    results = []
    for i in s1:
        if i % div == 0:
            results.append(i)
            print('adding {}'.format(i))
            return str.add(results)
        else: pass

for i in s1:
    if i % 2 == 0:
        s2 = set(i)


print(s2)
#print(s3)
#print(s4)

