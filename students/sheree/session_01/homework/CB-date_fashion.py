"""
 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
"""


def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return int(0)
    elif you >= 8 or date >= 8:
        return int(2)
    else:
        return int(1)

print(date_fashion(5, 10)) # 2
print(date_fashion(5, 2))  # 0
print(date_fashion(4, 5))  # 1
print(date_fashion(3, 5))
print(date_fashion(2, 4))
print(date_fashion(1, 3))
print(date_fashion(0, 2))
print(date_fashion(9, 2))
print(date_fashion(9, 11))
print(date_fashion(10, 2))
