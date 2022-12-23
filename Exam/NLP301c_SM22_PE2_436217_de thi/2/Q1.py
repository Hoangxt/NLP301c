# Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.
from nltk.book import *

four_letter_fd = FreqDist(w.lower() for w in text5 if len(w) == 4)

print(four_letter_fd.most_common(100), end='')
