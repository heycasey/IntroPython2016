#!/usr/bin/env python3

"""Dictionary of Donors and Amounts Donated"""

donors = {"Nick Padgett": [12312, 34230, 38593],
          "Julia Allen": [49203, 5023, 9052],
          "Pete Tamisin": [9503, 2093, 10932, 40923],
          "Charles Elliott": [209, 50912, 9026],
          "Andy Rocha": [20968, 2091, 8934],
          "Beth DeSousa": [29092, 5906, 8734]}

"""Function to generate thank you letter to a selected donor"""

def thank_you():
prompt = input("Please enter the name of a donor, or type 'list' in order to display a list of donors." '\n'
"> ")
# Check if name entered is in list. If not prompt to see if they would to add it #
while prompt not in donors:
    new_donor_add = input("That name is not in the donors list. Would you like to add it? Yes (Y) or No (N)?" '\n'
                          "> ")
if new_donor_add == 'Y': # Input name of new donor #
new_donor = input("Please enter the name of the new donor." '\n' "> ")
elif prompt == 'list':
        for donor in donors:
        print(donor)
elif prompt in donors:



"""Function to generate a report of donors sorted by total amounts donated"""

def print_donor_list():



"""Prompt user for input to generate thank you letter or report and validate selection"""

def main():
print("Hi there. What would you like to do?" '\n'
      "Generate a thank you letter (1)" '\n'
      "Generate a donor report (2)")
action = input("> ")
while action != 1 or 2:
    action = input("> ")
if action == 1:
    thank_you()
else:
    print_donor_list()

if __name__ == "__main__":
    main()
