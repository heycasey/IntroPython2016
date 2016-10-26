#!/usr/bin/env/python3
"""
LAB: Trigrams
October 20, 2016
"""

def trigram_fun():
    with open('sherlock.txt','r') as file_in:
        my_book = file_in.read()
    file_in.close()

    my_book = my_book.replace('\n', ' ')

    l_book = []
    l_book = my_book.split(' ')

    trigram_list = list(zip(l_book,l_book[1:],l_book[2:]))

    dict_list = {}
    for i in range(len(trigram_list)):
        tri_key = trigram_list[i][0] + ' ' + trigram_list[i][1]
        tri_value = trigram_list[i][2]
        if tri_key in dict_list:
            dict_list[tri_key].append(tri_value)
        else:
            dict_list[tri_key] = [tri_value]

    
    for k, v in dict_list.items():
        print('Keys:',k,'\n','Values:',v)


trigram_fun()