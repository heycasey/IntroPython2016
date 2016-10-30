
def reverse_ends(string):
    return string[-1] + string[1:-2] + string[0]

def del_evry_oth_char(string):
    return string[0:-1:2]

def first_last_four(string):
    """
    removes first and last four elements of a string, and every other between
    """
    return string[4:-4:2]

def reverse_string(string):
    return string[::-1]
