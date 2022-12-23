import numpy as np
from typing import List


def find_word(s: str, suffix: str) -> List[str]:
    result = []
    s = s.strip().split()
    for word in s:
        if word.endswith(suffix):
            result.append(word)
    return result


print(find_word('don lie me asjdk ize asdfize', 'ize'))
