# Grid printer


def print_grid():

    pl = "+"
    mi4 = "-"*4
    horiz = pl+mi4+pl+mi4+pl
    mid = "|    |    |"

    for i in range(2):
        print(horiz)
        for i in range(4):
            print(mid)
            i += 1
        i += 1
    print(horiz)

print_grid()
