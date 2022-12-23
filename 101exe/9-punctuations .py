# 9. How to remove punctuations ? (chấm câu)

# Q. Remove all the punctuations in the given text

import nltk
text = "The match has concluded !!! India has won the match . Will we fin the finals too ? !"

# Method 1
# Removing punctuation in nltk with RegexpTokenizer
tokenizer = nltk.RegexpTokenizer(r"\w+")

# Tokenization using word_tokenize()
tokens = tokenizer.tokenize(text)

print(" ".join(tokens))
