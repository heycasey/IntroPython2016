def print_grid_4():

#This is the first line to print. This prints the "+" and then 4 times the "-" and then again
    print("+", "-"*4,"+","-" * 4,"+")
#This prints the inside rows. This prints the | and then adds empy spaces
    for i in range(0,4):
        print("|",  " " * 4, "|", " " * 4 , "|")
#print("|",  " " * 4, "|", " " * 4 , "|")
#print("|",  " " * 4, "|", " " * 4 , "|")
#print("|",  " " * 4, "|", " " * 4 , "|")

#This repeats the middle row
    print("+", "-"*4,"+","-" * 4,"+")

#This prints the last 4 rows
    for i in range(0,4):
        print("|",  " " * 4, "|", " " * 4 , "|")

#This prints the final string
    print("+", "-"*4,"+","-" * 4,"+")

print_grid_4()

#this prints the table in a different size, depending on what the user inputs
print("Give me an integer, please.")
n = int(input())

def print_grid(n):

#This is the first line to print. This prints the "+" and then 4 times the "-" and then again
    print("+", "-"*n,"+","-" * n,"+")
#This prints the inside rows. This prints the | and then adds empy spaces
    for i in range(0,n):
        print("|",  " " * n, "|", " " * n , "|")

#This repeats the middle row
    print("+", "-"* n,"+","-" * n,"+")

#This prints the last 4 rows
    for i in range(0, n):
        print("|",  " " * n, "|", " " * n , "|")

#This prints the final string
    print("+", "-"*n,"+","-" * n,"+")

print_grid(n)

#this takes two numbers

def print_grid_final(column_rows, width):
    #this adds the "+" sign with "-", times the width, then times again for the number of cells
    #and ends with another "+" and starts a new line
    top = ("+" + "-" * width) * column_rows + "+" + "\n"
    #this prints the body
    body = ("|" + " " * width) * column_rows + "|" + "\n"

    #each row is the top, plus the body, times the width that I want
    row = top + body * width  

#the variable total is the row multiplied by the number of columns/rows that I want
# and then end the last row with "top".
    total = row * column_rows + top 
#print the entire table
    print(total)

#call the function with these two numbers
print_grid_final(5,4)