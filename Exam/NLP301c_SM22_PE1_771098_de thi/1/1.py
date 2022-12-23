import nltk
from nltk.book import *

my_list = []

for w in text6:
    if w.endswith('ise'):
        my_list.append(w)
    elif 'z' in w.lower():
        my_list.append(w)
    elif 'pt' in w.lower():
        my_list.append(w)
    elif w.istitle():
        my_list.append(w)


# print(sorted(set(my_list)))

print(sorted(set([w for w in text6 if w.endswith('ise') or any(
    s in w.lower() for s in ('pt', 'z')) or w.istitle()])))
