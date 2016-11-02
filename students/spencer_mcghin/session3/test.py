import numpy, collections

from tabulate import tabulate

donors = {"Nick Padgett": [12312, 34230, 38593],
          "Julia Allen": [49203, 5023, 9052],
          "Pete Tamisin": [9503, 2093, 10932, 40923],
          "Charles Elliott": [209, 50912, 9026],
          "Andy Rocha": [20968, 2091, 8934],
          "Beth DeSousa": [29092, 5906, 8734]}


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


# Print total donor donations #

# def print_donation_total():
#     totals_dict = {"Total $": []}
#     for donor, donations in sorted(donors.items()):
#         totals_dict["Total $"].append((sum(donations)))
#     return totals_dict
#
# # Print total number of donations #
#
# def print_num_donations():
#     num_results = {"Number of Donations": []}
#     for donor, donations in sorted(donors.items()):
#         num_results["Number of Donations"].append(len(donations))
#     return num_results
#
# # Print average donation #
#
# def print_avg_donation():
#     avg_results = {"Average Donation": []}
#     for donor, donations in sorted(donors.items()):
#         avg_results["Average Donation"].append(int(numpy.mean(donations)))
#     return avg_results


print(tabulate(report_data(), headers="keys", tablefmt="fancy_grid", numalign="center"))
