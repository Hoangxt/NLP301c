# 11. How to lemmatize a given text ?
# Difficulty Level : L2

# Q. Perform lemmatzation on the given text

# Lemmatization using spacy's lemma_ attribute of token
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."
doc = nlp(text)

lemmatized = [token.lemma_ for token in doc]
print(" ".join(lemmatized))
