def switch_first_last(n):
    return n[-1:] + n[1:-1] + n[0]



def remove_every_other(n):
    return n[::2]

def first_last_four(n):
    return n[4:-4:2]

def reversed(n):
    return n[::-1]


print(switch_first_last("Thisisalongteststring"))



