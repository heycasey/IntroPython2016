#for loop - (From 0 to 100 inclusive, do each step)
for i in range(0,101):
        #for each variable i, print Fizz if can be divided by 3 and  it is not divisible by 5
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz. This %d is a multiple of 3"% i)
        #for each variable i, print Buzz if it can be divided by 5 but not divisible by 3
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz. This %d is a multiple of 5" % i)
        #for each varaible i, print FizzBuzz if it is divisible by 3 and 5
    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz. This %d  is divisible by 3 and 5." % i)
        #If it's not  print divisible by either, print the number as is
    #elif i % 3 != 0 and i % 5 != 0:
    else:    
        print(i)
