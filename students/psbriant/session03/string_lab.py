"""
Name: Paul Briant
Date: 10/18/16
Class: Introduction to Python
Session: 03
Assignment String Lab

Description:
This program explores various ways to format strings.
"""
# -------------------------------Functions--------------------------------------


def str_format1(num_list):
    """
    Takes a list of three ints as input pads the first, rounds the second and
    converts the third to scientific notation.
    """
    print("File {:03d}: \t{:.2f}, {:.0e}".format(num_list[0], num_list[1],
          num_list[2]))


def str_format2(str_tuple):
    """
    Takes a dynamic tuple of ints and outputs them with some added formating.
    """
    t_len = len(str_tuple)
    f_string = '{:d}, ' * t_len
    print("The {:d} numbers are: ".format(t_len) + f_string.format(*str_tuple))


def main():
    """
    Tests each method to verify specified parameters return expected output.
    """
    # num_list = [2, 123.4567, 10000]
    # str_format1(num_list)
    # str_format1([10, 1.999, 100])
    # str_format1([100, 0.117, 567])
    t1 = (1, 2, 3)
    str_format2(t1)
    t2 = (1, 2, 3, 4, 5)
    str_format2(t2)

if __name__ == '__main__':
    main()
