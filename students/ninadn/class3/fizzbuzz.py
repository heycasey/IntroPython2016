'''Code to print numbers until n. If a number if a multiple of 3, print Fizz instead of the number. If it is a
multiple of 5, print Buzz instead. If it is a multiple of 15, print FizzBuzz.'''

def fizzbuzz(n):
	if n%15 == 0:
		return 'FizzBuzz'
	elif n%5 ==0:
		return 'Buzz'
	elif n%3 ==0:
		return 'Fizz'
	else: return n

def main():
	m = int(input('Enter a number :')) +1
	for i in range (1,m):
		print (fizzbuzz(i))

main()