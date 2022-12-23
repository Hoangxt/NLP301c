
from nltk.tokenize import word_tokenize

text = "Last week, the University of Cambridge shared its own research"
print("\nOriginal string:")
print(text)
token_text = word_tokenize(text)

print("\nThe tokens of the given text document:")
for s in token_text:
    print(s)
