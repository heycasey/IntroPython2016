#!/usr/bin/env python

donor_list = {'Bill Clinton': [100, 200, 300], 'Hilary Clinton': [200, 400],
              'Chelsea Clinton': [50], 'Barrack Obama': [250, 350, 450],
              'Michele Obama': [100, 300]}


def main():
    while True:
        display_menu()
        selection = input("->")
        if selection == "1":
            do_thankyou()
        elif selection == "2":
            do_report()
        elif selection == 'q':
            break


def display_menu():
    print("Choose an action:")
    print(" 1. Send a Thank You")
    print(" 2. Create a Report")
    print(" q. Exit")


def do_thankyou():
    print("Enter donor's full name (type 'list' for donor list, 'r' "
          "to return to main menu)")
    donor_name = input("->")
    if donor_name == "list":
        show_donorlist()
    elif donor_name == "r":
        pass
    else:
        while True:
            donation_amount = input("Enter donation amount ('r' to return "
                                    "to main menu):")
            if donation_amount == "r":
                break
            else:
                try:
                    donation_amount = int(donation_amount)
                    break
                except Exception as e:
                    print("Invalid input: Not an Integer")
        add_donation(donor_name, donation_amount)


def show_donorlist():
    print("Donor List:")
    for donor, contributions in donor_list.items():
        print("{0}: {1}".format(donor, ','.join(map(str, contributions))))
    print()


def add_donation(donor, amount):
    try:
        contribution_list = donor_list[donor]
        contribution_list.append(amount)
        print("Donation recorded successfully!")
        print("{0}: {1}".format(donor, ','.join(map(str, contribution_list))))
        print()
        print("Dear {0},\n\nThank you for your gracious contribution of {1}!\n"
              "We greatly appreciate your support!\n\nSincerely,\nJosh Hicks\n"
              .format(donor, amount))
    except Exception as e:
        print("Donor not found")


def do_report():
    sorted_donor_list = []
    for donor, contributions in donor_list.items():
        contribution_total = 0
        total_donations = 0
        average_donation = 0
        for contribution in contributions:
            contribution_total += contribution
        total_donations = len(contributions)
        average_donation = contribution_total // total_donations
        sorted_donor_list.append([donor, contribution_total, total_donations,
                                 average_donation])
    sorted_by_second = sorted(sorted_donor_list, key=lambda tup: tup[1])
    template = "{0:20}| {1:13}| {2:19}| {3:23}"
    print()
    print(template.format("Donor Name", "Total Donated", "Number of Donations",
                          "Average Donation Amount"))
    for donor in sorted_by_second:
        print(template.format(*donor))
    print()


if __name__ == '__main__':
    main()
