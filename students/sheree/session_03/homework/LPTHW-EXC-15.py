#this is exercize 15 on page 54 of the LPTHW
#exercise 15 - reading files

# this is using argument variable which will be a file to process
from sys import argv
# this is the script and the argument of filename
script, filename = argv
# setting var to selected filename
txt = open(filename)
# printing out the the filename
#printing out the file contents?
print("Here's your file %r:") % filename
print txt.read()
# promppting the file
print("Type the filename again:")
file_again = raw_input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
