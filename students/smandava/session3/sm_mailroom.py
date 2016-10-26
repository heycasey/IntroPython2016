#!/usr/bin/env python3
"""Oct 16 2016 Mail room Exercise."""
donor_list = [('Alfred Hitchcock', [10, 20, 30]),
              ('Martin Scorsese', [20, 30, 40]),
              ('Steven Spielberg', [40, 20, 30, 10]),
              ('Francis Coppola', [10, 10, 10]),
              ('Ridley Scott', [10, 20, 30, 10])]


def print_report():
    """Print Report."""
    print("This will print a report.")
    donor_list_new = []
    for index in range(len(donor_list)):
        total_amount = 0
        for sublist_index in range(len(donor_list[index][1])):
            total_amount += int(donor_list[index][1][sublist_index])
        avg_amount = (total_amount / (len(donor_list[index][1])))
        # print (donor_list[index][0],total_amount,len(donor_list[index][1]),\
        #          avg_amount)
        donor_list_new.append([donor_list[index][0], total_amount,
                              len(donor_list[index][1]), avg_amount])
        index = + 1
    # print (donor_list_new)

    def second_element(int):
        """Return 2nd element in nested lists."""
        return int[1]
    donor_list_new.sort(key=second_element, reverse=True)
    # print(donor_list_new)
    report_header = ("{0:<30s},{1:<30s},{2:<30s},{3:<30s}".
                     format('Donor Name', 'Total Amount',
                            'No.of Donations', 'Avg.Donation'))
    report_header = report_header.replace(',', '')
    print(report_header)
    for index in range(len(donor_list)):
        donation_report = ("{0:<30s},{1:<30.2f},{2:<30d},{3:<30.2f}".
                           format(donor_list_new[index][0],
                                  donor_list_new[index][1],
                                  donor_list_new[index][2],
                                  donor_list_new[index][3]))
        donation_report = donation_report.replace(',', '')
        print(donation_report)


def send_thanks():
    """Update the donor list and send a thank you note."""
    print("This will write a thank you note")
    print("Enter the word 'list' to see list of donors or \
          enter donor name followed by amount.")
    user_input = input("Enter full name of donor:")
    donation_count = len(donor_list)
    if (user_input == 'list'):
        print(donor_list)
        user_input = input("Enter full name of donor:")
    for index in range(len(donor_list)):
        while (user_input in donor_list[index]):
            try:
                d_amount = int(input("Please enter the donation amount:"))
            except ValueError:
                    d_amount = input('''Please enter only numbers
                                     for donation amount:''')
            donor_list[index][1].append((d_amount))
            donation_count = + 1
            print('''Dear {name}, Thank you very much for your generous
                  donation of ${amount}'''.
                  format(name=user_input, amount=d_amount))
            break
    else:
        if (not donation_count != len(donor_list)):
            try:
                d_amount = int(input("Please enter the donation amount:"))
            except ValueError:
                d_amount = input('''Please enter only numbers
                                     for donation amount:''')
            donor_list.append((user_input, [d_amount]))
            print('''Dear {name}, Thank you very much for your generous
            donation of ${amount}'''.format(name=user_input, amount=d_amount))


# here is where triple quoted strings can be helpful
msg = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""


def main():
    """Run the main interactive loop."""
    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip()in case there are any spaces

        if response == 'p':
            print_report()
        elif response == 's':
            send_thanks()
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')


if __name__ == "__main__":
    main()
