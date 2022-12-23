# 14. How to do spell correction in a given text ?
# Difficulty Level : L2

# Q. Correct the spelling errors in the following text

import textblob

from textblob import TextBlob

# Using textblob's correct() function
text = "He is a gret person. He beleives in bod"
text = TextBlob(text)
print(text.correct())
