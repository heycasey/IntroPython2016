# Charles Robison
# 2016.10.16
# Mailroom Lab

# Initial version using dictionary.  Abandoning for now...

#!/usr/bin/env python

donors = {
            'Smith':[100, 125, 100],
            'Galloway':[50],
            'Williams':[22, 43, 40, 3.25],
            'Cruz':[101],
            'Maples':[1.50, 225]
         }

donations = {}
for k, v in donors.items():
    donations[k] = sum(v)

def print_report():
    print("This will print a report")
    print("Name","\t","Donated","\t", "Times Donated", "\t", "Avg Donated")
    for i in donations:
        print(i, "\t", donations[i], "\t", len(donors[i]), "\t", donations[i]/len(donors[i]))


def send_thanks():
    print("This will write a thank you note")
    while True:
        print(ty_msg)
        response = input("==> ").strip()

        if response == 'list':
            for i in donations:
                print(i)
        elif response == 'add':
            pass
        elif response == 'x':
            break
        else:
            print('please type "list", "add" or "x"')



# here is where triple quoted strings can be helpful
msg = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""

ty_msg = """
Would you like to see a list of donors or add a new donor?
To see a list: type "list"
To enter a new donor: type "add"
To exit: type "x"
"""


def main():
    """
    run the main interactive loop
    """

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip() in case there are any spaces

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