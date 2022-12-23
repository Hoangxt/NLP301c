# write a function that takes a list of words or string and concatenates the first two and the
# last two characters of each word that has at least 4 character

# Example:
# Input string: "Our programs and activities ensure that every student reaches their full potential"
# Output string: ['prms','aces','enre','that','evry','stnt','rees','thir','full','poal']


def concat_first_last(str):
    str = str.split()
    result = []
    for i in str:
        if len(i) >= 4:
            result.append(i[:2] + i[-2:])
    return result


str = "Our programs and activities ensure that every student reaches their full potential"
print(concat_first_last(str))
