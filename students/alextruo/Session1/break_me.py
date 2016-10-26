#These will break if I try to run them

#notdefined is not a string or a number or a variable
def name_error():
    a = notdefined

#name_error();

#I can't concatenate a string and a number
def type_error():
    x = "string here"
    y = 80
    z = x + y
    print("> ", z)

#type_error()

#a is an integer and I can't append something to it (I can append a list though)
def attribute_error():
    a = 12
    b = a.append()

#attribute_error()

#This string is bad because it's not in double quotes
def syntax_error():
        print(""This is not a string that is formatted" correctly)

syntax_error()
