#!/usr/local/bin/python3

#### grid printer ####

def print_grid(x, y):
	print_horiz (x)
	print_rows (x, y)
	print_horiz (x)
	print_rows (x,y)
	print_horiz(x)

def print_horiz (x):
	# print top row, size x
	print ("+", end="")
	for i in range (0, x):
	    print ("-", end="")
	print ("+", end="")
	for i in range (0,x):
		print ("-", end="")
	print ("+")

def print_rows (x, y):
	# print y rows
	for i in range (0, y):
		print ("|", end="")
		for j in range (0, x):
			print (" ", end="")
		print ("|", end="")
		for j in range (0,x):
			print (" ", end="")
		print ("|")

print ("4 x 4 grid")
print
print_grid(4, 4)

print
print
print ("10 x 10 grid")
print
print_grid (10, 10)

print
print
print ("5 x 10 grid")
print
print_grid (5, 10)
