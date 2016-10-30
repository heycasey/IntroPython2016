#create a variable to open the file
f = open('students.txt', 'r')

#this reads the first line
print(f.readline())

#for each line in the file, f
def whole_class():
    for line in f:
        line=line.lower()
        #print each line out please:
        print(line)

languages = []
#keeps track of all the languages that people know
for line in f:
    if "python" in line.lower():
        print("Yes, someone knows Python.")
        one = 'python'
    if 'html' in line:
        print("Yes, someone knows HTML")
        two = 'html'
    if 'java' in line:
        three = 'java'
        print("Yes, someone knows Java.")
    if 'sql' in line:
        four = 'sql'
        print("Yes, someone knows SQL.")

#append each language to the list if someone knows it
languages.append(one)
languages.append(two)
languages.append(three)
languages.append(four)

#print the new list of languages
print(languages)
        