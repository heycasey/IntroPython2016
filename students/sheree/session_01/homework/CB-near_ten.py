"""Given a non-negative number "num", return True if num is within 2 of a multiple of 10. """


def near_ten(num):
    return num % 10 >= 8 or num % 10 <= 2


print(near_ten(12))  # True
print(near_ten(17))  # False
print(near_ten(19))  # True
print(near_ten(19))
print(near_ten(18))
print(near_ten(20))
print(near_ten(1))
print(near_ten(19))
print(near_ten(19875487349879))