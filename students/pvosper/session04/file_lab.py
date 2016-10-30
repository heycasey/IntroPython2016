#!/usr/bin/env python3

# === File Lab Exercises =====

# === Paths and File Processing =====

'''
write a program which prints the full path to all files in the current 
directory, one per line
write a program which copies a file from a source, to a destination (without 
using shutil, or the OS copy command)
'''

import os

print(os.getcwd(), ":")

directory_list = os.listdir()

for entry in directory_list:
    print("\t", entry)

# ====

f = open('temp_file.txt', 'w')
for i in range(100):
    f.write('All work and no play makes Jack a dull boy\n')
f.close()



# temp_file = open('../../../Examples/Session01/students.txt')
# text_string = temp_file.read()
# temp_file.close()

d = {}

for line in open('../../../Examples/Session01/students.txt'):
    s = []
    s = line.split(':')
    if len(s) == 2:
        d[s[0]] = s[1].replace('\n', ' ')
    else:
        d[s[0]] = '<n/a>'

# for entry in d:
#     print(entry)

# .strip().lower()

# f = open('myfile','w')
# f.write('hi there\n') # python will convert \n to os.linesep
# f.close() # you can omit in most cases as the destructor will call it

if __name__ == '__main__':
    print('\n=== MAIN ===\n')

#     print(d)
#     print(d.values())