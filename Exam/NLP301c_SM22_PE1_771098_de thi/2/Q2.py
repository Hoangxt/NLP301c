# Write a program to find all words that occur at least three times in the Brown Corpus.
import nltk
from nltk.corpus import brown

d = dict()
for w in brown.words():
    d[w.lower()] = 1 + d.get(w.lower(), 0)
wordtypes = set(w.lower() for w in brown.words())
more_than_3 = [w for w in wordtypes if d[w] >= 3]

print(len(more_than_3))

cfd = nltk.FreqDist(w.lower() for w in brown.words())

for t in more_than_3[:15]:
    print(t + ":", cfd[t])
