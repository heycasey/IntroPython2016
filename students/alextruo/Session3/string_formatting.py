#take these values ( 2, 123.4567, 10000)
#:03d means give me 3 characters total (002). 05.2f means 5 characters total, and 2 decimals for float.
#:.2g means; 'file_002 :   123.46, 1.00e+04'; and .2e is 2 decimal points and e for floating point exponential
print("Make this nice and pretty: file_{:03d} : {:05.2f}, {:.2e}".format(2, 123.4567, 10000))

#rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

def formatter_example(num):
    #this prints out the string and the number of items in the tupple using the len() function
    print("This will print the number of values in the tupple:  {:d}".format(len(num)))
    #this defines the variable as a string and then multiply it times the length
    d = ('{:d}')*len(num)
    #now paste that back into the value here
    print("\tThis will print what's in the tupple:")
    #take the formatter and make it into a list here with the list() function
    print(list(d.format(*num)))

formatter_example((2,3,5))
formatter_example((2,3,5, 7, 9))
formatter_example((2,3,5, 7, 9,2,5,6))
