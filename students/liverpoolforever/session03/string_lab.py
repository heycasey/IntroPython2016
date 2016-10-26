"""
String lab
"""

def main():
    print("============= String lab begins ===========================")
    inputList = [2,123.4567,10000]
    # print(inputList)
    formatStr = "file_{:03d} :{:12.4f},{:0.2e}"
    result = formatStr.format(inputList[0],inputList[1],inputList[2])
    print(result)
    # for the dynamic print
    inputTuple = (1,2,4,5,7,8)
    formatter(inputTuple)

def formatter(inputStr):
    # get the length
    multiplier = len(inputStr)
    # multiply the formatter
    fString = "{:d}"*multiplier
    fResult = fString.format(*inputStr)
    print(fResult)


if __name__ == "__main__":
    main()