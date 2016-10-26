#!/Users/jhefner/python_dev/uw_python/bin/python

import os



def main():
    # Paths and File Processing:
    # write a program which prints the full path to all files in the current directory, one per line
    for root_dir, dirs, files in os.walk("./"):
        for name in files:
            print(os.path.join(os.getcwd(),name))

    # write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
        # advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
        # Note that if you want it to do any kind of file, you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing.)
    file_data = ''
    with open('file_to_be_copied') as f:
        file_data = f.read()
        copy_data = open('copied_file','w')
        copy_data.write(file_data)


    # File reading and parsing:
    # In the class repo, in:
        # Examples/Session01/students.txt
    # You will find the list I generated in the first class of all the students in the class, and what programming languages they have used in the past.
    # Write a little script that reads that file, and generates a list of all the languages that have been used.
    # Extra credit: keep track of how many students specified each language.
    listoflanguages = set()
    for line in open('../../../Examples/Session01/students.txt'):
        languages_list = line.split(':')
        if len(languages_list) >1:
            for i in languages_list[1].split(','):
                listoflanguages.add(i.strip())
    print(listoflanguages)

if __name__ == '__main__':
    main()