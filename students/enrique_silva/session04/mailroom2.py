#!/usr/bin/env python

# User prompt at the beggining of program, asking what the user would like to do.

donor_list={
'enrique silva': ['Enrique Silva', [100, 200, 300]],
'jon smith' : ['Jon Smith', [200, 300, 400]],
'ally smith' : ['Ally Smith',[200, 300, 500]],
'anny gill' : ['Anny Gill', [300, 600, 1500]],
'terry bill' : ['Terry Bill', [500, 750, 1000]]
}

msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""

def main(donor_list):
    """run the main interactive loop"""

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip() in case there are any spaces

        if response == 'p':
            print_report(donor_list)
        elif response == 's':
            send_thanks(donor_list)
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')
        print()

def send_thanks(donor_list):
    """Send a thank you note to donor, add the donor to the list, or  accept
    a new donation"""
    user_name=str(input("""Type "list" to see donors in database or enter first name and last name: """))
    user_name=str(user_name.strip().lower())
    print()
    if user_name== 'list':
        print_donor_list(donor_list)
    else:
        search_donor_list(donor_list,user_name)

def print_donor_list(donor_list):
    for donor in donor_list:
        print(donor)

def search_donor_list(donor_list, user_name):
    """search thorugh list for name entered by potential donor, if name does not exist
    add name to and ask for donation, if it does, as for donation"""

    if user_name in donor_list:
        print('Welcome back!')
        print()
        prompt_donation_existing(donor_list, user_name)
    else:
        user_name_cap=user_name.title()
        donor_list[user_name]=[user_name_cap,[]]
        print (user_name_cap,', you are now registered in our donor database, congratulations!')
        print()
        prompt_donation_new(donor_list,user_name)

def prompt_donation_existing(donor_list, user_name):
     """ensure donation amount is an int and add donation to list for the existing donor"""
     try:
        donation_amount= int(input('How much would you like to donate? '))
        print()
        donor_list[user_name][1].append(donation_amount)
        send_email(donor_list, user_name,donation_amount)
     except ValueError:
        print('Please enter a valid integer')


def prompt_donation_new(donor_list, user_name):
     """ensure donation amount is an int and add donation to list for the new donor"""
     try:
        donation_amount= int(input('How much would you like to donate? '))
        donor_list[user_name][1].append(donation_amount)
        send_email(donor_list, user_name,donation_amount)
     except ValueError:
        print()
        print('Please enter a valid integer')

def send_email(donor_list, user_name, donation_amount):
    """write and send email to donor, thanking them for donation"""
    print('Hello {},\n\nThank you for generous danation of {:d}.\n\nSincerely, THE STAFF'.format(user_name,donation_amount))
    print()
    print(donor_list)


def print_report(donor_list):
    """print a report, that lists donor, total given, number of gifts, and average donation amounts"""
    report_entries=[]
    for values in donor_list.values():
        total_donations = sum(values[1])
        count_gifts = len(values[1])
        avg_donation = total_donations / count_gifts
        donor= values[0]
        report_entries.append((donor, total_donations, count_gifts,avg_donation))

    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Donated", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_entries:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))



main(donor_list)

