# !/usr/bin/env python3

"""
Name: Paul Briant
Date: 10/18/16
Class: Introduction to Python
Session: 03
Assignment: Mailroom

Description:
This program creates donor statistics reports or sends thank you letters based
on user specification.
"""
# -------------------------------Functions--------------------------------------


def print_report(donors):
    """
    Takes in the donors list and prints a report of donors ordered least to
    greatest in terms of historic contributions.
    """
    # list of the sum of total contributions by each donor
    total_list = sorted(sum_d(donors))
    # iterate through donors
    for i in range(len(total_list)):
        # Name, total donated, number of donations and average donation amount.
        print(total_list[i][1], total_list[i][0], total_list[i][2],
              total_list[i][0] / total_list[i][2])


def sum_d(donors):
    """
    Takes in a multi dimensional list of donors and contributions and returns
    a list containing total amount donated, donor name and number of donations.
    """
    total_list = []

    for item in donors:
        d_total = 0
        for d in item[1]:
            d_total += d
        total_list.append([d_total, item[0], len(item[1])])
    return total_list


def print_donor(donor_dict):
    """
    Take in the dictionary of donors and displays each donor name.
    """
    for key in donor_dict:
        print(donor_dict[key])


def find_donor(full_name, donor_dict):
    """
    Take in the name of the donor and the donor dictionary. Iterate through the
    compliation of donors and return donor information.

    To Do:
    Ensure 'donor' returns all donor related information.
    """
    for donor in donor_dict:
        if full_name.strip().lower() == donor.lower():
            return donor


def main_menu_selection(message):
    """
    Take in donor option message, prompts user for a response and return
    their response.
    """
    # Provide options and prompt the user for a response.
    print(message)
    # Remove any additional white space.
    action = input('==> ').strip()
    return action


def create_letter(donor):
    """
    Take in donor information and return a thank you letter to specific donor.
    To Do:
    Ensure donor key value pair works as intended.
    """
    # Display thank you
    return '''
          Dear {},
          Thank you for your generous donation of ${}!
          Your contribution to this organization will greatly
          impact our efforts to complete our mission.

          Sincerely,
          -The Team
          '''.format(donors[d_index][0], donors[d_index][1][-1]))


def send_ty(donor_dict):
    """
    This function takes in a multi dimensional list of donors and
    contributions, prompts for specific donor information and composes a thank
    you letter for the specified donor.
    """
    full_name = input("Please enter your full name: ")
    if full_name == 'list':
        print_donor(donor_dict)
        full_name = input("Please enter your full name: ")
    if full_name not in donors:
        # Add new donor name to donors
        donors.append([full_name, []])
    # Prompt for a donation amount
    amount = input("How much would you like to donate? ")
    # Verify amount is a number
    if not amount.isnumeric():
        amount = input("How much would you like to donate? ")
    d_index = add_donor(full_name, donors)
    # Append to donor in donors
    donors[d_index][1].append(amount)
    print(create_letter(donor))


def add_donor(name, donors):
    """
    This function takes in the full name of each donor and a multi dimensional
    list of donors and contributions and returns the index of the name in the
    donors list.
    """
    for item in donors:
        if name in item:
            d_index = item.index(name)
    return d_index

# ==============================================================================


def main():
    """
    Displays the main interactive interface of this program. The interface
    provides the user with options to send a thank you letter, print a report
    and exit the interface.
    """
    donors = [['Bill Gates', [1000000, 2500000, 1800000]],
              ['Sheryl Sandberg', [200000, 100000, 130000]],
              ['Larry Page', [150000, 110000, 170000]],
              ['Satya Nadella', [140000, 111000]],
              ['Susan Wojcicki', [100000, 109000]]]

    donor_dict = {'Bill Gates': [1000000, 2500000, 1800000], 'Sheryl Sandberg':
                  [200000, 100000, 130000], 'Larry Page': [150000, 110000,
                  170000], 'Satya Nadella': [140000, 111000], 'Susan Wojcicki':
                  [100000, 109000]
                  }

    message = """
    Please select from the following options:

    To send a thank you: type "s"
    To print a report: type "p"
    To exit: type "x"
    """

    action = ''
    # Continue to prompt user until user enters 'x'
    while True:
        action = main_menu_selection(message)
        # Determine action to take.
        if action == 's':
            send_ty(donors)
        elif action == 'p':
            print_report(donors)
        elif action == 'x':
            break
        else:
            print('please type "s", "p", or "x"')


if __name__ == '__main__':
    main()
