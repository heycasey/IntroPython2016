#define the function here with n as the value
print("Give me a number:")
n = int(input())

def fibonacci(n):
    """(must be indented) this is an example doc string compute the nth Fibonacci number"""
    if n < 0:
        return None
    elif n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#this calls the function with the number that I enter.
print("This is the number:", fibonacci(n))

def lucas(n):
    """this is the lucas series, which is similar but it starts with 1 and 1 instead"""
    if n < 0:
        return None
    elif n == 2:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
#call the function and print out this number from the lucas series
print("This the lucas number: ", lucas(n))

#define the sum series with 3 parameters, required, 2 optional
def sum_series(n, param1=0, param2=1):
    """
    for param1 = 0 , return the zero position
    for param2 = 1, return the first element in the series
    if the first and second numbers are 0 and 1, it's Fibonnaci
    if the first and second numbers are 2 and 1, it's Lucas
    """
    if n < 0:
        return None
    if n == 0:
        return param1
    elif n == 1:
        return param2
    else:
        return sum_series(n - 1, param1, param2) + sum_series(n - 2, param1, param2)

print("Prints the nth number in the sequence: ", sum_series(n))

#testing with assert statements
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(5) == 5

assert lucas(-1) ==  None
assert lucas(-2) ==  None
assert lucas(5) ==  8
