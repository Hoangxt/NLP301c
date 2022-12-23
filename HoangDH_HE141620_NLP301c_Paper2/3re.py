# Write a program that takes a sentence expressed as a single string, splits it, and counts
# up the words. Get it to print out each word and the word's frequency, one per line, in alphabetical order.

# Example:
# Input: "Reset your password if you just's can't remember your old one."

# Output:
# can't: 1
# if: 1
# just: 1
# new: 1
# one: 1
# old: 1
# password: 1
# remember: 1
# reset: 1
# your: 2

import re
import nltk
from nltk import word_tokenize


# def print_words_and_frequency(text):
#     """
#     Counts the words in a text and prints out the
#     resulting table in alphabetical order.
#     """

#     # tokenizer separates words from punctuation
#     tokens = word_tokenize(text)

#     # remove punctuation
#     words = [t.lower() for t in tokens if t.isalpha()]

#     # get word counts from FreqDist
#     ordered = sorted(set([(w, v) for w, v in nltk.FreqDist(words).items()]))

#     # get widths for pretty printing
#     # width of longest word
#     width = max([len(w) for w, _ in ordered]) + 2
#     # width of longest number
#     width_counts = max([len(str(v)) for _, v in ordered])

#     # print everything
#     for w, v in ordered:
#         print("{}:{}{:>{}}".format(w, ' ' * (width - len(w)),
#                                    v, width_counts))


# text = "Reset your password if you just's can't remember your old one."
# print_words_and_frequency(text)


def split_and_word_freq(sent):
    # splits = re.findall(r'\w+', sent)
    # dealing with phrases like it's, warm-hearted
    splits = re.findall(r"\w+(?:[-']\w+)*", sent)

    # create the word frequency using dictionary
    word_freq = {}
    for word in splits:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1

    # print word's frequency in alphabetical order
    for key in sorted(word_freq.keys()):
        print(key + ': ' + str(word_freq[key]))


sent = "Reset your password if you just's can't remember your old one."
split_and_word_freq(sent)
