# Convert words into spacy tokens
import spacy
# python -m spacy download en_core_web_lg
nlp = spacy.load('en_core_web_lg')
word1 = "amazing"
word2 = "terrible"
word3 = "excellent"
token1 = nlp(word1)
token2 = nlp(word2)
token3 = nlp(word3)

# Use similarity() function of tokens
print('similarity between', word1, 'and',
      word2, 'is', token1.similarity(token2))
print('similarity between', word1, 'and',
      word3, 'is', token1.similarity(token3))
