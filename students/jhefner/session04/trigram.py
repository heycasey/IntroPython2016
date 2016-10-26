#!/Users/jhefner/python_dev/uw_python/bin/python

import os

"""
Thoughts on how im going to do this:
How to store the data: a dictionary.
Key = First two words (starting at position 0,1 in line of document and incrementing to end of line
Value = set. set is populated with each the 2 words that come after the key. This will retain only unique matches without incurring overhead of duplicate checking.

The method for creating the dictionary:
Bring entire file into memory if possible. If it looks like the file is too big I'll have to evaluate it line by line.
Split entire file or each line as mentioned above ^ so it is now a long list.
Start at (0,1) of list and define it as the key, add (2) of list to set.
Increment list position to key(1,2) and set(3) and so on.

That will generate my dictionary to make up a new novel with.

Generating the text file:
1. To choose an arbitrary starting point use rand to choose a random dictionary key that has that as the first word in the key.
2. Take Key and append to output.
3. Use rand to choose a random value from keys set and append to output.
4. Evaluate last word in output, find rand dictionary key sthat starts with the word.
5. Step 2-4 until done.


"""

def read_file_to_memory(filename):
    with open(filename) as f:
        file_data = f.read()
        return file_data

def file_massager(data):
    listerizer = data.split()
    # TODO: LEFT OFF HERE
    super_sweet_dictionary = {}
    return super_sweet_dictionary

def main():
    file_data = read_file_to_memory('sherlock_small.txt')
    dict_of_words = file_massager(file_data)
    print(dict_of_words)








if __name__ == '__main__':
    main()