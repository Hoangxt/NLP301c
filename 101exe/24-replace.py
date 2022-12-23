# 24. How to replace all the pronouns in a text with their respective object names

# Replace the pronouns in below text by the respective object nmaes

# Input :

# text=" My sister has a dog and she loves him"

# Out Output :

# [My sister,she]
# [a dog ,him ]


# Import neural coref library
# !pip install neuralcoref
import spacy
import neuralcoref

# Add it to the pipeline
nlp = spacy.load('en')
neuralcoref.add_to_pipe(nlp)

# Printing the coreferences
doc1 = nlp('My sister has a dog. She loves him.')
print(doc1._.coref_clusters)
