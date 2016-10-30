def slicing1(n):
    """return a sequence with the first and last items exchanged"""
    print (n[-1:]+n[1:-1]+n[:1])
    

def slicing2(n):
    """return a sequence with every other item removed"""
    print( n[0::2])


def slicing3(n):
    """return a sequence with the first and last 4 items removed, 
    and every other item in between"""
    newword = n[4:-4:2]
    print (newword)

def slicing4(n):
    """return a sequence reversed (just with slicing)"""
    word = n[::-1]
    print (word)
    

def slicing5(x):
    """return a sequence with the middle third, then last third, 
    then the first third in the new order"""
    third = len(x)//3

    start = x[:third]
    middle = x[third:-third]
    end = x[-third:]
    print (middle+end+start)

n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print("original = ",n)
slicing1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
slicing2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
slicing3([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
slicing4([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
slicing5([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
slicing1('cheeseburgeryummy')
slicing2('cheeseburgeryummy')
slicing3('cheeseburgeryummy')
slicing4('cheeseburgeryummy')
slicing5('cheeseburgeryummy')
