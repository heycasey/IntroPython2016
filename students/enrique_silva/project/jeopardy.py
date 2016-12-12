# The following program will simulate a game of jeopardy.
# The user will be asked to guess a letter or the complete word.
# The user will only be given 10 opportunities,
# at which time the game will be over
# if the user has not guessed the word after ten.

import random

animals = {'giraffe': ['long neck'], 'lion': ['king of the jungle'],
           'cheetah': ['has spots and is fast']}

movies = {'gladiator': ["Ancient Rome"],
          'frozen': ['let it go']}

continents = {'africa': ['the sahara'], 'antartica': ['very cold'],
              'asia': ['china is here']}


def user_prompts():
    menu = """Welcome to Jeopardy. Please pick a category:

    For Animals type: animals

    For Movies type: movies

    For continents type: continents

    To exit please type: x
    """

    start_game = """The game has started please enter 1 letter

    or a word that is {} characters in length.

    Be smart you only have 10 attempts."""

    return menu, start_game


def main(animals, movies, continents):
    """Present user with jeopardy menu,
    loop until user decides to exit"""\

    menu, _ = user_prompts()
    while True:
        print(menu)
        response = input('====> ').lower()
        if response == 'animals':
            category_choice(animals)
        elif response == 'movies':
            category_choice(movies)
        elif response == 'continents':
            category_choice(continents)
        elif response == 'x':
            break
        else:
            print('Please enter a valid entry\n')


def category_choice(category):
    """Take category and create a list. Use
    the key to get value from dictionary,
    value is a hint for the user."""

    list = [key for key in category.keys()]
    word = random.choice(list)
    hint = category[word]
    guessing_game(word, hint)


def guessing_game(word, hint):
    """Create loop that takes a user's guessGive the
    user 10 attempts to guess the word correctly."""

    _, start_game = user_prompts()
    length_word = len(word)
    print(start_game.format(length_word))
    attempts = 0
    guesses = list(length_word*'_')

    while attempts < 10:
        guess = input('===>').lower()
        if validate_guess(guess, word, guesses):
            break

        if guess in word:
            guesses = correct_guess(guess, guesses, attempts, word)

        else:
            attempts = wrong_guess(attempts, hint, word)


def validate_guess(guess, word, guesses):
    """Determine if the user's guess is a valid entry, or
    if the user has won the game. Valid entries include
    only letters and only one letter at a time If
    valid entry check if letter is a correct guess"""

    if guess == word or ''.join(guesses) == word:
        print('You won\n')
        return True

    elif len(guess) > 1:
        print('Only one letter at a time please!\n')
        # print(''.join(guesses))

    elif guess.isalpha() is False:
        print('Only letters please!\n')
        # print(''.join(guesses))

    elif guess in guesses:
        print("""You've already guessed this letter\n""")
        # print(''.join(guesses))


def correct_guess(guess, guesses, attempts, word):
    """If guess is correct, build word, by placing guess
    in appropriate position of the word. Tell the user
    they guessed correctly"""

    guesses = [guess if letter == guess else blank for
               blank, letter in zip(guesses, word)]

    print(''.join(guesses))
    print()
    print('You got one letter right, guess again you have {}'
          ' attempts remaining\n'.format(10-attempts))

    return guesses


def wrong_guess(attempts, hint, word):
    """If guess is incorrect, offer user a hint, only if less
    than two guesses. Keep track of incorrect guesses"""

    attempts += 1
    if attempts < 10:
        print('You are wrong, guess again you have {}'
              ' attempts remaining\n'.format(10-attempts))

    else:
        print('YOU LOST\n')

    if attempts < 2:
        hint_question = input("""If you would like a hint please"""
                              """ enter y if you don't want a hint"""
                              """ press n:\n """)

        if hint_question == 'y' or hint_question == 'Y':
            print(hint)
            print()

        else:
            print('So be it that was your last change'
                  ' for a hint, please guess again :) \n')

    return attempts


if __name__ == '__main__':
    main(animals, movies, continents)
