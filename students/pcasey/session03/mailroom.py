#!/usr/bin/env python

donors = [('Ed', [1, 4, 5]), ('Thomas', [3]), ('Nancy', [94, 6]), ('Sally', [42, 20, 10, 5, 60])]


def print_report():
    print("This will print a report")
    for i in range(len(donors)):
        nm = donors[i][0]
        tot = sum(donors[i][1])
        avg = find_avg(donors[i][1])
        count = len(donors[i][1])
        print("Name is: {name}".format(name=nm))
        print("Total donation is: {total}".format(total=tot))
        print("Average donation is: {average}".format(average=avg))
        print("Total number of donations is: {totalnum}".format(totalnum=count))


def send_thanks():
    print("This will write a thank you note")
    name_in = input("Enter a name:")
    for i in range(len(donors)):
        if name_in == "list":
            print(donors[i][0])
        elif name_in in donors[i][0]:
            don_in = input("Enter a donation amount:")
            if don_in.isnumeric():
                donors[name_in][1].extend([int(don_in)])


def find_name(name):
    # Return index number of name
    for i, donor in enumerate(donors):
        if donor in donors[i]:
            return i
#        return None


def find_avg(val):
    # Return the average of the list
    return sum(val)/len(val)


# here is where triple quoted strings can be helpful
msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
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
