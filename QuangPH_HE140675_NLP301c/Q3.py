# write code to initialize a two-dimensional array of sets call word_vowels and process
# a list of words, adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.


word_vowels = [[]]
words = ['The', 'dog', 'gave', 'John', 'the',
         'newspaper', 'The', 'cat', 'miowed']

l = []
for i in words:
    l.append(len(i))
m = max(l)

for i in range(1, m+2):
    word_vowels.append([])

for i in range(m+2):
    for j in range(100):
        word_vowels[i].append([])

for w in words:
    l = len(w)
    v = 0
    v += w.count('u')
    v += w.count('e')
    v += w.count('o')
    v += w.count('a')
    v += w.count('i')
    word_vowels[l][v].append(w)

print(set(word_vowels[3][1]))
print(set(word_vowels[9][3]))
