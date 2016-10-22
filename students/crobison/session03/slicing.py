# Charles Robison
# 2016.10.11
# Slicing Lab

name = 'charles'

#return a sequence with the first and last items exchanged.
print('swapped:')
print(name[6]+name[1:6]+name[0])
print(name[-1:]+name[1:-1]+name[:1])

#return a sequence with every other item removed
print('every other:')
print(name[::2])

#return a sequence with the first and last 4
# items removed, and every other item in between
print('every other and last 4 removed:')
long_name = 'charlesedwardrobison'
print(long_name[4:-4:2])

#return a sequence reversed (just with slicing)
print('reversed:')
print(long_name[::-1])

#return a sequence with the middle third, then last 
#third, then the first third in the new order
print(len(long_name))
def thirds(seq):
    i = len(seq)//3
    return seq[i:-i] + seq[-i] + seq[i]

thirds('this is a very long sentence')