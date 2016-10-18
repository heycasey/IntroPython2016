#!/usr/local/bin/python3

# Owner: Darryl Wong
# Date: 10/11/2016

def swap_first_last (list):
	temp = list[0]
	list[0] = list[-1]
	list[-1] = temp
	return list

def alternate (list):
	return (list[::2])

def first4last4alt (list):
	return list[4:-4:2]

def reverse (list):
	return list[::-1]

def reorder_third (list):
	size = len(list) // 3
	return list[size:size*2] + list[size*2:] + list[:size]

orig_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 99]

print("original list")
print (orig_list)

list = orig_list[:]
print ("list with first and last elements exchanged")
print (swap_first_last(list))

list = orig_list[:]	
print ("list with every other item removed")
print (alternate(list))

print ("list with first and last four removed and alternate")
list = orig_list[:]
print (first4last4alt(list))

print ("list reversed")
list = orig_list[:]
print (reverse(list))

print ("reorder third")
list = orig_list[:]
print (reorder_third(list))

