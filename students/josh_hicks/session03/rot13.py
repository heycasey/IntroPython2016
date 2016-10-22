#!/usr/bin/env python
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm


def rot13(s):
    rot13in = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rot13out = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    rot13 = dict(zip(rot13in, rot13out))
    return s.translate(s.maketrans(rot13))


if __name__ == '__main__':
    assert rot13("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner"
