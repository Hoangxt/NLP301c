# find the similarity between any two text documents

# input:
# text1 = "John lives in Canada"
# text2 = "John lives in America, though he's not from there"

# desired output:
# Similarity between text1 and text2 is 0.792817083631068
# import difflib


# def string_similarity(text1, text2):
#     result = difflib.SequenceMatcher(a=text1.lower(), b=text2.lower())
#     return result.ratio()


# text1 = 'John lives in Canada'
# text2 = "John lives in America, though he's not from there"
# print("Original string:")
# print(text1)
# print(text2)
# print("Similarity between text1 and text2 is ")
# print(string_similarity(text1, text2))

# Finding similarity using spaCy library
import spacy
nlp = spacy.load("en_core_web_sm")

text1 = "John lives in Canada"
text2 = "James lives in America, though he's not from there"
text3 = "hi"
text4 = "hello"
doc1 = nlp(text1)
doc2 = nlp(text2)
print(doc1.similarity(doc2))
