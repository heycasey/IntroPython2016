# Slicing lab

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def swapends(b):
    b = a[0], a[-1] = a[-1], a[0]
    return b


def everyother(a):
    return a[0::2]


def delfour(a):
    return a[4:-4:2]


def reverse(a):
    return a[::-1]


def midlastfirst(a):
    b = len(a) // 3
    c = a[b:-b] + a[-b:] + a[:b]
    return c
