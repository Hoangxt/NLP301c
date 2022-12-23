import nltk
from nltk.tokenize import word_tokenize


def word_percent(string, text):
    c = text.count(string)
    words = word_tokenize(text.strip())
    return c / len(words) * 100.0


text = 'Our programs and activities ensure that every student reaches their full potential'
string = 'es'
print(word_percent(string, text))
