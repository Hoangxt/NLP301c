1. Import nltk and download the ‘stopwords’ and ‘punkt’ packages
   Difficulty Level : L1

Q. Import nltk and necessary packages

Show Solution

# Downloading packages and importing

import nltk
nltk.download('punkt')
nltk.download('stop')
nltk.download('stopwords')

#> [nltk_data] Downloading package punkt to /root/nltk_data...
#> [nltk_data] Unzipping tokenizers/punkt.zip.
#> [nltk_data] Error loading stop: Package 'stop' not found in index
#> [nltk_data] Downloading package stopwords to /root/nltk_data...
#> [nltk_data] Unzipping corpora/stopwords.zip.
#> True 2. Import spacy and load the language model
Difficulty Level : L1

Q. Import spacy library and load ‘en_core_web_sm’ model for english language. Load ‘xx_ent_wiki_sm’ for multi language support.

Show Solution

# Import and load model

import spacy
nlp=spacy.load("en_core_web_sm")
nlp

# More models here: https://spacy.io/models

#> <spacy.lang.en.English at 0x7facaf6cd0f0>

<!--  -->

28. How to classify a text as positive/negative sentiment
    Difficulty Level : L2

Q. Detect if a text is positive or negative sentiment

Input :

text="It was a very pleasant day"
Desired Output:

Sentiment(polarity=0.9533333333333333, subjectivity=1.0)
Positive

Show Solution

# Sentiment analysis with TextBlob

from textblob import TextBlob
blob=TextBlob(text)

# Using the sentiment attribute

print(blob.sentiment)
if(blob.sentiment.polarity > 0):
print("Positive")

#> Sentiment(polarity=0.9533333333333333, subjectivity=1.0)
#> Positive
Note that the magnitude of polarity represents the extent/intensity . If it the polarity is greater than 0 , it represents positive sentiment and vice-versa.

<!--  -->

36. How to merge two tokens as one ?
    Difficulty Level : L3

Q. Merge the first name and last name as single token in the given sentence

Input:

text="Robert Langdon is a famous character in various books and movies "
Desired Output:

Robert Langdon
is
a
famous
character
in
various
books
and
movies

Show Solution

# Using retokenize() method of Doc object to merge two tokens

doc = nlp(text)
with doc.retokenize() as retokenizer:
retokenizer.merge(doc[0:14])

for token in doc:
print(token.text)

#> Robert Langdon
#> is
#> a
#> famous
#> character
#> in
#> various
#> books
#> and
#> movies

<!--  -->

37. How to extract Noun phrases from a text ?
    Difficulty Level : L2

Q. Extract and print the noun phrases in given text document

Input:

text="There is a empty house on the Elm Street"
Expected Output :

[a empty house, the Elm Street]

Show Solution

# Create a spacy doc of the text

doc = nlp(text)

# Use `noun_chunks` attribute to extract the Noun phrases

chunks = list(doc.noun_chunks)
chunks

#> [a empty house, the Elm Street]

38. How to extract Verb phrases from the text ?
    Difficulty Level : L3

Q. Extract the Verb Phrases from the given text

Input :

text=("I may bake a cake for my birthday. The talk will introduce reader about Use of baking")
Desired Output:

may bake
will introduce

Show Solution

# Import textacy library

!pip install textacy
import textacy

# Regex pattern to identify verb phrase

pattern = r'(<VERB>?<ADV>\*<VERB>+)'
doc = textacy.make_spacy_doc(text,lang='en_core_web_sm')

# Finding matches

verb_phrases = textacy.extract.pos_regex_matches(doc, pattern)

# Print all Verb Phrase

for chunk in verb_phrases:
print(chunk.text)

#> may bake
#> will introduce

<!--  -->

39. How to extract first name and last names present in the document ?
    Difficulty Level : L3

Q. Extract any two consecutive Proper Nouns that occour in the text document

Input :

text="Sherlock Holmes and Clint Thomas were good friends. I am a fan of John Mark"
Desired Output:

Sherlock Holmes
Clint Thomas
John Mark

Show Solution

# Import and initialize spacy's matcher

from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
doc=nlp(text)

# Function that adds patterns to the matcher and finds the respective matches

def extract_matches(doc):
pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
matcher.add('FULL_NAME', None, pattern)
matches = matcher(doc)

for match_id, start, end in matches:
span = doc[start:end]
print(span.text)

extract_matches(doc)

#> Sherlock Holmes
#> Clint Thomas
#> John Mark

<!--  -->

40. How to identify named entities in the given text
    Difficulty Level : L2

Q. Identify and print all the named entities with their labels in the below text

Input

text=" Walter works at Google. He lives in London."
Desired Output:

Walter PERSON
Google ORG
London GPE

Show Solution

# Load spacy modelimport spacy

nlp=spacy.load("en_core_web_sm")doc=nlp(text)

# Using the ents attribute of doc, identify labels

for entity in doc.ents:  
 print(entity.text,entity.label\_)

#> Walter PERSON
#> Google ORG
#> London GPE

41. How to identify all the names of Organizations present in the text with NER ?
    Difficulty Level : L2

Q. Identify and extract a list of all organizations/Companies mentioned in the given news article

Input :

text =" Google has released it's new model which has got attention of everyone. Amazon is planning to expand into Food delivery, thereby giving competition . Apple is coming up with new iphone model. Flipkart will have to catch up soon."
Expected Solution

['Google', 'Amazon', 'Apple', 'Flipkart']

Show Solution

doc=nlp(text)
list*of_org=[]
for entity in doc.ents:
if entity.label*=="ORG":
list_of_org.append(entity.text)

print(list_of_org)

#> ['Google', 'Amazon', 'Apple', 'Flipkart']

<!--  -->

45. How to find the ROOT word of any word in a sentence?
    Difficulty Level : L3

Q. Find and print the root word / headword of any word in the given sentence

Input :

text="Mark plays volleyball. Sam is not into sports, he paints a lot"
Desired Output :

Mark plays
plays plays
volleyball plays
. plays
Sam is
is paints
not is
into is
sports into
, paints
he paints
paints paints
a lot
lot paints

Show Solution

# use the head attribute of tokens to find it's rootword

doc=nlp(text)
for token in doc:
print(token.text,token.head)

#> Mark plays
#> plays plays
#> volleyball plays
#> . plays
#> Sam is
#> is paints
#> not is
#> into is
#> sports into
#> , paints
#> he paints
#> paints paints
#> a lot
#> lot paints

46. How to visualize the dependency tree in spaCy
    Difficulty Level : L2

Q. Visualize the dependencies of various tokens of the given text using spaCy

Input :

text="Mark plays volleyball. Sam is not into sports, he paints a lot"

Show Solution

# Use spacy's displacy with the parameter style="dep"

doc=nlp(text)

from spacy import displacy
displacy.render(doc,style='dep',jupyter=True)

59. How to classify a text as positive or negative sentiment with transformers?
    Difficulty Level : L4

Q. Find out whether a given text is postive or negative sentiment along with score for predictions

Input text:

text1="It is a pleasant day, I am going for a walk"
text2="I have a terrible headache"

Desired Output :

[{'label': 'POSITIVE', 'score': 0.9998570084571838}]
[{'label': 'NEGATIVE', 'score': 0.9994378089904785}]

Show Solution

# Import pipeline from transformers package

from transformers import pipeline

# Get the task specific pipeline

my_model = pipeline("sentiment-analysis")

# Predicting the sentiment with score

print(my_model(text1))
print(my_model(text2))

[{'label': 'POSITIVE', 'score': 0.9998570084571838}]
[{'label': 'NEGATIVE', 'score': 0.9994378089904785}]
