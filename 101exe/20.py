# 20. How to find the cosine similarity of two documents?
# Difficulty Level : L3

# Q. Find the cosine similarity between two given documents

# Input

# text1='Taj Mahal is a tourist place in India'
# text2='Great Wall of China is a tourist place in china'
# Desired Output :


# [[1.         0.45584231]
#  [0.45584231 1.        ]]

# Using Vectorizer of sklearn to get vector representation
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
documents = [text1, text2]

vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(documents)

# Obtaining the document-word matrix
doc_term_matrix = matrix.todense()
doc_term_matrix

# Computing cosine similarity
df = pd.DataFrame(doc_term_matrix)

print(cosine_similarity(df, df))
