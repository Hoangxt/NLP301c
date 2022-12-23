# Merge the first name and last name as single token in the given sentence.
# Using retokenize() method of Doc object to merge two tokens
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Robert Langdon is a famous character in various books and movies "
doc = nlp(text)
with doc.retokenize() as retokenizer:
    retokenizer.merge(doc[0:14])

for token in doc:
    print(token.text)
