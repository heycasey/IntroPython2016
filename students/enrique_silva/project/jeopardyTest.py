#this programs provides unit tests for the the jeopardy program.


from jeopardy import correct_guess, validate_guess, wrong_guess


def test_validate_guess():
    word = 'lion'
    guess = 'lion'
    guesses = list(guess)
    assert validate_guess(guess, word, guesses) is True


def test_correct_guess():
	guess = 'l'
	word = 'lion'
	guesses= (len(word) * '_')
	attempts=0
	something = correct_guess(guess, guesses, attempts, word)

	assert ''.join(something) == 'l___'







