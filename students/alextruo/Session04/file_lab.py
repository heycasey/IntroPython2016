#Paths and File Processing
import os, pathlib
#write a program which prints the full path to all files in the current directory, one per line
def full_path():    
    for root, directory, files in os.walk('.'):
        for p in files:
            p = os.path.join(root,p)
            print("This is the path:", p)
            print(os.path.abspath(p))

full_path()


#write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)

#advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.

#You need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing.)