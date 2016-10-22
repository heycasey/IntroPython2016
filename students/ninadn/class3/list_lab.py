#!/usr/bin/env python3

fruitlist = ['Apples', 'Pears', 'Oranges', 'Peaches']
print (fruitlist)

newfruit = str(input("Enter another fruit: "))
fruitlist.append(newfruit)
print (fruitlist)

fruitnum = int(input("Enter a number between 1 and 5: "))
print (fruitlist[fruitnum-1])
print ('ok\n')

fruitlist = ['mango']+fruitlist
print (fruitlist)

fruitlist.insert(0,'Banana')
print (fruitlist)
print ('ok\n')

#For loop to print only fruits startign with P. I tried using the or in the if statement to check for case, but got an error. Need to investigate.
for fruit in fruitlist:
	#print (fruit[0])
	if fruit[0] == 'P':
		print (fruit)

print ('\n\n\n')
'''Series 2'''
#Dispaly the list
print (fruitlist)

#Remove the last fruit from the list and display list
fruitlist.pop()
print (fruitlist)

#Multiply the list times 2 and get user input for fruit to delete
fruitlist = fruitlist*2
userfruit =''
while userfruit not in fruitlist:
	userfruit = str(input('Enter a fruit to delete: '))

for fruit in fruitlist:
	if fruit == userfruit:
		fruitlist.remove(userfruit)

print ('\n')
print (fruitlist) #print fruit list post fruit deletion

print ('\n\n\n')

'''Series 3'''

#Convert to all lower case. Trying to figure out a way to do so without creating a new variable.
lowerfruits = []
for fruit in fruitlist:
	lowerfruits.append(fruit.lower())
fruitlist = lowerfruits

print(fruitlist)

for fruits in fruitlist:
	userinput = str(input('Do you like :',fruits))
	while userinput == 'yes' or 'no':
		if userinput == 'yes':
			pass
		elif userinput == 'no':
			fruitlist.revove()

print (fruitlist)
print ('\n\n\n')

'''Series 4'''












