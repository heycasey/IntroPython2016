donors = [
    ('Hilary Clinton', [100, 30, 10]),
    ('Bernie Sanders', [20,40]),
    ('Shu Latif', [10]),
    ('God', [100]),
    ('Steve Jobs', [90, 80, 12])
    ]


def printdonors():
    """
    This will just print out the donors and the total amount they have donated. The space variable is just taking the
    total length of donor and donation amount and adding the right amount of spaces to add a '#' evenly for a box.
    :return: Boxed list of donors and total donor amounts.
    """
    print('#==========================#')
    for donor in donors:
        donation = sum(donor[1])
        space = " " * (20 - (len(donor[0]) + len(str(donation))))
        print('# {0} - ${1} {2}#'.format(donor[0], donation, space))
    print('#==========================#')


def thankyou():
    """
    :param donor: Donor Name
    :param donation: Donation Total
    :return: Prints out a thank you email to each donor.
    """
    for donor in donors:
        donation = sum(donor[1])
        print('''
        Dear {0},
        Thank you for your donation of ${1} to the Coalition of Never Selecting Evil Neanderthal Trump! Together we can make sure our
        country does not succumb to hate and fear. Your money will go towards helping to educate the masses and expose
        Donald Trump for the fraud and opportunist that he is.
        '''.format(donor[0], donation))


def finddonor(donor_name):
    """
    To match donor name.
    :param donor_name:
    :return:
    """
    for donor in donors:
        if donor_name.lower() == donor[0].lower():
            return donor
    return None


def creatreport():
    """
    This will print the donor, total amount donated, number of donations, and average amount of donations.
    :return: donor, total, number of donations, average donations in a nice table.
    """
    print('{:25s}  |  {:11s} | {:9s} | {:12s}'.format('Donor Name', 'Total Donated', 'Number of Donations', 'Average Donations\n'))
    for donor in donors:
        avg = round(sum(donor[1])/ len(donor[1]))
        total = sum(donor[1])
        don_amt = len(donor[1])
        print('{:25s} {:16.2f} {:15d} {:25.2f}'.format(donor[0], total, don_amt, avg))


def start():
    """
    This is the main menu where they can list the donors and total donated, add new donors, print thank you notes
    or create a report. We do not allow floating numbers for donation because people who donate fractional dollars
    are stupid and we don't have stupid donating to this foundation.
    :return:
    """
    ty_input = ''
    while ty_input != 'q':
        ty_input = input('''
#======================================================#
# Please make a selection from the following choices:  #
# list - List donors and totals                        #
# add - Add a new donor or donation                    #
# 1 - Send a Thank You Note                            #
# 2 - Create Report                                    #
# q : To Quit                                          #
#======================================================#
        ''')
        if ty_input.lower() == 'q':
            print('Goodbye!')
            break
        elif ty_input.lower() == 'list':
            printdonors()
            print('\n')
        elif ty_input.lower() == 'add':
            donor_name = input('Donor Name: ')
            donor = finddonor(donor_name)
            if donor is None:
                amount = int(input('Enter donation amount $ '))
                donor = (donor_name,[amount])
                donors.append(donor)
            else:
                amount = int(input('Enter donation amount $ '))
                donor[1].append(amount)
        elif ty_input == '1':
            thankyou()
        elif ty_input == '2':
            creatreport()
        else:
            print('I did not understand. Please try again.')

if __name__ == '__main__':
    start()
