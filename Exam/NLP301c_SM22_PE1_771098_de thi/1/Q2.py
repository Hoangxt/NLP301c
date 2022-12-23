#  Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.

from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.book import *


def find_most_frequent_non_stopwords(text, n=50, lang='english'):
    stopwords_set = set(stopwords.words(lang))
    words = [w.lower() for w in text if w.lower().isalpha()
             and w.lower() not in stopwords_set]
    fdist = FreqDist(words)
    return fdist.most_common(n)


print(find_most_frequent_non_stopwords(brown.words(), 50), end='')
