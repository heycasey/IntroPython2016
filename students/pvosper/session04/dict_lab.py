#!/usr/bin/env python3

'''
When the script is run, it should accomplish the following four series of actions:

=== ONE ===
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).

=== TWO ===
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.

=== THREE ===
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).

=== FOUR ===
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’
display the union and intersection of the two sets.

'''

# Initial dictionaries and utilities

d = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'chocolate'}

# CHB: you can use the build in .count() method of sequences (including strings)

# str.count('s')


def count_s(str):
    tally = 0  
    for char in str:
        if char.lower() == 's':
            tally += 1
    return tally

d2 = {}
for key in d:
    d2[key] = count_s(d[key])

if __name__ == '__main__':
    print('\n=== ONE ===')

    print('\nDisplay the dictionary.')
    print(d)
    
    print('\nDelete the entry for “cake”.')
    d.pop('cake')
    
    print('\nDisplay the dictionary.')
    print(d)
    
    print('\nAdd an entry for “fruit” with “Mango” and display the dictionary.')
    d['fruit'] = "Mango"
    print(d)
    
    print('\nDisplay the dictionary keys.')
    print(d.keys())
    
    print('\nDisplay the dictionary values.')
    print(d.values())
    
    print('\nDisplay whether or not “cake” is a key in the dictionary (i.e. False) (now).')
    print("'cake' in d =", 'cake' in d)
    
    print('\nDisplay whether or not “Mango” is a value in the dictionary (i.e. True).')
    print("'Mango' in d.values() =", "Mango" in d.values())
    
    print('\n=== TWO ===')

    print('\nUsing the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.')

    print('\nDisplay the dictionary.')
    print(d2)
    
    print('\n=== THREE ===')
    
    print('\nCreate sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.')
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))
    
    print('\nDisplay the sets.')
    print('\ns2: ', s2)
    print('\ns3: ', s3)
    print('\ns4: ', s4)
    
    print('\nDisplay if s3 is a subset of s2 (False)')
    print(s3.issubset(s2))
    
    print('\nand if s4 is a subset of s2 (True).')
    print(s4.issubset(s2))