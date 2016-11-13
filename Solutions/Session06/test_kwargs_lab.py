#!/usr/bin/env python3

"""
Test code for the args-kwargs lab

This kind of experimental code isn't all the suited to testing, but it's
not a bad way to run code as you develop it anyway...

And we want to encourage test code -- so we'll use it everywhere possible

Note: I decided that instead of having my funciton print somthing it would
return a string -- that way I could test that the returned string was correct.

"""

import pytest  # used for testing exceptions

from kwargs_lab import colors


# Calling "colors" in various ways.
def test_all_positional():
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_one_keyword():
    result = colors(link_color='purple')
    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'link: purple' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_pos_and_keyword():
    result = colors('yellow', 'gray', link_color='purple')
    # these aren't exhaustive by any means

    print(result)
    assert 'foreground: yellow' in result
    assert 'background: gray' in result
    assert 'link: purple' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_duplicate():
    """
    It's an error to have a keyword argument that duplicates a
    positional one
    """
    # this is the nifty pytest way to check for Exceptions
    with pytest.raises(TypeError):
        result = colors('yellow', fore_color='purple')
        print(result)


def test_duplicate2():
    """
    It's an error to have a keyword argument that duplicates a
    positional one
    """
    # this is a way to do it by hand:
    try:
        result = colors('yellow', fore_color='purple')
        print(result)
        assert False
    except TypeError as err:
        # you can also check if the error message is what you expect
        assert "multiple values for argument" in err.args[0]


def test_call_tuple():
    t = ('red', 'blue', 'yellow', 'chartreuse')
    result = colors(*t)

    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_call_dict():
    d = {'fore_color': 'red',
         'visited_color': 'cyan',
         'link_color': 'green',
         'back_color': 'blue',
         }
    result = colors(**d)

    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'visited: cyan' in result
    assert 'link: green' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_call_tuple_dict():
    t = ('red', 'blue')

    d = {'visited_color': 'cyan',
         'link_color': 'green',
         }
    result = colors(*t, **d)

    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'visited: cyan' in result
    assert 'link: green' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_call_everything():
    """
    this one uses:
      - a positional argument
      - *tuple
      - a keyword argument
      - **dict
    """
    t = ('red',)  # note the extra comma to amke it a tuple!

    d = {'visited_color': 'cyan'}

    result = colors('blue', *t, link_color='orange', **d)

    print(result)
    assert 'foreground: blue' in result
    assert 'background: red' in result
    assert 'visited: cyan' in result
    assert 'link: orange' in result
    # you can force a test failure if you want to see the output
    # assert False
