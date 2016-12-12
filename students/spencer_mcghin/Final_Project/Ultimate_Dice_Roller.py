#! /usr/bin/env python3

"""

DICE ROLLER FOR ALL YOUR GAMING NEEDS!
This program will allow a user to pick from a number of dice types
and roll them individually, in multiples of the same dice, or as an assortment
of different dice.

"""

# Imports
import random
import tabulate
import sys


# Define Global Variables
""" Dict object that takes user input (keys) and matches it with the side (value).
Used mostly for UI and to validate user input against side_dict keys in dice menu function."""


side_dict = {"1": 2,
             "2": 4,
             "3": 6,
             "4": 8,
             "5": 10,
             "6": 12,
             "7": 20,
             "8": 100}


# Classes
class Dice(object):
    roll_dict = {}

    def __init__(self, side=None, number=0):
        self.side = side
        self.number = number

    @staticmethod
    def roll_dice(side, number):
        """ Generate a number of random values based on user input for die_amount in die_amount_selector. """
        rolls = []
        for _ in range(number):
            rolls.append(random.randint(1, side_dict[side]))
        Dice.roll_dict['d' + str(side_dict[side])] = rolls


# Functions for main program

def main():
    """ Jumping off point for program. Goes directly to dice_menu function. """
    print('\n'"Hail Champion and welcome to the Super Dice Roller!" '\n'
          "Please choose a die to roll from the menu below." '\n'
          "You'll be able to choose more and/or different dice afterwards. \n")
    dice_menu()


def dice_menu():
    """ Print out menu of dice options. """
    print("Choose your die! \n-------- ")
    for number, die in sorted(side_dict.items()):
        print(number + '.', 'd' + str(die))
    select_die_type()


def select_die_type():
    """ Get value for user_input variable. Will be used later to pass to roll_dice method. """
    while True:
        user_input = input("> ")
        if user_input not in side_dict.keys():
            print("Prithee select a value from the list knave!")
        else:
            die_amount_selector(user_input)


def die_amount_selector(user_input):
    """ Prompt user for amount of dice to roll. """
    try:
        die_amount = int(input("How many would you like to roll? '\n> "))
    except ValueError:
        print("Prithee select a number from the list knave!")
        die_amount_selector(user_input)
    else:
        side, number = user_input, die_amount
        Dice.roll_dice(side, number)
        roll_more_prompt()


def roll_more_prompt():
    """ Check with user if they would like to roll more / different dice. """
    print("Would you like to roll any additional dice?")
    while True:
        confirm = input("Yes (y) or No (n)? \n> ")
        if confirm == 'y':
            dice_menu()
        elif confirm == 'n':
            print_die_results()
            exit_die_roller()
        else:
            roll_more_prompt()


def print_die_results():
    """ Print formatted output for agg_dict, which contains summed  dice rolls from roll_dict class object."""
    print(tabulate.tabulate(Dice.roll_dict, headers="keys", tablefmt="fancy_grid", numalign="center"))


def exit_die_roller():
    """ Menu to prompt user to exit or roll again. If they roll again, the roll_dict object is cleared. """
    while True:
        confirm = input("Exit (e) or roll again (r)? \n> ")
        if confirm == 'e':
            sys.exit()
        elif confirm == 'r':
            Dice.roll_dict.clear()
            dice_menu()
        else:
            print("Please select from the available options.")
            exit_die_roller()


if __name__ == '__main__':
    main()
