# Extract and print all the nouns present in the below text

# Coverting the text into a spacy Doc
import spacy
nlp = spacy.load("en_core_web_sm")
text = "James works at Microsoft. She lives in manchester and likes to play the flute"
doc = nlp(text)

# Using spacy's pos_ attribute to check for part of speech tags
for token in doc:
    # if token.pos_=='PRON'(pronouns )
    if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
        print(token.text)
