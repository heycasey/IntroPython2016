#!/usr/local/bin/python3

# created: Darryl Wong
# date: 10/9/2016
# Week 2 homework

def fizzbuzz(n):
	ret = ""
	if (n % 3 == 0):
		ret = ret + "fizz"
	if (n % 5 == 0):
		ret = ret + "buzz"
	if (ret == ""):
		ret = i
	return (ret)

for i in (range (1, 101)):
	print (fizzbuzz(i))
