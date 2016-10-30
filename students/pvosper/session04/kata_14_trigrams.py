#!/usr/bin/env python3

'''
Generate paragraphs of text based on trigrams within a source file.
'''

import random

sentance = ""
sentance_list = []

# text_string = '''
# Trigram analysis is very simple. Look at each set of three adjacent words in a 
# document. Use the first two words of the set as a key, and remember the fact 
# that the third word followed that key. Once you’ve finished, you know the list 
# of individual words that can follow each two word sequence in the document. 
# '''

# Read in file
# temp_file = open('sherlock_partial.txt')
temp_file = open('sherlock.txt')
text_string = temp_file.read().replace('\n', ' ')
temp_file.close()

# Remove upper case
text_string = text_string.lower()

# Fixups for Punctuation
text_string = text_string.replace('(', '')
text_string = text_string.replace(')', '')
text_string = text_string.replace('"', '')
text_string = text_string.replace(',', '')
text_string = text_string.replace('.', '')
text_string = text_string.replace('?', '')
text_string = text_string.replace('!', '')
text_string = text_string.replace('-', ' ') # Note space
text_string = text_string.replace(':', '')
text_string = text_string.replace(';', '')
text_string = text_string.replace("'", '')
text_string = text_string.replace('  ', ' ')

# Fixups for I and Roman numerals
text_string = text_string.replace(' i ', ' I ')
text_string = text_string.replace(' ii ', '')
text_string = text_string.replace(' iii ', '')
text_string = text_string.replace(' iv ', '')
text_string = text_string.replace(' v ', '')
text_string = text_string.replace(' vi ', '')
text_string = text_string.replace(' vii ', '')
text_string = text_string.replace(' vii ', '')
text_string = text_string.replace(' ix ', '')
text_string = text_string.replace(' x ', '')
text_string = text_string.replace(' xi ', '')
text_string = text_string.replace(' xii ', '')

# Fixups for personal names
text_string = text_string.replace(' holmes ', ' Holmes ')
text_string = text_string.replace(' sherlock ', ' Sherlock ')
text_string = text_string.replace(' irene ', ' Irene ')
text_string = text_string.replace(' adler ', ' Adler ')
text_string = text_string.replace(' mary ', ' Mary ')
text_string = text_string.replace(' jane ', ' Jane ')
text_string = text_string.replace(' watson ', ' Watson ')
text_string = text_string.replace(' godfrey ', ' Godfrey ')
text_string = text_string.replace(' norton ', ' Norton ')
text_string = text_string.replace(' boscombe ', ' Boscombe ')
text_string = text_string.replace(' sir ', ' Sir ')
text_string = text_string.replace(' arthur ', ' Arthur ')
text_string = text_string.replace(' conan ', ' Conan ')
text_string = text_string.replace(' doyle ', ' Doyle ')
text_string = text_string.replace(' hatherley ', ' Hatherley ')
text_string = text_string.replace(' venner ', ' Venner ')
text_string = text_string.replace(' matheson ', ' Matheson ')
text_string = text_string.replace(' rucastle ', ' Rucastle ')
text_string = text_string.replace(' sutherland ', ' Sutherland ')
text_string = text_string.replace(' duncan ', ' Duncan ')
text_string = text_string.replace(' ross ', ' Ross ')
text_string = text_string.replace(' moran ', ' Moran ')
text_string = text_string.replace(' wilson ', ' Wilson ')

# Fixups for place names
text_string = text_string.replace(' paris ', ' Paris ')
text_string = text_string.replace(' carlsbad ', ' Carlsbad ')
text_string = text_string.replace(' german ', ' German ')
text_string = text_string.replace(' briony ', ' Briony ')
text_string = text_string.replace(' bohemia ', ' Bohemia ')
text_string = text_string.replace(' scandinavia ', ' Scandinavia ')
text_string = text_string.replace(' eglow ', ' Eglow ')
text_string = text_string.replace(' england ', ' England ')
text_string = text_string.replace(' astrakhan ', ' Astrakhan ')
text_string = text_string.replace(' eglonitz ', ' Eglonitz ')
text_string = text_string.replace(' prague ', ' Prague ')
text_string = text_string.replace(' ulster ', ' Ulster ')
text_string = text_string.replace(' montana ', ' Montana ')
text_string = text_string.replace(' pondicherry ', ' Pondicherry ')
text_string = text_string.replace(' paddington ', ' Paddington ')
text_string = text_string.replace(' russian ', ' Russian ')
text_string = text_string.replace(' new zealand ', ' New Zealand ')

# Fixups for days of the week
text_string = text_string.replace(' monday ', ' Monday ')
text_string = text_string.replace(' tuesday ', ' Tuesday ')
text_string = text_string.replace(' wednesday ', ' Wednesday ')
text_string = text_string.replace(' thursday ', ' Thursday ')
text_string = text_string.replace(' friday ', ' Friday ')
text_string = text_string.replace(' saturday ', ' Saturday ')
text_string = text_string.replace(' sunday ', ' Sunday ')

# Fixups misc contractions and possessives
text_string = text_string.replace(' oclock ', " o'clock ")
text_string = text_string.replace(' mr ', " Mr. ")
text_string = text_string.replace(' mrs ', " Mrs. ")
text_string = text_string.replace(' jamess ', " James's. ")


# Create list
text_list = text_string.split()

# This strips all punctuation but introduces errors
# for i, entry in enumerate(text_list):
#     temp_string = ''
#     for char in entry:
#         if char.isalpha():
#             temp_string = temp_string + char.lower()
#     text_list[i] = temp_string

# $todo another day
'''
To find Proper Nouns, look for the NNP tag:

from nltk.tag import pos_tag

sentence = "Michael Jackson likes to eat at McDonalds"
tagged_sent = pos_tag(sentence.split())
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]

propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
# ['Michael','Jackson', 'McDonalds']
'''

# In trigrams dictionary, each value is a list of lists
trigrams = {}

# Build dictionary of trigrams
for i in range(len(text_list)-2):
    # I could make this one line, but then I would understand it even less
    key = text_list[i] + " " + text_list[i+1]
    val = [text_list[i+2]]
    trigrams.setdefault(key, []).append(val)

def pick_value(val_list):
    # random includes upper range value
    return val_list[random.randint(0, len(val_list) - 1)]
    
def make_sentance():
    sentance = ""
    seed = random.choice(list(trigrams.keys()))
    sentance_list = seed.split()
    for i in range(random.randint(8, 24)):
        seed = sentance_list[-2] + " " + sentance_list[-1]
        sentance_list.append(pick_value(trigrams[seed])[0])
    for word in sentance_list:
        sentance = sentance + " " + word
    sentance = sentance[1].upper() + sentance[2:] + '.'
    return sentance
    # $todo don't end sentences with joins like 'and', 'the', 'a'
    
def make_paragraph():
    paragraph = "   "
    for i in range(random.randint(3, 7)):
        paragraph = paragraph + " " + make_sentance()
    return paragraph

# 3 to 5 sentences per paragraph

if __name__ == '__main__':
    print('\n=== MAIN ===\n')
    
    print(make_paragraph())