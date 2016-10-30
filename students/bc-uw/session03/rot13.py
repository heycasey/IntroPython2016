"""
Rot13 exercise:

This module should provide at least one function called rot13 that takes any amount of text and returns that same text encrypted by ROT13.

This function should preserve whitespace, punctuation and capitalization.
"""


def rot13(text):
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    return text.translate(table)


if __name__ == '__main__':
    print(rot13("Great news everyone!"))   
