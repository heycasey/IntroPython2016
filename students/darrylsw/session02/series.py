#!/usr/local/bin/python3

# created: Darryl Wong
# date: 10/9/2016
# Week 2 homework
#  - fibonacci series
#  - lucas series
#  - generic series passing 0 and 1st values as arguments

def fibonacci(n):
	"""returns the nth value in the fibonacci series"""
	if (n==0):
		return 0
	elif (n==1):
		return 1
	else:
		return (fibonacci (n-1) + fibonacci (n-2))

def lucas(n):
	"""returns the nth value in the lucas series"""
	if (n==0):
		return 2
	elif (n==1):
		return 1
	else:
		return (lucas (n-1) + lucas (n-2))

def sum_series(n, a=0, b=1):
	"""returns the nth value of a summation series where the 0th value is "a" and the 1st value is "b" """
	"""if a and/or b are not defined, defaults to 0 and 1 for the fibonacci series """
	if (n==0):
		return a
	elif (n==1):
		return b
	else:
		return (sum_series (n-2, a, b) + sum_series (n-1, a, b))


# test the first 9 values of the fibonacci series using assert

assert (fibonacci(0) == 0)
assert (fibonacci(1) == 1)
assert (fibonacci(2) == 1)
assert (fibonacci(3) == 2)
assert (fibonacci(4) == 3)
assert (fibonacci(5) == 5)
assert (fibonacci(6) == 8)
assert (fibonacci(7) == 13)
assert (fibonacci(8) == 21)


# test the first 9 values of the lucas series using assert
assert (lucas(0) == 2)
assert (lucas(1) == 1)
assert (lucas(2) == 3)
assert (lucas(3) == 4)
assert (lucas(4) == 7)
assert (lucas(5) == 11)
assert (lucas(6) == 18)
assert (lucas(7) == 29)
assert (lucas(8) == 47)

# test the first 9 values of the sum series function using assert - fibonacci version (default values)
assert (sum_series(0) == 0)
assert (sum_series(1) == 1)
assert (sum_series(2) == 1)
assert (sum_series(3) == 2)
assert (sum_series(4) == 3)
assert (sum_series(5) == 5)
assert (sum_series(6) == 8)
assert (sum_series(7) == 13)
assert (sum_series(8) == 21)


# test the first 9 values of the sum series funcation using assert - fibonacci version
assert (sum_series(0, 0, 1) == 0)
assert (sum_series(1, 0, 1) == 1)
assert (sum_series(2, 0, 1) == 1)
assert (sum_series(3, 0, 1) == 2)
assert (sum_series(4, 0, 1) == 3)
assert (sum_series(5, 0, 1) == 5)
assert (sum_series(6, 0, 1) == 8)
assert (sum_series(7, 0, 1) == 13)
assert (sum_series(8, 0, 1) == 21)

# test the first 9 values of the sum series using assert - lucas series version
assert (sum_series(0, 2, 1) == 2)
assert (sum_series(1, 2, 1) == 1)
assert (sum_series(2, 2, 1) == 3)
assert (sum_series(3, 2, 1) == 4)
assert (sum_series(4, 2, 1) == 7)
assert (sum_series(5, 2, 1) == 11)
assert (sum_series(6, 2, 1) == 18)
assert (sum_series(7, 2, 1) == 29)
assert (sum_series(8, 2, 1) == 47)

