from nltk.tokenize import sent_tokenize

text = '''

NLTK ist Open Source Software. Der Quellcode wird unter den Bedingungen der Apache License Version 2.0 vertrieben.  
Die Dokumentation wird unter den Bedingungen der Creative Commons-Lizenz Namensnennung - Nicht kommerziell - Keine 
abgeleiteten Werke 3.0 in den Vereinigten Staaten verteilt.
'''
print("\nOriginal string:")
print(text)
token_text = sent_tokenize(text, language='german')
print("\nSentence-tokenized copy in a list:")
print(token_text)
print("\nRead the list:")
for s in token_text:
    print(s)
