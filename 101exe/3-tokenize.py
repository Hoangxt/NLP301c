# Print the tokens of the given text document
import nltk
text = "Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided."

# Tokeniation with nltk
tokens = nltk.word_tokenize(text)
for token in tokens:
    print(token)
