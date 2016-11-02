#!/usr/bin/env python3

import numpy, collections

from tabulate import tabulate

"""Dictionary of Donors and Amounts Donated"""

donors = {"Nick Padgett": [12312, 34230, 38593],
          "Julia Allen": [49203, 5023, 9052],
          "Pete Tamisin": [9503, 2093, 10932, 40923],
          "Charles Elliott": [209, 50912, 9026],
          "Andy Rocha": [20968, 2091, 8934],
          "Beth DeSousa": [29092, 5906, 8734]}


""" Input args """

# Input for donation amount #

donation_amount = input("Please enter a donation amount '\n'"
                        "> ")
donor_name = input()

"""

Functions for program

"""

"""Main menu prompt"""

def user_input():
    print("From the menu, please select from the following options: '\n'"
          "1.) Generate a Thank You Letter '\n'"
          "2.) Generate a Donor Report '\n'"
          "3.) Exit '\n'"
          "You may exit the program at any time by typing 'Exit' or return to the main menu by typing 'Menu'")
    selection = input("> ")




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
    donors.update({# Variable) : int(donation_amount)})

# Verify donation amount is an integer #

def check_donation():
    while isinstance(donation_amount, int):
        add_amount()
    else:
        return

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

# Generate combined dictionary objects for tabulate data input format #

def report_data():
    # establish separate dictionary objects #
    results = collections.OrderedDict()
    donor_dict = {"Donors": []}
    totals_dict = {"Total $": []}
    num_results = {"Number of Donations": []}
    avg_results = {"Average Donation": []}
    # loop through donors data set and perform aggregate functions #
    for donor, donations in sorted(donors.items()):
        donor_dict["Donors"].append(donor)
        totals_dict["Total $"].append((sum(donations)))
        num_results["Number of Donations"].append(len(donations))
        avg_results["Average Donation"].append(int(numpy.mean(donations)))
    # combine dictionary objects into one for tabulate data input format #
    results.update(donor_dict)
    results.update(totals_dict)
    results.update(num_results)
    results.update(avg_results)
    return results

print(tabulate(report_data(), headers="keys", tablefmt="fancy_grid", numalign="center"))

if __name__ == '__main__':
# todo - write program!