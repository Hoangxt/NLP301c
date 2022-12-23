from nltk.tokenize import word_tokenize

s = "xin chao cac ban sinh vien fpt fuck fap"  # define text s

# def common_string(text):
#     words = word_tokenize(text.strip())
#     list = []
#     count = []
#     for w in words:
#         if list.count(w[0]) == 0:
#             list.append(w[0])
#             count.append(1)
#         else:
#             a = list.index(w[0])
#             count[a]+=1
#     m = max(count)
#     i = count.index(m)
#     return list[i]
# print(common_string(s))

# write a function that takes a list of words and returns the most common word last character


def common_string(text):
    words = word_tokenize(text.strip())
    list = []
    count = []
    for w in words:
        if list.count(w[-1]) == 0:
            list.append(w[-1])
            count.append(1)
        else:
            a = list.index(w[-1])
            count[a] += 1
    m = max(count)
    i = count.index(m)
    return list[i]


print(common_string(s))
