#this is exercize 16 on page 59 of the LPTHW pdf 
#exercise 16 - reading and writing files

# we're using arguments here, the arg is a filename var
from sys import argv
# argv standard options for filename
script, filename = argv
# print the file name we passed
# print an option to exit
# print an option to continue, ie: return for yes
print("We're going to erase %r.") % filename
print("If you don't want that, hit CTRL-C (^c).")
print("If you do want that, hit RETURN.")
# getting input with a ? prompt
raw_input("?")
# printing a status message
# setting target to file I don't understand the w here
print("Opening the file...")
target = open(filename, "w") # W IS FOR WRITE APPARENTLY!!! 

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write("line1\nline2\nline3\n")

print("And finally, we close it.")
target.close()