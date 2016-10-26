#!/Users/jhefner/python_dev/uw_python/bin/python




def main():
    # Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
    things = {}
    things['name'] = "Chris"
    things['city'] = "Seattle"
    things['cake'] = "Chocolate"

    # Display the dictionary.
    print(things)

    # Delete the entry for “cake”.
    print(things.pop('cake'))

    # Display the dictionary.
    print(things)

    # Add an entry for “fruit” with “Mango” and display the dictionary.
    things['fruit'] = "Mango"

    # Display the dictionary keys.
    for i in things.keys():
        print(i)

    # Display the dictionary values.
    for i in things.values():
        print(i)

    # Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    print("cake" in things.keys())

    # Display whether or not “Mango” is a value in the dictionary (i.e. True).
    print("Mango" in things.values())

    # Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
    things_copy = things.copy()
    for k, v in things_copy.items():
        number_of_ts=0
        for i in k:
            if i =='t':
                number_of_ts+=1
        # print("Key:", k,"\tValue:",v,"\t# of ts:",number_of_ts)
        things_copy[k]=number_of_ts
    print("Result of things_copy:\n",things_copy)

    # Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    s2 = set(range(0,21,2))
    s3 = set(range(0,21,3))
    s4 = set(range(0,21,4))

    # Display the sets.
    print("s2:",s2)
    print("s3:",s3)
    print("s4:",s4)

    # Display if s3 is a subset of s2 (False)
    print(s3.issubset(s2))

    # and if s4 is a subset of s2 (True).
    print(s4.issubset(s2))

    # Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    character_set = set(list("Python"))
    character_set.add("i")
    print(character_set)

    # Create a frozenset with the letters in ‘marathon’
    fs = frozenset(list("marathon"))
    print(fs)

    # display the union and intersection of the two sets.
    print("fs union character_set:",fs.union(character_set))
    print("fs intersetcion character_set:",fs.intersection(character_set))

if __name__ == '__main__':
    main()