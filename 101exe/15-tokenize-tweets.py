# 15. How to tokenize tweets ?
# Difficulty Level : L2

# Q. Clean the following tweet and tokenize them

# Input :

# text=" Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro :) "
import nltk
from nltk.tokenize import TweetTokenizer
import re
text = " Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro :) "
# Cleaning the tweets
text = re.sub(r'[^\w]', ' ', text)

# Using nltk's TweetTokenizer
tokenizer = TweetTokenizer()
print(tokenizer.tokenize(text))
