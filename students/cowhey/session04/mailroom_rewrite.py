#!/usr/bin/env python3

donors = {"Wilmot Filipe": [18.00, 72.00],
          "Neoptolemus Yaropolk": [36.00],
          "Mahesha Diogenes": [90.00, 54.00, 18.00],
          "Arthur Tjaz": [18.00],
          "Luuk Sinclair": [180.00]}

still_running = True

def end_program():
    global still_running
    still_running = False

def accept_donation():
    amount = input("How much did this person donate? \n")
    if amount == "x" or check_if_number(amount):
        return amount
    else:
        print("You must enter a numeric amount.")
        return accept_donation()

def check_if_number(num):
    try:
        float(num)
        return True
    except ValueError or TypeError:
        return False


def create_reports():
    donor_rows = []
    for donor in donors.keys():
        new_row = []
        new_row.append(donor)
        new_row.append("{:.2f}".format(sum(donors[donor])))
        new_row.append(str(len(donors[donor])))
        new_row.append("{:.2f}".format(float(new_row[1]) / int(new_row[2])))
        donor_rows.append(new_row)
    return donor_rows


def format_row(row):
    formatted = []
    for item in row:
        formatted.append('{:30}'.format(item))
    return ' '.join(formatted)


def print_donor_list():
    print("These are the donors you have in your database:")
    for donor in list(donors.keys()):
        print(donor)
    print()


def print_report():
    print("This will print a report")
    header_row = ["Name", "Total Donated", "Number of Donations", "Average Donation"]
    donor_rows = create_reports()
    donor_rows.sort(key=total_donation_amount, reverse=True)
    print(format_row(header_row))
    for row in donor_rows:
        print(format_row(row))
    print()


def send_thanks():
    print("This will write a thank you note")
    donor_names = list(donors.keys())
    thank_you_command = input("Type the full name of the person you would like to thank. \nOr type 'list' to see a list of donors.\n")
    if thank_you_command.lower() == "x":
        return
    elif thank_you_command.lower() == "list":
        print_donor_list()
    else:
        donation_amount = accept_donation()
        if donation_amount == "x":
            return
        else:
            donation_amount = float(donation_amount)
        if thank_you_command in donor_names:
            name = thank_you_command
            donors[name].append(donation_amount)
            print("Adding ${:02.2f} to {}'s donations.".format(donation_amount, name))
                # this is where i am in for converting to new standards
            print_thank_you(name)
        else:
            print(donation_amount)
            name = thank_you_command
            donors[name] = [donation_amount]
            print("Adding {} as a donor, with a donation of ${:02.2f}.".format(name, donation_amount))
            print_thank_you(name)



# here is where triple quoted strings can be helpful
msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To write thank yous to all donors: type "w"
To exit: type "x"
"""

def main():
    """
    run the main interactive loop
    """

    response = ""
    # keep asking until the users responds with an 'x'
    global still_running
    while still_running:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip().lower()  # strip() in case there are any spaces
        if response in functions.keys():
            functions[response]()
        else:
            print('please type "s", "p", or "x"')


def print_thank_you(donor):
    print("Writing this thank you to disk: ")
    letter = "Dear {},\nThank you for your gift of ${:02.2f} to the Fund for Unmatched Socks. \nYour help will be greatly appreciated by all those who partake in our holey work.".format(donor, donors[donor][-1])
    print(letter)
    print()
    file_name = donor.replace(" ", "_") + ".txt"
    with open(file_name, "w") as output_text:
        output_text.writelines(letter)

def total_donation_amount(donor_row):
    return float(donor_row[1])


def write_all_thank_yous():
    for donor in donors.keys():
        print_thank_you(donor)


functions = {"x": end_program,
             "p": print_report,
             "s": send_thanks,
             "w": write_all_thank_yous
             }


if __name__ == "__main__":
    main()
