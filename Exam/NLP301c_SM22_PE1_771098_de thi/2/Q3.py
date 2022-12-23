from nltk.tokenize import sent_tokenize, word_tokenize

text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
print("\nOriginal string:")
print(text)
print("\nTokenize words sentence wise:")
result = [word_tokenize(t) for t in sent_tokenize(text)]
print("\nRead the list:")
for s in result:
    print(s)
