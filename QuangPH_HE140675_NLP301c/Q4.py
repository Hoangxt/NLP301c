import spacy

text="John is happy finally. He had landed his dream job finally. He told his mom. She was elated "

nlp=spacy.load("en_core_web_sm")
doc=nlp(text)

for token in doc:
  if token.pos_=='PRON':
    print(token.text)