# Write a function that takes a list of words (containing duplicates) and returns a list of words (with no duplicates) sorted by
# decreasing frequency.

import nltk


def decreasing_freq_with_no_duplicates(words):
    wordset = set(words)
    fdist = nltk.FreqDist(words)
    return sorted(wordset,
                  key=lambda x: fdist[x],
                  reverse=True)


words = ['one', 'two', 'two', 'four', 'four', 'four', 'four', 'three', 'three']
print(decreasing_freq_with_no_duplicates(words))
