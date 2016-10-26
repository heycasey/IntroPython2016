#!/usr/bin/env python

'''Writes a random text using trigrams from a supplied text.
Use:
$ python3 trigrams.py filename fileLength frontMatter endMatter
filename: file name, including file path
fileLength: an integer
frontMatter: file's front matter end string (must be in quotation marks, optional)
endMatter: file's end matter beginning string (must be in quotation marks, optional)'''


import random
from sys import argv


def make_trigrams(word_list):
    '''Return a dictionary of trigrams.
    word_list: a list of single words, in order, from a text'''
    trigrams = {}
    for x in range(len(word_list[:-2])):
        bigram = " ".join(word_list[x:x+2])
        if bigram in trigrams:
            trigrams[bigram].append(word_list[x+2])
        else:
            trigrams[bigram] = [word_list[x+2]]
    return trigrams


def read_file(file_name, front_matter, end_matter):
    '''Read an input file.
    Return a list of all words in the file.
    file_name: string of file name, including file path if not in current directory'''
    with open(file_name, "r") as input_file:
        if front_matter:
            skip_front_matter(input_file, front_matter)
        all_words = []
        for line in input_file:
            # skip end of book
            if end_matter and line.startswith(end_matter):
                break
            else:
                all_words += line.rstrip().split()
    return all_words


def skip_front_matter(f, front_matter):
    '''Skip over the front matter in the book
    f: an open file object
    front_matter: string of the front matter ending line'''
    for line in f:
        if line.startswith(front_matter):
            break


def choose_trigrams(trigram_dict, length):
    '''Return a text produced from trigrams.
    trigram_dict: a dictionary of trigrams,
                key is a bigram, value is a list of the third trigram element
    length: length of the output text'''
    output_words = []
    first_bigram = random.choice(list(trigram_dict.keys()))
    output_words += first_bigram.split()
    for n in range(2, length - 2):
        last_bigram = " ".join(output_words[n-2:n])
        if last_bigram in trigram_dict:
            next_word = random.choice(trigram_dict[last_bigram])
            output_words.append(next_word)
        else:
            choose_trigrams(trigram_dict, n)
    return " ".join(output_words)


def write_trigram_text(input_file, length, front_matter=None, end_matter=None):
    '''Print a text produced from trigrams derived from input file.
    input_file: string of file name
    front_matter: text of final line of text's front matter (title, publication info)
    end_matter: text of first line of text's end matter (acknowledgments, etc.)
    length: length, in words, of ouput text'''
    all_words = read_file(input_file, front_matter, end_matter)
    trigrams = make_trigrams(all_words)
    length = int(length)
    final_text = choose_trigrams(trigrams, length)
    print(final_text)


if __name__ == "__main__":
    args = argv[1:]
    write_trigram_text(*args)
