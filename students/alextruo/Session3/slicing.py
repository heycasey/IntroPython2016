#this is a sample list of integers
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#this is a sample sentence with a string
sentence = "Mary had a little lamb. Or something."

#this will print the first number in the list
print("\nThis will print the first number in the list and the last number in the list")
print(alist[0])
#this will print the last number
print(alist[-1])

#this prints the first four of the list
print("\nThis prints the first four in the list:")
print(alist[0:4])

#this prints the last 4 in the list
print("\nThis prints the last four in the list:")
#use -4 and then an empty range to get the last 4 from the list
print(alist[-4:])

#this  starts at the 4th one and then ends at the 4th to the last one
print("\nThis returns the middle ones:")
print(alist[4 :-4])

#return a sequence reversed (just with slicing)
print("\nThis prints the last ones in reverse")

# starts at the  end (I don't specify the beginning or end [first, end, by how much])
print(alist[: : -1])

#this prints out the length of the list
print("\nThis is the length of the list:")
x = len(alist)
print(x)

third =  round((x / 3))

print("\nThis is the last third")
print(alist[-third : ])

print("\nThis is the second third")
print(alist[ third: -third])

print("\nThis is the first third")
print(alist[0 : third])