

mydict = {name: "Chris", city: "Seattle", cake: "Chocolate"}

mydict.items()

del mydict[cake]

mydict.items()

mydict[fruit] = "Mango"

mydict.items()

if 'cake' not in mydict.keys():
    print("No cake!")

if "Mango" in mydict.values():
    print("Yeah Mango")

#need a solution for this one
tees = {k:v for k,v in mydict.items()}

s2 = set()
s3 = set()
s4 = set()

for i in range(0,21):
    if i % 2 == 0:
        s2.add(i)
    elif i % 3 == 0:
        s3.add(i)
    else i % 4 == 0:
        s4.add(i)

print(s2, s3, s4)

s3.issubset(s2)
s4.issubset(s2)

pyset = set()
for letter in "python":
    pyset.add(letter)
pyset.add("i")

for l in "marathon":
    listy = []
    listy.append(l)

myfs = frozenset(listy)
