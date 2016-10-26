#!/usr/bin/env/python3
"""
LAB: Files
October 20, 2016
"""

import os

# Paths and File Processing
def list_files():

    cwd = os.getcwd()

    for file in os.listdir(cwd):
        print(os.path.abspath(file))
 
list_files()
print()


def copy_file(f_name):

    f_size = os.stat(f_name)
    f_size = f_size.st_size

    f = open(f_name,'rb')

    counter = 0
    output = open('copy_' + f_name,'wb')

    while counter <= f_size:
        f_section = f.read(counter)
        counter += 1
        output.write(f_section)

    output.close()
    f.close()
    print(f_name + " copied as copy_" + f_name)

copy_file('students.txt')
print()

# File reading and parsing

def process_file():
    
    lines = open('students.txt','r').readlines()

    del lines[0]

    dict_lang = {}

    for i in range(0,len(lines)):
        languages = lines[i].split(':')[-1]
        languages = languages.strip('" "\n\t')
        languages = languages.lower()
        languages = languages.split(',')

        for j in range(0,len(languages)):
            if languages[j] not in dict_lang.keys():
                dict_lang[languages[j]] = 1
            else:
                current = dict_lang[languages[j]]
                dict_lang[languages[j]] = current + 1

    print(dict_lang)

process_file()












