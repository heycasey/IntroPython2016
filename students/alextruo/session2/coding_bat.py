def parrot_trouble(talking, hour):
    '''define the variable with two parameters, talking and hour'''
    return (talking and (hour < 7 or hour > 20))

#this will print that we are in trouble 
print("The parrot is talking and it's 6am.", parrot_trouble(True, 6))
#this will print if we that we are not in trouble, false
print("The parrot is not talking and it's 5am.", parrot_trouble(False,5))
#this will print if we that we are not in trouble.
print("The parrot is  talking and it's noon.", parrot_trouble(True,12))

def talking_parrot2(x):
    talking = True
    isTalking = "Danger!" if talking and x  < 7 or x > 20 else "Not danger!"
    return isTalking
print(talking_parrot2(12))

is_hungry = True
state = "hungry" if is_hungry else "not hungry"
#This prints the statement if is_hungry is True
print(state)
