#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
bio = {"Name" : "Chris", "City": "Seattle", "Cake": "Chocolate"}

#define the function with  a name, () and end with :
def main():
    #print the dictionary out
    print(bio)
    #pop out or remove this key and value
    bio.pop("Cake")
    #print the list again
    print(bio)
    #add the key Fruit: Mango to the dictionary
    bio["Fruit"] = "Mango"
    #print bio again; mango is now added
    print(bio) 
    #print the keys for all items in the dictionary
    for things in bio.keys():
        print("These are all the keys.", things)
    #print(bio.keys())
    #print(bio.values())
    #print the values for all items in the dictionary
    for stuff in bio.values():
        print("These are all the values.", stuff)
    #Check if cake is a key
    while "Cake" not in bio: 
        print("Sorry, 'Cake' is not a key in the dictionary.")
        #break to end
        break
    #check if the string mango is a value in the bio dictionary.
    while "Mango" in bio.values():
        print("True. Mango is a value in the dictionary.")
        break
    #for each variable (a for the key, b is for the value)
    for a, b in bio.items():
    #if the letter 't' appears in the variables for the values
        while 't' in b.lower():
          # print the letter and this statement
            print(b, "There are %s instances of the letter 't' here." % b.count('t'))
            #assign a variable to the number of 't' in the string
            new_values = b.count('t')
            #make a copy of the new dictionary to enter the new values
            bio_copy = bio.copy()
            #for each instance of "a" which is the key, change the value.
            bio_copy[a] = new_values
            #print the new dictionary
            print("This is the new dictionary:", bio_copy)
            break

main()

def sets_example():
    #Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    s2 = set([2, 3, 4, 6, 8, 12, 16, 18, 20])
    s3 = set([3, 6, 15, 18])
    s4 = set([4,8, 16, 20])

    #Display the sets.
    print("This is: %s" % s2)
    print("This is: %s" % s3)
    print("This is: %s" % s4)

    #Display if s3 is a subset of s2 (False)
    print("s3 is not a subset of s2", s3.issubset(s2))

    #and if s4 is a subset of s2 (True).
    print("s4 is a subset of s2", s3.issubset(s2))

    #Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    set5 = set(['P', 'y', 't', 'h', 'o', 'n'])
    print(set5)
    set5.add('i')
    print(set5)

    #Create a frozenset with the letters in ‘marathon’
    frozen = frozenset(('m','a', 'r', 'a', 't', 'h', 'o', 'n'))

    #display the union and intersection of the two sets.
    print("Displays the union of set5 and frozen:", set5.union(frozen))
    print("Displays the intersection of the two sets:", set5.intersection(frozen))

sets_example()

#for key, value in bio.items():
  #  for value2 in value:
       # if 't' in value2:
         #   print(value, "there's %s %s in here." % (value2.count('t'), 't'))

#assign a variable to each value in the dictionary
"""
for letter in bio.values():
    #if the letter 't' appears in the variables
    while 't' in letter:
      # print the letter and this statement
        print(letter, "There's a letter 't' here.")
        #print the number of "t" in the word
        print(letter.count('t'))
        new_values = letter.count('t')
        bio_copy = bio.copy()
        bio_copy[letter] = new_values
        print(bio_copy)
        break
"""
