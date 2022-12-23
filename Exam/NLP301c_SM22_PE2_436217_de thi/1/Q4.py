# Extract the Verb Phases from the given text
import textacy
text = ("I may bake a cake for my birthday. The talk will introduce reader about Use of baking")
# Regex pattern to identify verb phrase
pattern = r'(<VERB>?<ADV>*<VERB>+)'
doc = textacy.make_spacy_doc(text, lang='en_core_web_sm')

# Finding matches
verb_phrases = textacy.extract.pos_regex_matches(doc, pattern)

# Print all Verb Phrase
for chunk in verb_phrases:
    print(chunk.text)
