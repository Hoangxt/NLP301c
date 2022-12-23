# 3. Write a Python NLTK program to create a list of words from a given string.
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
print("\nOriginal string:")
print(text)
print("\nList of words:")
print(word_tokenize(text))
