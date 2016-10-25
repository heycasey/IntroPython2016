#!/Users/sheree/miniconda3/bin/python
"""

    mailroom.py

    http://uwpce-pythoncert.github.io/IntroToPython/exercises/mailroom.html#exercise-mailroom

    @author: sheree@pennah.com don't email me

"""

#simplified the data structure for expediency

DONATION_ARCHIVE = [
["Alice", [111, 11111, 1111111]],
["Bob", [222, 22222, 2222222]],
["Carol", [333, 33333, 3333333]],
["David", [444, 44444, 4444444]],
["Edward", [555, 55555, 5555555]],
["Frankie", [6, 6]]
]

#making a working copy so I don't get confused by the original data set
DONATION_LIST = DONATION_ARCHIVE[:]


def show_list_of_donors():
    """shows a simple list of donors and count of donations"""
    print("\t*** Donors List ***\n")
    for i in DONATION_LIST:
        print("\t{0} has made {1} donations totalling ${2}.00.".format(i[0], len(i[1]), sum(i[1])))
    pass


def send_thanks_letter():
    """main thanks path, will call thanks printer"""
    print("\nHere are the donors we found:\n")
    print(show_list_of_donors())
    list_of_donor_names = [name[0] for name in DONATION_LIST]
    print("Which donor would you like to send a letter to?\n")
    prompt = ">>> "
    donor_name = input(prompt)
    if donor_name in list_of_donor_names:
        donator_index = list_of_donor_names.index(donor_name)
        print_thanks_letter(donator_index)
        print("Please copy & paste it into your email program.\n")
    else:
        print("Could not find {0}. Would you like to add a new donation?".format(donor_name))
        yes_or_no_prompt = "Y/N? "
        answer = input(yes_or_no_prompt)
        if answer == "Y":
            add_a_new_donation(donor_name)
            list_of_donor_names = [name[0] for name in DONATION_LIST]
            donator_index = list_of_donor_names.index(donor_name)
            print_thanks_letter(donator_index)
        else:
            print("OK.")
    pass


def print_thanks_letter(donor_index):
    """prints a thank you email for a particular donation """
    letter = '''

    Dear {0},

    We are so delighted to have your continued support.

    This letter serves as not only a note of our gratitude,
    but a tax receipt for your donation of ${1}.00.

    Our Deepest Thanks,

         -The Foundation

    '''
    print(letter.format(
                        DONATION_LIST[donor_index][0],
                        DONATION_LIST[donor_index][1][0]
                        ))
    return donor_index


def add_a_new_donation(donor):
    """adds a single donation to our donations"""
    print("How much did {0} donate?\n".format(donor))
    prompt = ">>> "
    amount = int(input(prompt))
    new_donor_to_add_to_main_donors = []
    new_donor_to_add_to_main_donors.append(donor)
    new_donor_to_add_to_main_donors.append([amount])
    DONATION_LIST.append(new_donor_to_add_to_main_donors)
    donor_index = DONATION_LIST.index(new_donor_to_add_to_main_donors)
    return donor_index


def report_creator():
    """ print report of donations, including any new additions, in a fancy way"""
    print("Donations Report".center(80, "-"))
    print("{:^18} {:^18} {:^18} {:^18}".format("DONOR", "COUNT", "TOTAL", "AVERAGE"))
    for i in DONATION_LIST:
        print("{:^18} {:^18} {:^18} {:^18}".format(i[0], len(i[1]), sum(i[1]), (sum(i[1])) // len(i[1])))
    print()
    print("end".center(80, "-"))
    print()
    pass


def main():
    print("\n**** Welcome To The Mailroom ****")
    print()
    print("Command `ty` will Send a Thank You Letter")
    print("Command `cr` will Create a Report")
    print("Command `xx` will Exit")
    print()

    while True:

        entry_prompt = "Please enter `ty`, `cr`, or `xx` below.\n>>> "
        command = input(entry_prompt)
        if command == "cr":
            report_creator()
        elif command == "ty":
            send_thanks_letter()
        elif command == "xx":
            print("Exiting the mailroom. Goodbye.")
            break
        else:
            print("I'm sorry, I don't understand.\n")


if __name__ == '__main__':
    main()
