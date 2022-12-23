# Write code to print out an index for a lexicon, allowing someone to look up words according to their meanings (or pronunciations; whatever properties are contained in lexical entries).
import nltk
entries = nltk.corpus.cmudict.entries()
d = {}

for word, pronunciation in entries:
    for phoneme in pronunciation:
        # create item if it doesn't exist
        # if it does exist, add current word
        d.setdefault(phoneme, []).append(word)


def find_all_entries(d, arg1, *args):
    """
    Returns a set of words using the phonemes
    in arg1 and args.

    Arguments:

    d:    A dictionary of items.
    arg1: The first index to be match.
    args: Optional 2nd - nth indices to be matched.
    """

    rest = set(d[arg1])
    for a in args:
        rest = rest.intersection(set(d[a]))

    return rest


print(find_all_entries(d, 'AE2', 'B', 'D', 'IH0', 'K'))
