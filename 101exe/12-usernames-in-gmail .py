# 12. How to extract usernames from emails ?
# Difficulty Level : L2

# Q. Extract the usernames from the email addresses present in the text

import re
text = "The new registrations are potter709@gmail.com , elixir101@gmail.com. If you find any disruptions, kindly contact granger111@gamil.com or severus77@gamil.com "

# Using regular expression to extract usernames

# \S matches any non-whitespace character
# @ for as in the Email
# + for Repeats a character one or more times

all_gmail = re.findall(r"\S+@\S+", text)
usernames = re.findall('(\S+)@', text)

print(usernames)
