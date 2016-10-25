# # 10.1
#
# tens_list = [10, 20, 30, 40]
# funny_strings = ['crunchy frog', 'ram bladder', 'lark vomit']
# some_other = ['spam', 2.0, 5, [10, 20]]
#
# empty_list = []
#
# print(tens_list)
# print(funny_strings)
# print(some_other)
# print(empty_list)
# print()
# print(tens_list[1:])
# print(funny_strings[1])
# print(some_other[::2])

# # 10.2
# food_birds = ['chicken', 'turkey']
#
# food_birds[0] = 'seagull'
# print(food_birds)

# 10.3

# cheeses = ['cheddar', 'gouda', 'munster']
#
# for cheese in cheeses:
#     print(cheese)
#
# print()
#
# numbers = [1, 2, 3, 4, 5]
#
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
#
# print(numbers)
#
# print()
#
# for x in []:
#     print("this won't execute")
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
#

# 10.7

# def add_all(t):
#     total = 0
#     for x in t:
#         total += x
#     return total
#
# print("Result of add all function is {0}".format(add_all([1, 2, 3])))

# exercise 1

# def nested_sum(lists_of_list_of_ints):
#     for lists in lists_of_list_of_ints:
#         print(sum(lists))
#         pass
#
# print(nested_sum([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
#
# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res
#
# print(capitalize_all(["ahoy there."]))

# """
# Exercise 3
# Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
# """
#
# list_to_update = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def cumulativer(nums):
#     sums = 0
#     cums_list = []
#     for i in nums:
#         sums += i
#         cums_list.append(sums)
#     return cums_list
#
# print(cumulativer(list_to_update))

# 10.8

# t = ['a', 'b', 'c']
# x = t.pop(1)
# print(t)
# x = t.pop()
# print(t)
# print(x)

# """Exercise 4
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3]."""
#
#
# def middle(str):
#     return str[1:-1]
#
# print(middle("Oklahoma"))
# print(middle("Michelle Obama"))
# print(middle("Beyonce Knowles"))

# """Exercise 5
# Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None."""
#
# def chop(lst):
#     lst = lst[1:-1]
#     print(lst)
#     return None
#
# chop(["Apple", "Banana", "Canteloupe"])

