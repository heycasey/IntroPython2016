#!/usr/bin/env python

import os

direct = "/Users/isaacc/python-cert/IntroPython2016/Examples/Session01"
with open(os.path.join(direct, "students.txt"), "r") as in_file:
    language_list = []
    for line in in_file.readlines()[1:]:
        split_line = line.split(": ")
        if len(split_line) > 1:
            language_list.append(split_line[1].strip())

language_dict = {}

language_list = [l.split(", ") for l in language_list]

for lang_list in language_list:
    for lang in lang_list:
        if lang.strip() in language_dict:
            language_dict[lang.strip()] += 1
        else:
            language_dict[lang.strip()] = 1

print(language_dict)
print(list(language_dict.keys()))
