import random

with open("holmes.txt", "r") as input_file:
    book = input_file.readlines()

book = " ".join(book)

# problem: does not strip punctuation
# use regex to replace punctuation
book_words = [word.strip() for word in book.split(" ")]

book_word_count = {}

# dictionary of word frequency
for word in book_words:
    if word in book_word_count:
        book_word_count[word] += 1
    else:
        book_word_count[word] = 1


# word list
unique_words = [key for key in book_word_count.keys()]

# list of cumulative frequency
frequency_list = [book_word_count[unique_words[0]]]
for x in range(1, len(unique_words)):
    frequency_list.append(frequency_list[x - 1] + book_word_count[unique_words[x]])


# total words
total_words = frequency_list[-1]

# random number
random_word_index = random.randint(0, total_words)

# use bisection search to find the correct place for the index
def bisect(histogram, ind, start, stop):
    midpoint = (stop + start) // 2
    if (ind == histogram[midpoint]) or (histogram[midpoint - 1] < ind and ind < histogram[midpoint + 1]):
        return midpoint
    elif ind < histogram[midpoint]:
        return bisect(histogram, ind, start, midpoint + 1)
    else:
        return bisect(histogram, ind, midpoint, stop)

print("this is the index: " + str(random_word_index))
word_index = bisect(frequency_list, random_word_index, 0, len(frequency_list))
print(word_index)
print(unique_words[word_index])
