"""
Slicing operations - Have assert statements
"""

def swapFirstLast(inputSeq):

    lastItem = inputSeq[-1]
    firstItem = inputSeq[0]
    inputSeq[0] = lastItem
    inputSeq[-1] = firstItem
    print(inputSeq)

def reverseSeq(inputSeq):

    result = inputSeq[::-1]
    print(result)

def firstLastFourItems(inputSeq):

    result =  inputSeq[:4]  + inputSeq[-4:]
    lastFourItems = result[::2]
    print(lastFourItems)
    # print("First four items" ,  firstFourItems)
    # print("Last four items" ,  lastFourItems)

def newOrder(inputSeq):

    lengthOfList = len(inputSeq)
    parts = lengthOfList//3
    firstThird = inputSeq[1:parts]

    # firstFourItems = inputSeq[:4]
    # lastFourItems = inputSeq[4:]
    # print("First four items" ,  firstFourItems)
    # print("Last four items" ,  lastFourItems)

if __name__ == "__main__":
    # response = input("a prompt for the user > ")
    # print(response)
    print("Run some slicing operations")
    inputList = [34, 56, 19, 23, 55,66,77,88]
    print(inputList)
    # swapFirstLast(inputList)
    # reverseSeq(inputList)
    firstLastFourItems(inputList)


