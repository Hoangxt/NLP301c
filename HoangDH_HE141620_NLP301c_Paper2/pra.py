# Write a Python program to calculate the length of a string.

def length_of_string(string):
    return len(string)


string = "Our programs and activities ensure that every student reaches their full potential"
print(length_of_string(string))

# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'


def count_char(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


print(count_char('google.com'))
