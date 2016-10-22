# !/usr/bin/env python3

"""
Name: Paul Briant
Date: 10/18/16
Class: Introduction to Python
Session: 03
Assignment List Lab

Description:
This module contains four unique list manipulation methods. Each method takes
a list of four fruit and modifys it. The number of elements in each list is
often increased or decreased based on user input.

"""
# -------------------------------Functions--------------------------------------


def series1(fruit):
    """
    Take in a list of strings and display the original list before prompting
    the user to add additonal items to the list. The original list is modified
    based on user input and insertions to the beginning of the list.
    """
    print(fruit)
    # Prompts user for an additional fruit
    new_fruit = input("Please enter another fruit ")
    fruit.append(new_fruit)
    print(fruit)
    number = int(input("Please enter a number "))
    # Display number and corrisponding fruit on one is first basis.
    print(number, fruit[number - 1])
    # Adds new fruit to beginning of list using concatenation
    fruit = ["Watermelon"] + fruit
    print(fruit)
    # Inserts new fruit at beginning of list
    fruit.insert(0, "Pineapple")
    print(fruit)
    # displays all fruits beginning with the letter 'P'
    for item in fruit:
        if item[0] == 'P':
            print(item)


def series2(fruit):
    """
    Take in a list of strings and display the original list before removing the
    last element of the list and prompting the user for a specific item to
    remove from the list.
    """
    print(fruit)
    # Remove last element from list
    del fruit[-1]
    print(fruit)
    # Prompts user for a fruit to remove from list
    to_delete = input("What fruit do you want deleted from this list? ")
    fruit.remove(to_delete)


def series3(fruit):
    """
    Take in a list of strings and iterate through it prompting the user
    regarding their preference for each fruit. If the user does not like the
    fruit, it is deleted from the list. If the user does not specify their
    preference, they are prompted until they do. A list of remaining fruit is
    displayed after the user has specified their preference for each fruit.
    """
    for item in fruit[:]:
        # Asks the user whether they like each fruit
        preference = input("Do you like " + item.lower() + "? yes|no ")
        # Checks to make sure user entered either 'yes' or 'no'
        if preference != 'no' and preference != 'yes':
            # Repeatedly prompts user to enter 'yes' or 'no' until they do.
            while True:
                preference = input("Please answer with either yes or no ")
                if preference == 'yes' or preference == 'no':
                    break
        if preference == 'no':
            # remove item from fruit
            fruit.remove(item)
    print(fruit)


def series4(fruit):
    """
    Take in a list of strings and reverse each letter of each item. Display the
    original list minus the last element and it's copy.
    """
    # Create copy of fruit
    rev_fruit = fruit[:]
    rev_fruit = " ".join(rev_fruit)
    rev_fruit = rev_fruit[::-1]
    rev_fruit = rev_fruit.split()
    rev_fruit.reverse()
    # Delete last item in original list
    del fruit[-1]
    print(fruit, rev_fruit)


# ==============================================================================


def main():
    """
    Calls to each series are made using the fruit list as input.
    """
    # Create original list of fruit
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    # series1(fruit)
    # series2(fruit)
    series3(fruit)
    # series4(fruit)


if __name__ == '__main__':
    main()
