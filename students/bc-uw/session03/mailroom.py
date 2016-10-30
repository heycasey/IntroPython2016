#!/usr/bin/python3

'''
This script should be executable. The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each
The script should prompt the user (you) to choose from a menu of 2 actions: 'Send a Thank You' or 'Create a Report'.
'''

#donors and their donation amounts
donors = {
"reginald": [500, 350, 666],
"sassafrass": [99],
"diggles": [444, 555]
}

prompt = """
To send a thank you note: enter "s"\n
To print a report: enter "r"\n
To quit: "q"\n
Choose an option:==>"""

def sendThankyou():
    nameprompt = "Please Enter a Donor Name (Enter 'list' for donors): "
    response = input(nameprompt)
    if response == 'list':
        listDonors()
    else:
        if response not in donors.keys():
            donors[response] = []
        else:
            try:
                newdonation = int(input("Enter Donation Amount: "))
            except ValueError:
                print("Please enter an integer")
                pass
            donors[response].append(newdonation)

    print("Dear {}: Thanks for the money bro").format(response)


def createReport():

    #make a list from my dictionary
    mylist = []

    #get values of list items in dict, add to list
    for k in donors.keys():
        for v in donors[k]:
            mylist.append(v)

    total_donations = sum()
    number_donations = len()
    average = total_donations / number_donations
    report.append(donor, total_donations, number_donations, average)


def listDonors():
    for i in donors.keys():
        print(i)

if __name__ == "__main__":
    while True:
        response = input(prompt)
        if response not in ['r', 'x', 's']:
            print("Please enter a valid selection")
            continue
        elif response == 'r':
            createReport()
        elif response == 's':
            sendThankyou()
        elif response == 'q':
            break
        else: print("Please enter your selection")
