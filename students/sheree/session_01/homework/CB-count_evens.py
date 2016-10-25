"""Return the number of even ints in the given array."""


def count_evens(nums):
    counter = 0
    for i in nums:
        if i % 2 == 0:
            counter += 1
    return counter

# Example Cases
print(count_evens([2, 1, 2, 3, 4]))  # 3
print(count_evens([2, 2, 0]))  # 3
print(count_evens([1, 3, 5]))  # 0
