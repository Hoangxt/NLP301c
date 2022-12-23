# write a function that takes a text and a  vocabulary as its arguments and returns the set of words
# that appear in the text but not in the vocabulary. Both arguments can be represented as lists of strings.

from nltk import word_tokenize


def return_vocab_not_in_text(text, vocab):
    """
    Returns strings in text but not in vocab.

    Arguments:

    text:  A list of strings, a set of strings, or a string.
    vocab: A list of strings, a set of strings, or a string.
    """

    # if text and vocab are some combination of set and list
    if isinstance(text, set) and isinstance(vocab, set):
        return text.difference(vocab)
    elif isinstance(text, list) and isinstance(vocab, set):
        return set(text).difference(vocab)
    elif isinstance(text, set) and isinstance(vocab, list):
        return text.difference(set(vocab))

    # if text is a str
    if type(text) == str:
        text = word_tokenize(text)
    else:
        assert isinstance(text,
                          list), "Argument `text` must be a list or a string"

    # if vocab is a str
    if type(vocab) == str:
        vocab = word_tokenize(vocab)
    else:
        assert isinstance(vocab,
                          list), "Argument `vocab` must be a list or a string"

    return set(text).difference(set(vocab))
