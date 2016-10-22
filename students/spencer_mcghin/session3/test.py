import numpy

"""Dictionary of Donors and Amounts Donated"""

donors = {"Nick Padgett": [12312, 34230, 38593],
          "Julia Allen": [49203, 5023, 9052],
          "Pete Tamisin": [9503, 2093, 10932, 40923],
          "Charles Elliott": [209, 50912, 9026],
          "Andy Rocha": [20968, 2091, 8934],
          "Beth DeSousa": [29092, 5906, 8734]}

# Print donor list #

def print_donor_list():
    for donor, donation in sorted(donors.items()):
        print(donor)

# Print total donor donations #

def print_donation_total():
    totals_results = []
    for donor, donations in sorted(donors.items()):
        totals_results.append((sum(donations)))
    print(totals_results)


# Print total number of donations #

def print_num_donations():
    num_results = []
    for donor, donations in sorted(donors.items()):
        num_results.append(len(donations))
    print(num_results)


# Print average donation #

def print_avg_donation():
    avg_results = []
    for donor, donations in sorted(donors.items()):
        avg_results.append(int(numpy.mean(donations)))
    print(avg_results)


print_donor_list()

print_donation_total()

print_num_donations()

print_avg_donation()
