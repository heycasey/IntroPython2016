#!/usr/bin/env/python3
"""
LAB: Dictionary and Set Lab
October 18, 2016
"""

# Dictionary Section
dict_1 = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}

print('Dictionary 1: ',dict_1)

dict_1.pop('cake')

print('Dictionary 1: ',dict_1)

dict_1['fruit'] = 'Mango'

print('Dictionary 1: ',dict_1)

for keys in dict_1.keys():
    print('Keys: ',keys)

for values in dict_1.values():
    print('Values: ',values)

print('Is cake a key in the Dictionary 1? ' + str(('cake' in dict_1.keys())))

print('Is Mango a value in the Dictionary 1? ' + str (('Mango' in dict_1.values())))

total = 0
dict_2 = {}
for keys, values in dict_1.items():
    for letter in values:
        if letter == 't':
            total += 1
    dict_2[keys] = total
    total = 0
print('Dictionary 1: ', dict_1)
print('Dictionary 2: ', dict_2)

# Sets Section
s2 = set(range(0,21,2))
s3 = set(range(0,21,3))
s4 = set(range(0,21,4))

print('s2: ',s2)
print('s3: ',s3)
print('s4: ',s4)

print('Is s3 a subset of s2: ',s3.issubset(s2))
print('Is s4 a subset of s2: ',s4.issubset(s2))

s5 = set('Python')
s5.add('i')
s6 = frozenset('marathon')

print('Union of sets: ',s5.union(s6))
print('Intersection of sets: ',s5.intersection(s6))

