"""Simple program to take a string and swithc the first and last characters

def switch(word):
	word2=word[0:len(word):2]
	for i in range (0, len(word)):
		if i%2 == 0:
			word2=word2+word[i]
		else:
			word2=word2
	return word2

def main():
	word = str(input('Enter a phrase or string: '))
	word2 = switch(word)
	print(word2)

main()
"""

'''Simple program to return a sequence reversed with slicing only

initstr = str(input("Enter a string :"))
newstr = initstr[len(initstr):0:-1]+initstr[0]
print (len(initstr))
print (newstr)
'''

'''Simple program to return a sequence with the middle third, then last third, then the first third in a new order'''

fullstring = str(input("Enter a word or phrase :"))
newstring = fullstring[int(len(fullstring)/3):int(len(fullstring)*2/3)]+fullstring[int(len(fullstring)*2/3):len(fullstring)]+fullstring[:int(len(fullstring)*1/3)]
print(newstring)
print (len(fullstring))
print (len(newstring))
