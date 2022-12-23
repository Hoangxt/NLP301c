#  Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.
from nltk.book import *


def vocab_size(text):
    """
    Returns the number of words in a   text.  Only alphabetic strings
    are considered.  Enclitics are removed from the count.
    """

    return len([w for w in text if w.isalpha() and w.lower not in ("d", "ll", "m", "re", "s", "t", "ve")])


def percent(word, text):
    """
    Returns the percentage that a given word comprises in a text.
    """

    word_count = len([w for w in text if w.lower() == word.lower()])
    total_words = vocab_size(text)
    return 100 * word_count/total_words


print(percent('whale', text1))
