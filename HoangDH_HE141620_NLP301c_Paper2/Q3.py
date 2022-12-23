# Write a function that takes a string and doubles each vowel(aeiouy), inserting
# the consonant "l" in between.
# Hint: use a regexp
# Example:
# Input string: strange_string = "Strange women lying in ponds distributing swords is no basis for a system of government"
# Output string: "Stralangele wolomelen lylyiling ilin polonds dilistrilibulutiling swolords ilis nolo balasilis folor ala sylystelem olof golovelernmelent"

# using re module
# import re

# def double_vowel(string):
#     return re.sub(r'([aeiouy])', r'\1l\1', string)


# strange_string = "Strange women lying in ponds distributing swords is no basis for a system of government"
# print(double_vowel(strange_string))

# using regexp

def double_vowel(string):
    vowels = 'aeiouy'
    result = ''
    for char in string:
        if char in vowels:
            result += char + 'l' + char
        else:
            result += char
    return result


strange_string = "Strange women lying in ponds distributing swords is no basis for a system of government"
print(double_vowel(strange_string))
