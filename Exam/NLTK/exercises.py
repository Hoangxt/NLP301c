# 1. Write a Python NLTK program to split the text sentence/paragraph into a list of words.
from nltk.tokenize import SExprTokenizer
import nltk.data
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
text = '''
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
'''
print("\nOriginal string:")
print(text)
token_text = sent_tokenize(text)
print("\nSentence-tokenized copy in a list:")
print(token_text)
print("\nRead the list:")
for s in token_text:
    print(s)

# 2. Write a Python NLTK program to tokenize sentences in languages other than English.

text = '''

NLTK ist Open Source Software. Der Quellcode wird unter den Bedingungen der Apache License Version 2.0 vertrieben.  
Die Dokumentation wird unter den Bedingungen der Creative Commons-Lizenz Namensnennung - Nicht kommerziell - Keine 
abgeleiteten Werke 3.0 in den Vereinigten Staaten verteilt.
'''
print("\nOriginal string:")
print(text)
token_text = sent_tokenize(text, language='german')
print("\nSentence-tokenized copy in a list:")
print(token_text)
print("\nRead the list:")
for s in token_text:
    print(s)

# 3. Write a Python NLTK program to create a list of words from a given string.
text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
print("\nOriginal string:")
print(text)
print("\nList of words:")
print(word_tokenize(text))

# 4. Write a Python NLTK program to split all punctuation into separate tokens.
text = "Reset your password if you just can't remember your old one."
print("\nOriginal string:")
print(text)
result = WordPunctTokenizer().tokenize(text)
print("\nSplit all punctuation into separate tokens:")
print(result)

# 5. Write a Python NLTK program to tokenize words, sentence wise.
text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
print("\nOriginal string:")
print(text)
print("\nTokenize words sentence wise:")
result = [word_tokenize(t) for t in sent_tokenize(text)]
print("\nRead the list:")
for s in result:
    print(s)

# 6. Write a Python NLTK program to tokenize a twitter text.
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
tweet_text = "NoSQL introduction - w3resource http://bit.ly/1ngHC5F  #nosql #database #webdev"
print("\nOriginal Tweet:")
print(tweet_text)
result = tknzr.tokenize(tweet_text)
print("\nTokenize a twitter text:")
print(result)

# 7. Write a Python NLTK program to remove Twitter username handles from a given twitter text.
tknzr = TweetTokenizer(strip_handles=True)
tweet_text = "@abcd @pqrs NoSQL introduction - w3resource http://bit.ly/1ngHC5F  #nosql #database #webdev"
print("\nOriginal Tweet:")
print(tweet_text)
result = tknzr.tokenize(tweet_text)
print("\nTokenize a twitter text:")
print(result)

# 8. Write a Python NLTK program that will read a given text through each line and look for sentences. Print each sentence and divide two sentences with "==============".
text = '''
Mr. Smith waited for the train. The train was late.
Mary and Samantha took the bus. I looked for Mary and
Samantha at the bus station.
'''
print("\nOriginal Tweet:")
print(text)
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
print('\n==============\n'.join(sent_detector.tokenize(text.strip())))

# 9. Write a Python NLTK program to find parenthesized expressions in a given string and divides the string into a sequence of substrings.
text = '(a b (c d)) e f (g)'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))
text = '(a b) (c d) e (f g)'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))
text = '[(a b (c d)) e f (g)]'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))
print(text)
print(SExprTokenizer().tokenize(text))
text = '{a b {c d}} e f {g}'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))
