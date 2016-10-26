"""Oct 15, 2016 Slicing lab."""

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
p = a_list[-1:] + a_list[1:14] + a_list[:1]
q = a_list[0:15:2]
r = a_list[4:-4:2]
s = a_list[::-1]
l = len(a_list) // 3
t = a_list[l:-l] + a_list[-l:] + a_list[:l]
