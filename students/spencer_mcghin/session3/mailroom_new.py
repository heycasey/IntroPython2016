#!/usr/bin/env python3

import numpy


"""Dictionary of Donors and Amounts Donated"""

donors = {"Nick Padgett": [12312, 34230, 38593],
          "Julia Allen": [49203, 5023, 9052],
          "Pete Tamisin": [9503, 2093, 10932, 40923],
          "Charles Elliott": [209, 50912, 9026],
          "Andy Rocha": [20968, 2091, 8934],
          "Beth DeSousa": [29092, 5906, 8734]}


""" Input variables """

# Input for donation amount #

donation_amount = input("Please enter a donation amount '\n'"
                        "> ")
donor_name = input()

"""

Functions for program

"""

"""Main menu prompt"""

def main():
    menu = {}
    menu['1.)']="Generate a Thank You Letter"
    menu['2.)']="Generate a Donor Report"
    menu['3.)']="List Current Donors"
    print("At any time, type 'Exit' in order to exit the program, or 'Menu' to go back to the main menu.")
    while True:
        options=sorted(menu.keys())
        for entry in options:
            print(entry, menu[entry])




"""Send a thank you functions"""

# Print donor list #

def print_donor_list():
    for donor, donation in sorted(donors.items()):
        print(donor)

# Add donor name to list #

def add_donor():
    donors.update()

# Add donation amount to new donor #

def add_amount():
    donors.update({# Variable : donation_amount})

# Verify donation amount is an integer #

def check_donation():
    while isinstance(donation_amount, int):
        add_amount()
    else:
        main()

# Print email to terminal #


def print_email():
        print("Hello %r, Thank you so much for your generous donation to our very charitable organization." '\n'
              "Your contribution will help us to further our reach in providing charitable services to those in need." '\n'
              "We hope that you will continue to support our organization in the future." '\n'
              "Sincerely," '\n'
              '\n'
              "Spencer McGhin")


"""

Print donor donation report functions

"""

# Print lists containing output of functions below #

def print_report():
# todo - print output of functions below as list for each donor using tabulate

# Print total donor donations #

def print_donation_total():
    totals_results = []
    for donor, donations in sorted(donors.items()):
        totals_results.append((sum(donations)))

# Print total number of donations #

def print_num_donations():
    num_results = []
    for donor, donations in sorted(donors.items()):
        num_results.append(len(donations))

# Print average donation #

def print_avg_donation():
    avg_results = []
    for donor, donations in sorted(donors.items()):
        avg_results.append(int(numpy.mean(donations)))


# Output info for tabulate format #
# todo - generate list of lists containing output from each function for each donor

if __name__ == '__main__':
# todo - write program!