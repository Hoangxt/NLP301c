# Q. Perform stemming/ convert each token to it’s root form in the given text

import nltk
from nltk.stem import PorterStemmer

text = "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."

stemmer = PorterStemmer()
stemmed_tokens = []
for token in nltk.word_tokenize(text):
    stemmed_tokens.append(stemmer.stem(token))

print(" ".join(stemmed_tokens))
